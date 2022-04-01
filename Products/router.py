from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from typing import Any, List

from Database import db
from . import schema
from . import services
api_router = APIRouter(tags=['products'])


@api_router.post("/products/category", status_code=status.HTTP_201_CREATED)
async def create_category(category_in: schema.CategoryCreate, db_session: Session = Depends(db.get_db)) -> Any:
    new_category = await services.create_new_category(category=category_in, db_session=db_session)
    return new_category


@api_router.get("/products/category", response_model=List[schema.Category])
async def get_all_categories(db_session: Session = Depends(db.get_db)):
    return await services.get_all_categories(db_session)


@api_router.get('/products/category/{category_id}', response_model=schema.Category)
async def get_category_by_id(category_id: int, db_session: Session = Depends(db.get_db)):
    category = await services.get_category_by_id(category_id, db_session)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found!")
    return category


@api_router.delete("/products/category/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category_by_id(category_id: int, db_session: Session = Depends(db.get_db)):
    category = await services.get_category_by_id(category_id, db_session)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category Not Found!")
    return await services.delete_category_by_id(category_id, db_session)