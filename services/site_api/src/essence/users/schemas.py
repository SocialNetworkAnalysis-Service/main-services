from pydantic import BaseModel, field_validator


class UserSchema(BaseModel):
    id: int
    phone: str

    class Config:
        from_attributes = True


class UserInAuth(BaseModel):
    phone_number: str

    # validator the phone_number of all classes
    @field_validator("phone_number")
    def validate_phone_number(cls, value):
        if not value.isnumeric() or len(value) != 11:
            raise ValueError("phone number must be 11 digits.")
        return value


class UserInVeify(BaseModel):
    phone_number: str
    sms_code: str

    # validator the phone_number of all classes
    @field_validator("phone_number")
    def validate_phone_number(cls, value):
        if not value.isnumeric() or len(value) != 11:
            raise ValueError("phone number must be 11 digits.")
        return value

    # validator the sms_code
    @field_validator("sms_code")
    def validate_sms_code(cls, value):
        if not value.isnumeric() or len(value) != 4:
            raise ValueError("sms code must be 4 digits.")
        return value


class UserSchemaAdd(BaseModel):
    phone: str


class VerifCodeShemaAdd(BaseModel):
    phone: str
    verification_code: str


class UserJWTResponse(BaseModel):
    access_token: str
    refresh_token: str