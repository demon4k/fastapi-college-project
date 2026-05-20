from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.category import Category
from app.schemas.category import CategoryCreate


async def create_category(db: AsyncSession, category: CategoryCreate):
    new_category = Category(**category.model_dump())

    db.add(new_category)
    await db.commit()
    await db.refresh(new_category)

    return new_category


async def get_categories(db: AsyncSession):
    result = await db.execute(select(Category))
    return result.scalars().all()