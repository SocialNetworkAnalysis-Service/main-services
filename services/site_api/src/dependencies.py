import secrets

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from nats.js import JetStreamContext

from src.essence.users.repository import UsersRepository
from src.essence.users.service import UsersService
from src.essence.verification_codes.repository import VerifCodesRepository
from src.essence.verification_codes.service import VerifCodesService

security = HTTPBasic()


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "user")
    correct_password = secrets.compare_digest(credentials.password, "password")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


# Services
def users_service():
    return UsersService(UsersRepository)


def verif_codes_service():
    return VerifCodesService(VerifCodesRepository)


# Nats stub
class GetNatsJetStream:
    def __init__(self, js: JetStreamContext):
        self.js = js

    def __call__(self):
        return self.js


def nats_jetstream_stub():
    raise NotImplementedError
