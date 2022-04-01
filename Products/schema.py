from pydantic import BaseModel, constr


# Shared properties
class CategoryBase(BaseModel):
    name: constr(min_length=2, max_length=50)


# Properties to receive on Category creation
class CategoryCreate(CategoryBase):
    pass


# Properties to receive on Category update
class CategoryUpdate(CategoryBase):
    pass


# Properties shared by models stored in DB
class CategoryInDBBase(CategoryBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Category(CategoryInDBBase):
    pass


# Properties to stored in DB
class CategoryInDB(CategoryInDBBase):
    pass