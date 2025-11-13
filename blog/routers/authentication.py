
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .. import schema, database, models, tokens
from ..hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(
    tags= ["Authentication"]
)
ACCESS_TOKEN_EXPIRE_MINUTES = 30

@router.post("/login", status_code=status.HTTP_202_ACCEPTED)
async def login(request: OAuth2PasswordRequestForm = Depends(), db : Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User Credentials {request.username} is invalid")
    
    if not Hash.verify(request.password, user.password): #type: ignore
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User password is in-correct: {request.password}")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = tokens.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
