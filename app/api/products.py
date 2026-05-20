from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.crud.products import create_product, get_products
from app.schemas.product import ProductCreate, ProductResponse

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductResponse)
async def add_product(product: ProductCreate, db: AsyncSession = Depends(get_db)):
    return await create_product(db, product)


@router.get("/", response_model=list[ProductResponse])
async def read_products(db: AsyncSession = Depends(get_db)):
    return await get_products(db)