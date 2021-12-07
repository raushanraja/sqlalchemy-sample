from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, UUID4


class UserBase(BaseModel):
    id: Optional[UUID4] = None
    username: Optional[str] = None
    fullname: Optional[str] = None
    email: Optional[EmailStr] = None
    hashed_password: Optional[str] = None
    is_active: Optional[bool] = False
    created_at: Optional[datetime] = None


class Create(UserBase):
    username: str
    email: EmailStr
    password: str


class CreatePasswordHash(UserBase):
    username: str
    email: EmailStr
    hashed_password: str


class Update(UserBase):
    password: Optional[str] = None


class DBBase(UserBase):
    id: UUID4

    class Config:
        orm_mode = True


class User(DBBase):
    pass


class DB(DBBase):
    hashed_password: str
