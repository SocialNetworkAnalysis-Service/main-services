from src.db.repository import AbstractRepository
from src.essence.users.schemas import VerifCodeShemaAdd
from src.essence.verification_codes.models import (
    VerificationCodes as VerifCode,
)


class VerifCodesService:
    def __init__(self, codes_repo: AbstractRepository):
        self.codes_repo: AbstractRepository = codes_repo()

    async def add_code(self, code: VerifCodeShemaAdd):
        code_dict = code.model_dump()
        finded_code = await self.codes_repo.find_one(phone=code_dict["phone"])
        if finded_code:
            await self.codes_repo.update_by_id(
                finded_code.id, verification_code=code_dict["verification_code"]
            )
        else:
            code = await self.codes_repo.add_one(code_dict)
        return True

    async def check_code(self, phone_number: str, verify_code: str) -> VerifCode:
        code = await self.codes_repo.find_one(
            phone=phone_number, verification_code=verify_code
        )
        return code