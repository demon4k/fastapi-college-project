from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.order import Order
from app.schemas.order import OrderCreate


async def create_order(db: AsyncSession, order: OrderCreate):
    new_order = Order(**order.model_dump())

    db.add(new_order)
    await db.commit()
    await db.refresh(new_order)

    return new_order


async def get_orders(db: AsyncSession):
    result = await db.execute(select(Order))
    return result.scalars().all()