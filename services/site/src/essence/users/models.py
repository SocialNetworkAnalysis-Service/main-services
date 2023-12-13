from sqlalchemy.orm import Mapped, mapped_column

from src.db.database import Base
from src.essence.users.schemas import UserSchema


class Users(Base):
    __tablename__: str = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    phone: Mapped[str] = mapped_column(unique=True)

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            phone=self.phone,
        )