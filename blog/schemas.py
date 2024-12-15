from typing import Optional
from pydantic import BaseModel

class Blog(BaseModel):
    title:str
    body:str
    class config:
        orm_mode=True



class User(BaseModel): 
    name:str
    email:str
    password:str
class ShowUser(BaseModel):
    name:str
    email:str
    blogs: list[Blog] =[]
    class config:
        orm_mode=True


class ShowBlog(Blog):

    title:str
    body:str
    creator:ShowUser
    class config:
        orm_mode=True
   