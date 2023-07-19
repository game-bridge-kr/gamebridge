from dotenv import find_dotenv, load_dotenv
from os import environ

load_dotenv(find_dotenv('.env'))


def mongo_db_url() -> str:
    return environ.get('MONGO_DB_URL')

def mongo_db_database() -> str:
    return environ.get("MONGO_DB_DATABASE")

MONGO_DB_USER = environ.get('MONGO_DB_USER')
MONGO_DB_PASSWORD = environ.get('MONGO_DB_PASSWORD')

NAVER_CLIENT_ID = environ.get('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = environ.get('NAVER_CLIENT_SECRET')

VULTR_API_KEY = environ.get('VULTR_API_KEY')
