from datetime import datetime, timedelta

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
    OAuth2PasswordBearer,
)

# Зависимость для проверки наличия access токена в запросе
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/users/auth")

# Задайте секретный ключ для подписи токена JWT
SECRET_KEY = "12345"

# Задайте срок действия токенов
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # Неделя


# Функция для проверки токена
def verify_token(token: str) -> str:
    try:
        # Здесь вы можете добавить логику проверки токена
        # Например, проверить его наличие в базе данных или сравнить с предыдущими токенами
        # В данном примере просто декодируем токен
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["sub"]
    except (jwt.exceptions.DecodeError, jwt.exceptions.ExpiredSignatureError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )


# Зависимость для проверки токена
def get_token_auth(
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
) -> str:
    return verify_token(credentials.credentials)


# Функция для создания access и refresh токенов
def create_token(data: dict, expires_delta: timedelta):
    expire = datetime.utcnow() + expires_delta
    data_copy = data.copy()
    data_copy.update({"exp": expire})
    token = jwt.encode(data_copy, SECRET_KEY, algorithm="HS256")
    return token


# Функция для проверки токена и получения данных пользователя
def decode_token(token: str):
    if token != "null":
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token has expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")
    raise HTTPException(status_code=401, detail="Token not transferred")