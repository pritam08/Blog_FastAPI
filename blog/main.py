from fastapi import FastAPI,Depends,status,Response,HTTPException
from typing import Optional,List
from pydantic import BaseModel
from .schemas import *
from .model import *
from .database import *
from .hashing import *
from fastapi import *
import uvicorn
from passlib import crypto
from passlib.context import CryptContext


app=FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



Base.metadata.create_all(engine)


def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()

@app.post('/blogs',status_code=status.HTTP_201_CREATED,tags=["blogs"])
def create(request:Blog,db: Session=Depends(get_db)):

    new_blog=Blog_table(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



@app.get('/blogs',status_code=status.HTTP_200_OK,response_model=List[ShowBlog],tags=["blogs"])
def all(db: Session=Depends(get_db)):
    blogs=db.query(Blog_table).all()
    return blogs


@app.get('/blog/{id}',status_code=status.HTTP_200_OK,response_model=ShowBlog,tags=["blogs"])
def show(id:int,reponse:Response, db: Session=Depends(get_db)):
    blog=db.query(Blog_table).filter(Blog_table.id==id ).first()

  
    if not blog:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog for id {id} not available")
        # reponse.status_code=status.HTTP_404_NOT_FOUND
        # return {"detail":f"Blog for id {id} not available"}
    
    print(blog)
    return blog

@app.delete("blog/{id}",status_code=status.HTTP_204_NO_CONTENT,tags=["blogs"])

def delete(id:int,reponse:Response, db: Session=Depends(get_db)):
    # blog=db.query(Blog_table).filter(Blog_table.id== id )
    blog=db.query(Blog_table).filter(Blog_table.id== id)
    print(blog)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog for id {id} not available")
  
    blog.delete(synchronize_session=False)
     
    db.commit()
    return {"Done"}
    


@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=["blogs"])
def update(id:int,reponse:Blog,db: Session=Depends(get_db)):
    blog=db.query(Blog_table).filter(Blog_table.id== id)
    print(blog)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog for id {id} not available")
       
    blog.update({"title":reponse.title,"body":reponse.body})
    db.commit()
    return "Updated "


@app.post("/user",response_model=ShowUser,tags=["user"])
def create_user(request:User,db: Session=Depends(get_db)):
    hashedPassword=Hash.bcrypt(request.password)
    new_user=User_table(name=request.name,email=request.email,password=hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return request

@app.get("/user/{id}",response_model=ShowUser,tags=["user"])
def show_user(id:int,db: Session=Depends(get_db)):
    user = db.query(User_table).filter(User_table.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    
    return user










if __name__ =="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8885)#reload=True)