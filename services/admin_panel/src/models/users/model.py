from src.db.database import Base
import sqlalchemy as sq


class Users(Base):
    __tablename__: str = 'users'

    id = sq.Column(sq.Integer, primary_key=True)
    phone = sq.Column(sq.String, unique=True, nullable=False)

    def __repr__(self):
        return self.phone