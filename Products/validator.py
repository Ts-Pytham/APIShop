from typing import Optional

from sqlalchemy.orm import Session

from . import models


async def verify_category_exist(category_id: int, db_session: Session) -> Optional[models.Category]:
    return db_session.query(models.Category).filter(models.Category.id == category_id).first()