from urllib.parse import urlencode, urlunparse
from ...model.naver import NidUrlComponents, Token
from ...constants import NAVER_CLIENT_ID, NAVER_CLIENT_SECRET
import requests

STATE = '11' # random value


def get_autorhize_url() -> str:
    query_params = {
        'client_id': NAVER_CLIENT_ID,
        'redirect_uri': "http://127.0.0.1:8000/api/login/naver/redirect",
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
        path="oauth2.0/token",
        query=urlencode(query_params)
    ).to_url()

    response = requests.get(access_token_url).json()
    return Token(**response)

