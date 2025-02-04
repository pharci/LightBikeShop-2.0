from db.models.user import User
from sqlalchemy.future import select
from db.db import AsyncSessionLocal
import bcrypt

def create_password_hash(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

async def get_user_by_id(user_id: int) -> User:
    async with AsyncSessionLocal() as session:
        stmt = select(User).where(User.id == user_id)
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()
        return user

async def get_user_by_username(username: str) -> User:
    async with AsyncSessionLocal() as session:
        stmt = select(User).where(User.username == username)
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()
        return user
    
async def createsuperuser(username: str, password: str):
    async with AsyncSessionLocal() as session:
        async with session.begin():
            user = User(username=username, password_hash=create_password_hash(password), is_superuser=True)
            session.add(user)
        await session.commit()