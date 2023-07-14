from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from .naver import NaverUser


class User(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()))
    naver_user: NaverUser
