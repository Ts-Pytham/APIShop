from typing import List
from unicodedata import name
from fastapi import HTTPException
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

async def update_category(category_id: int, category: schema.CategoryUpdate, db_session : Session):
    categoryc = models.Category(**category.dict())
    categoryc.id = category_id
    db_session.query(models.Category).filter(models.Category.id == category_id).update(
        {
            models.Category.name : categoryc.name 
        }, synchronize_session=False)
    db_session.commit()
    return categoryc

async def create_new_product(product: schema.ProductCreate, db_session: Session) -> models.Product:
    new_product = models.Product(**product.dict())

    db_session.add(new_product)
    db_session.commit()
    db_session.refresh(new_product)
    return new_product

async def get_product_by_id(product_id: int, db_session: Session) -> models.Product:
    product_info = db_session.query(models.Product).get(product_id)
    return product_info

async def update_product(product_id: int, product: schema.ProductUpdate, db_session: Session) -> schema.ProductUpdate:
    productc = models.Product(**product.dict())
    db_session.query(models.Product).filter(models.Product.id == product_id).update(
        {
            models.Product.id : product_id,
            models.Product.name : productc.name, 
            models.Product.description : productc.description,
            models.Product.quantity : productc.quantity,
            models.Product.price : productc.price,
            models.Product.category_id : productc.category_id, 
        
        }, synchronize_session=False)
    db_session.commit()
    return product


async def get_all_products(db_session: Session) -> List[models.Product]:
    products = db_session.query(models.Product).all()
    return products