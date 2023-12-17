from src.db.repository import AbstractRepository
from src.essence.users.models import Users as User
from src.essence.users.schemas import UserSchemaAdd


class UsersService:
    def __init__(self, users_repo: AbstractRepository):
        self.users_repo: AbstractRepository = users_repo()

    async def create_user(self, user: UserSchemaAdd):
        user_dict = user.model_dump()
        user_id = await self.users_repo.add_one(user_dict)
        return user_id

    async def find_user_by_phone(self, phone_number: str) -> User:
        user = await self.users_repo.find_one(phone=phone_number)
        return user