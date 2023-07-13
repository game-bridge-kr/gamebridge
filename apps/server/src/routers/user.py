from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.responses import RedirectResponse
from ..services.user import naver_client, user_service
from ..model.naver import LoginCallbackRequest, NaverUserRegisterRequest
from ..model.user import User


router = APIRouter(tags=["user"])

@router.get("/api/naver/authenticate", response_class=RedirectResponse)
async def naver_login():
    return naver_client.get_authenticate_url()


@router.get("/api/naver/redirect")
async def naver_login_callback(request: LoginCallbackRequest = Depends()):
    if request.code is not None:
        token = naver_client.get_access_token(request.code)
        print(token.access_token)
        return naver_client.get_user(token.access_token)
    
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail= "failed to get code from naver login API"
    )


@router.post("/api/naver/register")
async def naver_register(request: NaverUserRegisterRequest = Body()):
    naver_user = naver_client.get_user(request.access_token)
    user = User(naver_user=naver_user)
    user_service.register(user)  
    return user
   

    
