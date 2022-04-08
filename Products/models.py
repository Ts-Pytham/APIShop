from itertools import product
from sqlalchemy import Column, Integer, Text, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from Database.session import Base

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

    product = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    quantity = Column(Integer)
    description = Column(Text)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey('category.id', ondelete="CASCADE"), )
    category = relationship("Category", back_populates="product")
