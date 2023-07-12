from dotenv import find_dotenv, dotenv_values

_env_values = dotenv_values(find_dotenv())

MONGO_DB_URL = _env_values['MONGO_DB_URL']
MONGO_DB_USER = _env_values['MONGO_DB_USER']
MONGO_DB_PASSWORD = _env_values['MONGO_DB_PASSWORD']

NAVER_CLIENT_ID = _env_values['NAVER_CLIENT_ID']
NAVER_CLIENT_SECRET = _env_values['NAVER_CLIENT_SECRET']