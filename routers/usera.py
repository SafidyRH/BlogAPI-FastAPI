from fastapi import APIRouter, Depends, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session 
from ..hashing import Hash
from .. repository import user


router = APIRouter(
    prefix="/User",
    tags = ['usera']
)
get_db = database.get_db


@router.post('/', response_model = schemas.ShowUser)
def create_user(request : schemas.User, db : Session = Depends(get_db)):
    return user.create(request,db)
    


@router.get('/{id}', response_model = schemas.ShowUser)
def show_user(id : int, db : Session = Depends(get_db)):
    return user.showUserById(id,db)