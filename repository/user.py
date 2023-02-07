from fastapi import HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session 
from ..hashing import Hash



def create(request : schemas.User, db : Session):
    new_user = models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def showUserById(id:int, db :Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user:
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"details" : f"user with the id {id} is not available"}
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"User with the id {id} is not available")

    return user
