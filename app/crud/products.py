from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product
from app.schemas.product import ProductCreate


async def create_product(db: AsyncSession, product: ProductCreate):
    new_product = Product(**product.model_dump())

    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)

    return new_product


async def get_products(db: AsyncSession):
    result = await db.execute(select(Product))
    return result.scalars().all()