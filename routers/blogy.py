from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from .. import schemas, database, oauth2
from .. repository import blog
from sqlalchemy.orm import Session 

router = APIRouter(
    prefix = "/blog",
    tags=['blogy']
)


@router.get('/',response_model = List[schemas.ShowBlog])
def get_blog(db : Session = Depends(database.get_db),current_user : schemas.User = Depends(oauth2.get_current_user)):
    
    return blog.get_all(db)


@router.get('/{id}', status_code = 200, response_model = schemas.ShowBlog)
def show_blog(id, db : Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.getBlogById(id,db)


@router.post('/', status_code = status.HTTP_201_CREATED)
def create(request: schemas.Blog, db : Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(db, request)


@router.put('/{id}' , status_code = status.HTTP_202_ACCEPTED)
def update(id, request : schemas.Blog, db : Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)



@router.delete('/{id}' , status_code = status.HTTP_204_NO_CONTENT)
def destroy(id, db : Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)
