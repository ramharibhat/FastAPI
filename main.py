from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def index():
    return {"Root URL message": "Welcome to FastAPI sample project Home page"}

@app.get("/about")
async def about():
    return {"data": {"message": "More about this FastAPI app"}}

@app.get("/blog/{id}")
async def get_blog_id(id: int):
    # fetch a particular blog by id = id
    return {"data": id}


@app.get("/blog/{id}/comments")
async def blog_comments(id: int, limit: int = 10):
    # fetch a particular blog comments by id = id

    return {"data": {"1", "2"}}


@app.get("/blogs")
async def get_blogs(limit: int = 10, published: bool = False, sort: Optional[str] = None ):
    # get only limited blogs from db
    if published:
        return {"data": f"fetached {limit} published blogs from db"}
    else:
        return {"data": f"fetched {limit} un-published blogs from db"} 
    

class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]


@app.post("/blog")
async def create_blog(blog: Blog):
    return {"data": f"Created new blog with title {blog.title}" }

