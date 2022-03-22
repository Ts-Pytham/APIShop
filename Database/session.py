from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Core.config import Settings

engine = create_engine(Settings.DATABASE_URI)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)


Base = declarative_base()