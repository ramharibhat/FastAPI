from sqlalchemy.orm import Session
from .. import models, schema
from fastapi import HTTPException, status


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schema.Blog, db: Session):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The blog ID {id} is not found")
    
    blog.delete(synchronize_session=False)
    db.commit()
    return {"description": f"Deleted successfully db record with id {id}"}

def update(id: int, db: Session, request: schema.Blog):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The blog ID {id} is not found")
    
    blog.update({"title": request.title, "body": request.body})
    db.commit()
    return {"detail": "Updated blog details with the request"}

def get_id(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"details": f"The particular blog id - {id} is not found!"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The particular blog id {id} is not found!")
    return blog
