from typing import Optional
from dataclasses import dataclass
from pydantic import BaseModel
from .url import UrlComponents


@dataclass
class NidUrlComponents(UrlComponents):
    netloc: str = "nid.naver.com"


class LoginCallbackRequest(BaseModel):
    state: str
    code: Optional[str]
    error: Optional[str]
    error_description: Optional[str]


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int
    error: Optional[str]
    error_description: Optional[str]

