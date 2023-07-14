from urllib.parse import urlencode
from ...model.naver import NidUrlComponents, OpenApiUrlComponents, Token, NaverUser, NaverUserResponse
from ...constants import NAVER_CLIENT_ID, NAVER_CLIENT_SECRET
import requests

STATE = '11' # random value


def get_authenticate_url() -> str:
    query_params = {
        'client_id': NAVER_CLIENT_ID,
        'redirect_uri': "http://127.0.0.1:8000/api/naver/redirect",
        'response_type': 'code',
        'state': STATE
    }

    return NidUrlComponents(
        path="/oauth2.0/authorize", 
        query=urlencode(query_params)
    ).to_url()


def get_access_token(code: str) -> Token:
    query_params = {
        'grant_type': 'authorization_code',
        'client_id': NAVER_CLIENT_ID,
        'client_secret': NAVER_CLIENT_SECRET,
        'code': code,
        'state': STATE
    }

    access_token_url = NidUrlComponents(
        path="/oauth2.0/token",
        query=urlencode(query_params)
    ).to_url()

    response = requests.get(access_token_url).json()
    return Token(**response)


def get_user(access_token: str) -> NaverUser:
    headers = {
        'Authorization': 'Bearer ' + access_token
    }

    url = OpenApiUrlComponents(
        path="/v1/nid/me"
    ).to_url()

    response = requests.get(url=url, headers=headers).json()
    return NaverUserResponse(**response).response

