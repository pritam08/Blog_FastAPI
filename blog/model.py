from typing import Annotated
from database import Base
from sqlalchemy.orm import DeclarativeBase
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlalchemy import Column,Integer,String


class Blog_table(Base):
    __tablename__="blogs"
    id=Column(Integer,primary_key=True)
    title=Column(String)
    body=Column(String) 



class User_table(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    email=Column(String) 
    password=Column(String) 



class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_name: str