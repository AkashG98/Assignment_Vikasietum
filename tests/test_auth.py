
import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_login_admin():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v1/login", json={
            "username": "admin_user",
            "password": "admin_pass"
        })
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

@pytest.mark.asyncio
async def test_login_employee():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v1/login", json={
            "username": "employee_user",
            "password": "employee_pass"
        })
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

@pytest.mark.asyncio
async def test_login_invalid_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v1/login", json={
            "username": "unknown_user",
            "password": "wrong_pass"
        })
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid username or password"}
