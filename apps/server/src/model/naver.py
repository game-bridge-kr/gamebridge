from typing import Optional
from pydantic.dataclasses import dataclass
from pydantic import BaseModel, EmailStr, model_validator, Field
from enum import Enum
from .url import UrlComponents


@dataclass
class NidUrlComponents(UrlComponents):
    netloc: str = "nid.naver.com"


@dataclass
class OpenApiUrlComponents(UrlComponents):
    netloc: str = "openapi.naver.com"



class LoginCallbackRequest(BaseModel):
    state: str
    code: str
    error: Optional[str] = None
    error_description: Optional[str] = None

    @model_validator(mode="before")
    def verify_sucess(cls, values): 
        error = values.get("error")
        error_description = values.get("error_description")
        if error is not None:
            raise ValueError(f"failed to login with naver open API authentication, error_description={error_description}")

        return values


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int
    error: Optional[str] = None
    error_description: Optional[str] = None

    @model_validator(mode="before")
    def verify_success(cls, values):
        error = values.get("error")
        error_description = values.get("error_description")
        if error is not None:
            raise ValueError(f"failed to get access token from naver open API, error_description={error_description}")

        return values


class NaverUser(BaseModel):
    id: str
    nickname: str
    email: EmailStr
    gender: str
    birthyear: int
    age: str
    mobile: str


class NaverUserResponse(BaseModel):
    resultcode: str
    message: str
    response: NaverUser


class NaverUserRequest(BaseModel):
    access_token: str

