from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from .. import schema, database, oAuth2
from ..repository import user

router = APIRouter(
    prefix = "/user",
    tags=["Users"])

get_db = database.get_db

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.CleanUser)
async def create_user(request:schema.User, db: Session = Depends(get_db),
                      current_user: schema.User = Depends(oAuth2.get_current_user)):
    return user.create_user(request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schema.CleanUser)
async def get_user(id: int, db: Session = Depends(get_db),
                   current_user: schema.User = Depends(oAuth2.get_current_user)):
    return user.get_user_id(id, db)