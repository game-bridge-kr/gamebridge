from ...model.user import User
from ...repository.mongo import database
from pymongo.results import InsertOneResult


def register(user: User) -> InsertOneResult:
    users = database.get_users()

    # https://www.mongodb.com/docs/manual/tutorial/query-embedded-documents/
    query_filter = { 'naver_user.id': user.naver_user.id }
    if users.count_documents(query_filter) > 0:
        raise ValueError("user id already exists")
    
    return users.insert_one(user.model_dump())
    