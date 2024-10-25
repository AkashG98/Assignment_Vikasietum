
import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_create_salary_as_admin():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        admin_login = await ac.post("/api/v1/login", json={
            "username": "admin_user",
            "password": "admin_pass"
        })
    admin_token = admin_login.json()["access_token"]

    salary_data = {
        "employee_id": 1,  
        "base_salary": 5000.00,
        "bonuses": 1500.00
    }
    
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await ac.post("/api/v1/salaries", json=salary_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["message"] == "Salary processing initiated"

@pytest.mark.asyncio
async def test_create_salary_for_nonexistent_employee():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        admin_login = await ac.post("/api/v1/login", json={
            "username": "admin_user",
            "password": "admin_pass"
        })
    admin_token = admin_login.json()["access_token"]

    salary_data = {
        "employee_id": 999,  
        "base_salary": 5000.00,
        "bonuses": 1000.00
    }
    
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await ac.post("/api/v1/salaries", json=salary_data, headers=headers)
    assert response.status_code == 404
    assert response.json() == {"detail": "Employee not found"}
