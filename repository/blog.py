from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import status, HTTPException


def get_all(db:Session):
    return db.query(models.Blog).all()
    

def getBlogById(id : int, db :Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not blog:
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"details" : f"Blog with the id {id} is not available"}
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"Blog with the id {id} is not available")

    return blog


def create(db : Session, request: schemas.Blog):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id : int,db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code = 404, detail = f"Blog with the id {id} does not exist")

    blog.delete(synchronize_session = False)
    db.commit()
    return {"Done"}

def update(id:int, request:schemas.Blog, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if blog is None:
        raise HTTPException( status_code = 404, detail = f"Blog with the id {id} does not exist")

    blog.title = request.title
    blog.body = request.body
    db.add(blog)
    #blog.update()
    db.commit()
    return 'updated'
    
