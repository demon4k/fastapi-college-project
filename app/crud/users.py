from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

from app.core.security import hash_password


async def get_all_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()


async def get_user_by_id(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()


async def create_user(db: AsyncSession, user: UserCreate):
    new_user = User(
        name=user.name,
        email=user.email,
        age=user.age,
        hashed_password=hash_password(user.password),
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user


async def update_user(db: AsyncSession, user_id: int, user: UserUpdate):
    db_user = await get_user_by_id(db, user_id)

    if db_user is None:
        return None

    db_user.name = user.name
    db_user.email = user.email
    db_user.age = user.age

    await db.commit()
    await db.refresh(db_user)

    return db_user


async def delete_user(db: AsyncSession, user_id: int):
    db_user = await get_user_by_id(db, user_id)

    if db_user is None:
        return None

    await db.delete(db_user)
    await db.commit()

    return db_user