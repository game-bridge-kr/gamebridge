from fastapi.testclient import TestClient
from ...src.main import app


client = TestClient(app)


def test_hello():
    response = client.get("/")
    content = response.json()

    assert response.status_code == 200
    assert content['message'] == "Hello World"


def test_naver_authenticate():
    response = client.get("/api/naver/authenticate")

    # httpx stores the original response in history list
    assert response.history[0].status_code == 307


def test_naver_login_callback():
    response = client.get("/api/naver/token")

    assert response.status_code == 422


def test_naver_user():
    response = client.get("/api/naver/user", params={'access_token': 'token'})

    assert response.json()['naver_user']['id'] == 'id-1'


def test_naver_register():
    response = client.post("/api/naver/register", json={'access_token': "token"})

    assert response.json()['naver_user']['id'] == 'id-1'


def test_naver_register_twice():
    response1 = client.post("/api/naver/register", json={'access_token': "token"})
    response2 = client.post("/api/naver/register", json={'access_token': "token"})

    assert response1.json()['naver_user']['id'] == 'id-1'
    assert response2.status_code == 400
