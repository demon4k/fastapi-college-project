import pytest

from app.crud.users import (
    create_user,
    delete_user,
    get_all_users,
    get_user_by_id,
    update_user,
)
from app.schemas.user import UserCreate, UserUpdate


@pytest.mark.asyncio
async def test_crud_create_user(prepare_database):
    from tests.conftest import TestingSessionLocal

    async with TestingSessionLocal() as db:
        user = UserCreate(
            name="CRUD User",
            email="crud@example.com",
            age=18,
            password="12345678",
        )

        created_user = await create_user(db, user)

        assert created_user.id is not None
        assert created_user.name == "CRUD User"


@pytest.mark.asyncio
async def test_crud_get_all_users(prepare_database):
    from tests.conftest import TestingSessionLocal

    async with TestingSessionLocal() as db:
        user = UserCreate(
            name="CRUD User",
            email="crud@example.com",
            age=18,
            password="12345678",
        )

        await create_user(db, user)

        users = await get_all_users(db)

        assert len(users) == 1


@pytest.mark.asyncio
async def test_crud_get_user_by_id(prepare_database):
    from tests.conftest import TestingSessionLocal

    async with TestingSessionLocal() as db:
        user = UserCreate(
            name="CRUD User",
            email="crud@example.com",
            age=18,
            password="12345678",
        )

        created_user = await create_user(db, user)

        found_user = await get_user_by_id(db, created_user.id)

        assert found_user is not None
        assert found_user.email == "crud@example.com"


@pytest.mark.asyncio
async def test_crud_update_user(prepare_database):
    from tests.conftest import TestingSessionLocal

    async with TestingSessionLocal() as db:
        user = UserCreate(
            name="CRUD User",
            email="crud@example.com",
            age=18,
            password="12345678",
        )

        created_user = await create_user(db, user)

        update_data = UserUpdate(
            name="Updated CRUD User",
            email="updated_crud@example.com",
            age=20,
        )

        updated_user = await update_user(db, created_user.id, update_data)

        assert updated_user.name == "Updated CRUD User"
        assert updated_user.age == 20


@pytest.mark.asyncio
async def test_crud_delete_user(prepare_database):
    from tests.conftest import TestingSessionLocal

    async with TestingSessionLocal() as db:
        user = UserCreate(
            name="CRUD User",
            email="crud@example.com",
            age=18,
            password="12345678",
        )

        created_user = await create_user(db, user)

        deleted_user = await delete_user(db, created_user.id)

        assert deleted_user.id == created_user.id

        found_user = await get_user_by_id(db, created_user.id)

        assert found_user is None