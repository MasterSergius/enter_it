from pydantic import BaseModel
from pydantic import Field
from datetime import datetime


class UserInfo(BaseModel):
    username: str
    # TODO: add email, age, etc.


class UserDBModel(BaseModel):
    id: int
    username: str
    password: str
    created_at: datetime

    class Config:
        from_attributes = True


class CreateUserRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=3, max_length=50)


class CreateUserResponse(BaseModel):
    message: str
