from src.db.repository import SQLAlchemyRepository
from src.essence.users.models import Users


class UsersRepository(SQLAlchemyRepository):
    model = Users