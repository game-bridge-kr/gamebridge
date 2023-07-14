from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.responses import RedirectResponse
from ..services.user import naver_client, user_service
from ..model.naver import LoginCallbackRequest, NaverUserRequest
from ..model.user import User


router = APIRouter(tags=["user"], prefix="/api/naver")

@router.get("/authenticate", response_class=RedirectResponse)
async def naver_login():
    return naver_client.get_authenticate_url()


@router.get("/token")
async def naver_login_callback(request: LoginCallbackRequest = Depends()):
    if request.code is not None:
        return naver_client.get_token(request.code)

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail= "failed to get code from naver login API"
    )


@router.get("/user")
async def naver_user(access_token: str):
    naver_user = naver_client.get_user(access_token)
    user = User(naver_user=naver_user)
    user_service.get_naver_user(user)  
    return user


@router.post("/register")
async def naver_register(request: NaverUserRequest = Body()):
    naver_user = naver_client.get_user(request.access_token)
    user = User(naver_user=naver_user)
    user_service.register(user)  
    return user
