
import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_create_employee_as_admin():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        admin_login = await ac.post("/api/v1/login", json={
            "username": "admin_user",
            "password": "admin_pass"
        })
    admin_token = admin_login.json()["access_token"]

    employee_data = {
        "employee_id": 1,
        "name": "John Doe",
        "designation": "Software Engineer",
        "department": "IT",
        "joining_date": "2024-01-01"
    }
    
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await ac.post("/api/v1/employees", json=employee_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["employee_id"] == 1
    assert response.json()["name"] == "John Doe"

@pytest.mark.asyncio
async def test_create_employee_as_employee():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        employee_login = await ac.post("/api/v1/login", json={
            "username": "employee_user",
            "password": "employee_pass"
        })
    employee_token = employee_login.json()["access_token"]

    employee_data = {
        "employee_id": 2,
        "name": "Jane Doe",
        "designation": "Manager",
        "department": "Sales",
        "joining_date": "2024-02-01"
    }
    
    headers = {"Authorization": f"Bearer {employee_token}"}
    response = await ac.post("/api/v1/employees", json=employee_data, headers=headers)
    assert response.status_code == 403  
