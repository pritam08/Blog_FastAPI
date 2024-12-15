from typing import Annotated
from .database import Base
from sqlalchemy.orm import DeclarativeBase
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlalchemy import Column,Integer,String

from sqlalchemy import Column, Integer, String, ForeignKey
from blog.database import Base
from sqlalchemy.orm import relationship

class Blog_table(Base):
    __tablename__="blogs"
    id=Column(Integer,primary_key=True)
    title=Column(String)
    body=Column(String) 
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship("User_table", back_populates="blogs")



class User_table(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    email=Column(String) 
    password=Column(String) 

    blogs = relationship('Blog_table', back_populates="creator")



