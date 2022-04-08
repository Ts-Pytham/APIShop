from pydantic import BaseModel, constr, validator, EmailStr

class UserBase(BaseModel):
    name: constr(min_length=2, max_length=50)
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: str
    pass

class UserInDBBase(UserBase):
    id: int
    password: str

    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    class Config:
        orm_mode = True
