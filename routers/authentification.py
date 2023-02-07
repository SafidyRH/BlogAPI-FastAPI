from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, database, models, JWTtoken
from sqlalchemy.orm import Session 
from ..hashing import Hash 
from datetime import timedelta



router = APIRouter(
    tags = ["Authentification"]
)
#get_bd = database.get_db()

ACCESS_TOKEN_EXPIRE_MINUTES = 30


@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(database.get_db)):
    
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code = 404, detail = f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code = 404, detail = f"Incorrect Password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = JWTtoken.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
    return user

