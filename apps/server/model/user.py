from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum


class Gender(Enum):
    F = "Female"
    M = "Male"
    U = "Unknown"


class NaverUser(BaseModel):
    id: str
    name: str
    nickname: str
    email: EmailStr
    gender: Gender
    birthyear: int
    age: str
    mobile: str