from typing import Optional
from pydantic import BaseModel

class Blog(BaseModel):
    title:str
    body:str

class ShowBlog(Blog):
    class config:
        orm_mode=True

class User(BaseModel):
    name:str
    email:str
    password:str
