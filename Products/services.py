from typing import List
from sqlalchemy.orm import Session
from . import models
from . import schema


async def create_new_category(category: schema.CategoryCreate, db_session: Session) -> models.Category:
    db_category = models.Category(**category.dict())
    db_session.add(db_category)
    db_session.commit()
    db_session.refresh(db_category)
    return db_category


async def get_all_categories(db_session: Session) -> List[models.Category]:
    categories = db_session.query(models.Category).all()
    return categories


async def get_category_by_id(category_id: int, db_session: Session) -> models.Category:
    category_info = db_session.query(models.Category).get(category_id)
    return category_info


async def delete_category_by_id(category_id: int, db_session: Session):
    db_session.query(models.Category).filter(models.Category.id == category_id).delete()
    db_session.commit()