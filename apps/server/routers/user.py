from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from ..services.user import naver_service
from ..model.naver import LoginCallbackRequest


router = APIRouter(tags=["user"])

@router.get("/api/login/naver", response_class=RedirectResponse)
async def naver_login():
    return naver_service.get_autorhize_url()


@router.get("/api/login/naver/redirect")
async def naver_login_callback(request: LoginCallbackRequest = Depends()):
    if request.code is not None:
        token = naver_service.get_access_token(request.code)
        
