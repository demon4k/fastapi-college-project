from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.crud.orders import create_order, get_orders
from app.schemas.order import OrderCreate, OrderResponse

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=OrderResponse)
async def add_order(order: OrderCreate, db: AsyncSession = Depends(get_db)):
    return await create_order(db, order)


@router.get("/", response_model=list[OrderResponse])
async def read_orders(db: AsyncSession = Depends(get_db)):
    return await get_orders(db)