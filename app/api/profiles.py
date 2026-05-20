from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.crud.profiles import create_profile, get_profiles
from app.schemas.profile import ProfileCreate, ProfileResponse

router = APIRouter(prefix="/profiles", tags=["Profiles"])


@router.post("/", response_model=ProfileResponse)
async def add_profile(profile: ProfileCreate, db: AsyncSession = Depends(get_db)):
    return await create_profile(db, profile)


@router.get("/", response_model=list[ProfileResponse])
async def read_profiles(db: AsyncSession = Depends(get_db)):
    return await get_profiles(db)