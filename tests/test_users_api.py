import pytest


@pytest.mark.asyncio
async def test_create_user(client):
    response = await client.post(
        "/users/",
        json={
            "name": "Test User",
            "email": "test@example.com",
            "age": 18,
            "password": "12345678",
        },
    )

    assert response.status_code == 200
    data = response.json()

    assert data["name"] == "Test User"
    assert data["email"] == "test@example.com"
    assert data["age"] == 18


@pytest.mark.asyncio
async def test_get_users(client):
    await client.post(
        "/users/",
        json={
            "name": "Test User",
            "email": "test@example.com",
            "age": 18,
            "password": "12345678",
        },
    )

    response = await client.get("/users/")

    assert response.status_code == 200
    assert len(response.json()) == 1


@pytest.mark.asyncio
async def test_get_user_by_id(client):
    created = await client.post(
        "/users/",
        json={
            "name": "Test User",
            "email": "test@example.com",
            "age": 18,
            "password": "12345678",
        },
    )

    user_id = created.json()["id"]

    response = await client.get(f"/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["id"] == user_id


@pytest.mark.asyncio
async def test_update_user(client):
    created = await client.post(
        "/users/",
        json={
            "name": "Test User",
            "email": "test@example.com",
            "age": 18,
            "password": "12345678",
        },
    )

    user_id = created.json()["id"]

    response = await client.put(
        f"/users/{user_id}",
        json={
            "name": "Updated User",
            "email": "updated@example.com",
            "age": 20,
        },
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Updated User"


@pytest.mark.asyncio
async def test_delete_user(client):
    created = await client.post(
        "/users/",
        json={
            "name": "Test User",
            "email": "test@example.com",
            "age": 18,
            "password": "12345678",
        },
    )

    user_id = created.json()["id"]

    response = await client.delete(f"/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["message"] == "User deleted successfully"