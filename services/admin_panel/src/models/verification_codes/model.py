from src.db.database import Base
import sqlalchemy as sq
from src.db.database import create_session
from sqlalchemy import select


# create models with 2 fields: phone and sms code
class VerificationCodes(Base):
    __tablename__ = 'verification_codes'
    id = sq.Column(sq.Integer, primary_key=True)
    phone = sq.Column(sq.String, nullable=False)
    verification_code = sq.Column(sq.String, nullable=False)

    def __init__(self, phone, verification_code):
        self.phone = phone
        self.verification_code = verification_code

    # function of create code object
    @classmethod
    async def create_code(cls, phone: str, sms_code: str):
        verification_code = sms_code
        # check code in table
        async with create_session() as session:
            query = select(cls).where(cls.phone == phone)
            result = await session.execute(query)
            code = result.scalar_one_or_none()
            if code:  # if code exists in db
                code.verification_code = verification_code  # change code by new_code
                await session.commit()
            else:  # if code not exists in db
                code = cls(phone=phone, verification_code=verification_code)
                session.add(code)
                await session.commit()
        return code
