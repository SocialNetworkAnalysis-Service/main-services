from pydantic import BaseModel


class VerifCodeSchema(BaseModel):
    id: int
    phone: str
    verification_code: str

    class Config:
        from_attributes = True