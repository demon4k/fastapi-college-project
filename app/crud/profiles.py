from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.profile import Profile
from app.schemas.profile import ProfileCreate


async def create_profile(db: AsyncSession, profile: ProfileCreate):
    new_profile = Profile(**profile.model_dump())

    db.add(new_profile)
    await db.commit()
    await db.refresh(new_profile)

    return new_profile


async def get_profiles(db: AsyncSession):
    result = await db.execute(select(Profile))
    return result.scalars().all()