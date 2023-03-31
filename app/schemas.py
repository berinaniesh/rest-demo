from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional
from pydantic.types import conint


# JWT
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


# Users
class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


# Post
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


# votes
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True
