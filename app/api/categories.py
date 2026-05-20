from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.crud.categories import create_category, get_categories
from app.schemas.category import CategoryCreate, CategoryResponse

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/", response_model=CategoryResponse)
async def add_category(category: CategoryCreate, db: AsyncSession = Depends(get_db)):
    return await create_category(db, category)


@router.get("/", response_model=list[CategoryResponse])
async def read_categories(db: AsyncSession = Depends(get_db)):
    return await get_categories(db)