from typing import Optional

from sqlalchemy.orm import Session

from .models import User


async def verify_email_exist(email: str, db_session: Session) -> Optional[User]:
    return db_session.query(User).filter(User.email == email).first()

async def verify_user_exits(id : int, db_session: Session) -> Optional[User]:
    return db_session.query(User).filter(User.id == id).first()