from fastapi import APIRouter, HTTPException

from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.crud.users import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user,
)

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[UserResponse])
async def read_users():
    return get_all_users()


@router.get("/{user_id}", response_model=UserResponse)
async def read_user(user_id: int):
    user = get_user_by_id(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.post("/", response_model=UserResponse)
async def add_user(user: UserCreate):
    return create_user(user)


@router.put("/{user_id}", response_model=UserResponse)
async def edit_user(user_id: int, user: UserUpdate):
    updated_user = update_user(user_id, user)

    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return updated_user


@router.delete("/{user_id}")
async def remove_user(user_id: int):
    deleted_user = delete_user(user_id)

    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted successfully", "user": deleted_user}