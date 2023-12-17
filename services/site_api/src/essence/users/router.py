from typing import Annotated
from datetime import timedelta

from fastapi import APIRouter, Request, Form, Depends, HTTPException, status

from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from src.essence.users.schemas import (
    UserInAuth,
    UserInVeify,
    UserJWTResponse,
    UserSchemaAdd,
    VerifCodeShemaAdd,
)
from src.essence.users.service import UsersService
from src.essence.verification_codes.service import VerifCodesService
from src.dependencies import users_service, verif_codes_service
from src.security import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    REFRESH_TOKEN_EXPIRE_MINUTES,
    create_token,
    decode_token,
    oauth2_scheme,
)
from src.utils.sms_api import send_call_verify

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

templates = Jinja2Templates(directory="src/templates")

# define the registration route
@router.post("/enter_phone_number/")
async def auth_by_phone(
    phone_number: Annotated[str, Form()],
    request: Request,
    verif_codes_service: Annotated[VerifCodesService, Depends(
        verif_codes_service)]
):
    # send the verify call with number-code
    call_sent = await send_call_verify(phone_number)

    # write sms code in verification_codes table
    if call_sent:
        if await verif_codes_service.add_code(
            VerifCodeShemaAdd(phone=phone_number, verification_code=call_sent)
        ):
            return {"message": "verification code sent successfully"}
        
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="error sending sms-call",
        )


# define the verify_sms route
@router.post("/enter_sms_code/", response_model=UserJWTResponse)
async def verify_sms(
    sms_code: Annotated[str, Form()],
    phone_number: Annotated[str, Form()],
    request: Request,
    users_service: Annotated[UsersService, Depends(users_service)],
    verif_codes_service: Annotated[VerifCodesService, Depends(verif_codes_service)],
):
    print(sms_code, phone_number)
    if await verif_codes_service.check_code(
        phone_number=phone_number, verify_code=sms_code
    ):
        user = await users_service.find_user_by_phone(phone_number)
        if user is None:
            await users_service.create_user(
                user=UserSchemaAdd(phone=phone_number)
            )
        # нужно подумать над запрос об удалении кода верификации из БД, так как он уже не нужен будет после авторизации
        # return {'message': 'users was in db'}
        # Создаем access и refresh токены
        access_token = create_token(
            {"sub": phone_number},
            timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        )
        refresh_token = create_token(
            {"sub": phone_number},
            timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES),
        )
        return {"access_token": access_token, "refresh_token": refresh_token}
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="sms code or phone number is not valid",
    )
   # return templates.TemplateResponse("verify_sms.html", {"request": request, 'error_message': 'Неверный смс-код!'})


# # Функция для обновления access токена с помощью refresh токена
# def process_refresh_token(refresh_token: str):
#     try:
#         payload = decode_token(refresh_token)
#         if "sub" not in payload:
#             raise HTTPException(status_code=401, detail="Invalid refresh token")

#         # Создаем новый access токен
#         access_token = create_token(
#             {"sub": payload["sub"]}, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#         )
#         refresh_token = create_token(
#             {"sub": payload["sub"]}, timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
#         )
#         return {"access_token": access_token, "refresh_token": refresh_token}
#     except HTTPException:
#         raise
#     except Exception:
#         raise HTTPException(status_code=401, detail="Invalid refresh token")


# # Роут для обновления access токена с помощью refresh токена
# @router.post("/refresh_tokens", response_model=UserJWTResponse)
# def get_tokens(refresh_token: str = Depends(oauth2_scheme)):
#     return process_refresh_token(refresh_token)
