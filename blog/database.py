from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String,create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.ext import declarative
from sqlalchemy.orm import sessionmaker

# /DATA_BASE_URL="sqlite://C://Users//Pritam//Desktop//fastAPI//blog_projec/t//blog//blog.db"

sqlite_file_name = "C://Users//Pritam//Desktop//fastAPI//blog_project//blog//blog.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


# engine = create_engine(DATA_BASE_URL, connect_args = {"check_same_thread": False})
# 
# Base=declarative()

class Base(DeclarativeBase):
    pass
# Base=DeclarativeBase()/

session=sessionmaker(bind=engine,autoflush=False)