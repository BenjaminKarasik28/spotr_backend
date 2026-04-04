from typing import Optional
from sqlmodel import SQLModel
from pydantic import EmailStr

class SpotrUserBase(SQLModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = None

    email: EmailStr

    gym: Optional[str] = None

    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None

    gender: Optional[str] = None
    age: Optional[int] = None

class SpotrUserCreate(SpotrUserBase):
    pass


class SpotrUserUpdate(SQLModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    gym: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    gender: Optional[str] = None
    age: Optional[int] = None


class SpotrUserRead(SpotrUserBase):
    id: int