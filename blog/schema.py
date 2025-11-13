from pydantic import BaseModel
from typing import List, Optional

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        from_attributes = True

class User(BaseModel):
    name: str
    email: str
    password: str


class CleanUser(BaseModel):
    name: str
    email: str
    
    blogs : List[Blog] = []

    class Config():
        from_attributes = True


class CleanBlog(Blog):
    title: str
    body : str

    creator: CleanUser


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
