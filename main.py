from itertools import product
from fastapi import FastAPI
from Core.config import settings
from Database import models
from Products import router as product_router
from Users import router as user_router
from Auth import router as auth_router

app = FastAPI(title="My application", version="0.1")


@app.get("/")
async def home() -> dict:
    return {'message': 'OK'}

app.include_router(product_router.api_router)
app.include_router(user_router.api_router)
app.include_router(auth_router.api_router)