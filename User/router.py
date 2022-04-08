from typing import List

from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session

from Database import db

from . import schema
from . import services
from . import validator

api_router = APIRouter(
    tags=['Users']
)


@api_router.post('/user/', status_code=status.HTTP_201_CREATED, response_model=schema.User)
async def create_user_registration(user_in: schema.UserCreate, db_session: Session = Depends(db.get_db)):
    # Read More : Pydantic Validation with Database (https://github.com/tiangolo/fastapi/issues/979)

    user = await validator.verify_email_exist(user_in.email, db_session)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )

    new_user = await services.new_user_register(user_in, db_session)
    return new_user

@api_router.get('/user/', response_model=List[schema.User])
async def get_all_users(db_session: Session = Depends(db.get_db)):
    return await services.all_users(db_session)

@api_router.get('/user/{user_id}', response_model=schema.User)
async def get_user_by_id(user_id: int, db_session: Session = Depends(db.get_db)):
    return await services.get_user_by_id(user_id, db_session)