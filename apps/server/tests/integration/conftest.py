from ...src.model.naver import NaverUser
from ...src.services.user import naver_client
from ...src.repository.mongo import database
import pytest


# should run integration test but mocking naver API since access token is sensitive data.
@pytest.fixture(autouse=True)
def mock_naver_client_get_user(monkeypatch):
    def mock_naver_user(token):
        return NaverUser(
            id="id-1",
            nickname="nickname",
            email="test@email.com",
            gender="M",
            birthyear=1995,
            age="20-29",
            mobile="12345"
        )

    monkeypatch.setattr(naver_client, "get_user", mock_naver_user)        

@pytest.fixture(autouse=True)
def set_test_context(monkeypatch):
    # before each test
    monkeypatch.setenv("MONGO_DB_DATABASE", "test_database")
    database.connect()

    yield
    
    # after each test
    database.get_users().drop()
    database.close()

