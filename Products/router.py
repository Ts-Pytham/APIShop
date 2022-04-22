from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from typing import Any, List
from Core import security
from Database import db
from Users import schema as user_schema
from . import schema
from . import services
from . import validator
from Core import security
api_router = APIRouter(tags=['products/test'])


@api_router.post("/products/category", status_code=status.HTTP_201_CREATED)
async def create_category(category_in: schema.CategoryCreate, db_session: Session = Depends(db.get_db)
                        ,  current_user: user_schema.User = Depends(security.get_current_user)) -> Any:
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
async def delete_category_by_id(category_id: int, db_session: Session = Depends(db.get_db)
                                ,current_user: user_schema.User = Depends(security.get_current_user)):
    category = await services.get_category_by_id(category_id, db_session)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category Not Found!")
    return await services.delete_category_by_id(category_id, db_session)

@api_router.put("/products/category/{category_id}", response_model=schema.Category)
async def update_category(category_id: int, category: schema.CategoryUpdate, db_session: Session = Depends(db.get_db)
                        , current_user: user_schema.User = Depends(security.get_current_user)):
    category = await services.update_category(category_id, category,db_session)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category Not Found!")
    return category

@api_router.post('/products/', status_code=status.HTTP_201_CREATED)
async def create_product(product_in: schema.ProductCreate, db_session: Session = Depends(db.get_db)
                        , current_user: user_schema.User = Depends(security.get_current_user)):
    category = await validator.verify_category_exist(product_in.category_id, db_session)
    if not category:
        raise HTTPException(
            status_code=404,
            detail="You have provided invalid category id.",
        )

    product = await services.create_new_product(product=product_in, db_session=db_session)
    return product

@api_router.put('/products/{product_id}', response_model=schema.ProductUpdate)
async def update_product(product_id : int, product : schema.ProductUpdate, db_session: Session = Depends(db.get_db)
                        , current_user: user_schema.User = Depends(security.get_current_user)):
    new_product = await services.get_product_by_id(product_id, db_session)
    if not new_product:
        raise HTTPException(
            status_code=404,
            detail="The product is not found",
        )
    return await services.update_product(product_id, product, db_session)

@api_router.get('/products/', response_model=List[schema.Product])
async def get_all_products(db_session: Session = Depends(db.get_db)):
    return await services.get_all_products(db_session)