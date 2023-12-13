from src.db.repository import SQLAlchemyRepository
from src.essence.verification_codes.models import VerificationCodes


class VerifCodesRepository(SQLAlchemyRepository):
    model = VerificationCodes