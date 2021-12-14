from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from pydantic.networks import EmailStr
from pydantic.schema import TypeModelOrEnum
from pydantic.types import conint

class PostBase(BaseModel):
  title: str
  content: str
  published: bool = True

class PostCreate(PostBase):
  pass



class UserCreate(BaseModel):
  email: EmailStr
  password: str

class UserOut(BaseModel):
  id: int
  email: EmailStr
  created_at: datetime

  class Config:
    orm_mode = True

class Post(PostBase):
  id: int
  created_at: datetime
  owner_id: int
  owner: UserOut
  
  class Config:
    orm_mode = True


class PostOut(BaseModel):
  """
  * TODO:
  * doesn't work when the variable is named 'post' but works with 'Post'
  """
  Post: Post
  votes: int

  class Config:
    orm_mode=True



class Token(BaseModel):
  access_token: str
  token_type: str

class TokenData(BaseModel):
  id: Optional[str] = None
  
class Vote(BaseModel):
  post_id: int
  dir: conint(le=1)