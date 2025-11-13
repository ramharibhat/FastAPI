from fastapi import APIRouter, status, Depends
from typing import List
from sqlalchemy.orm import Session
from .. import schema, database, oAuth2
from ..repository import blog

router = APIRouter( 
    prefix = "/blog",
    tags=["Blogs"])

get_db = database.get_db

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schema.CleanBlog] )
async def get_all_blogs(db : Session = Depends(get_db), 
                        current_user: schema.User = Depends(oAuth2.get_current_user)):
    return blog.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_blog(request: schema.Blog, db : Session = Depends(get_db), 
                      current_user: schema.User = Depends(oAuth2.get_current_user)):
    return blog.create(request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(id: int, db : Session = Depends(get_db),
                      current_user: schema.User = Depends(oAuth2.get_current_user)):
    return blog.destroy(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_blog(id: int, request: schema.Blog, db : Session = Depends(get_db),
                      current_user: schema.User = Depends(oAuth2.get_current_user)):
    return blog.update(id, db, request)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schema.CleanBlog)
async def get_blog_id( id: int, db: Session = Depends(get_db),
                      current_user: schema.User = Depends(oAuth2.get_current_user)):
    return blog.get_id(id, db)