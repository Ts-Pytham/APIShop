from fastapi import Depends, HTTPException, status
from typing import List
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from Users.models import User
from Database import db
from Auth import schema
from . import config
auth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def create_access_token(*, sub:str) -> str:
    return create_token("access_token", lifetime=timedelta(minutes=config.settings.ACCESS_TOKEN_EXPIRE_MINUTES), sub=sub)

def create_token(token_type : str, lifetime : timedelta, sub : str) -> str:
    payload = {}
    expire = datetime.utcnow() + lifetime
    payload["exp"] = expire
    payload["type"] = token_type
    payload["iat"] = datetime.utcnow()
    payload["sub"] = sub
    return jwt.encode(payload, config.settings.SECRET_KEY, config.settings.ALGORITHM)

async def get_current_user(db: Session = Depends(db.get_db), token : str = Depends(auth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, config.settings.SECRET_KEY, algorithms=[config.settings.ALGORITHM], options={"verify_aud": False})
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schema.TokenData(username=username)
    
    except jwt.JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.email == token_data.username).first()
    
    if user is None:
        raise credentials_exception

    return user