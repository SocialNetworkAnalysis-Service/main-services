from sqlalchemy.orm import Mapped, mapped_column

from src.db.database import Base
from src.essence.verification_codes.schemas import VerifCodeSchema


# create models with 2 fields: phone and sms code
class VerificationCodes(Base):
    __tablename__ = "verification_codes"

    id: Mapped[int] = mapped_column(primary_key=True)
    phone: Mapped[str] = mapped_column(nullable=False)
    verification_code: Mapped[str] = mapped_column(nullable=False)

    def to_read_model(self) -> VerifCodeSchema:
        return VerifCodeSchema(
            id=self.id, phone=self.phone, verification_code=self.verification_code
        )