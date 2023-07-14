from fastapi import status, HTTPException
from ...model.user import User
from ...repository.mongo import database


def register(user: User):
    users = database.get_users()

    # https://www.mongodb.com/docs/manual/tutorial/query-embedded-documents/
    query_filter = { 'naver_user.id': user.naver_user.id }
    if users.count_documents(query_filter) > 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="user id already exists"
        )

    users.insert_one(user.model_dump())


def get_naver_user(user: User) -> bool:
    users = database.get_users()

    # https://www.mongodb.com/docs/manual/tutorial/query-embedded-documents/
    query_filter = { 'naver_user.id': user.naver_user.id }
    return users.count_documents(query_filter) > 0