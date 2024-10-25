
from fastapi import APIRouter, HTTPException, Depends
from auth.token_handler import create_access_token
from pydantic import BaseModel
from typing import Optional
from datetime import timedelta

router = APIRouter()

users_db = {
    "admin_user": {
        "username": "admin_user",
        "password": "admin_pass",
        "role": "admin"
    },
    "employee_user": {
        "username": "employee_user",
        "password": "employee_pass",
        "role": "employee"
    }
}

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/api/v1/login")
def login(user: UserLogin):
    user_data = users_db.get(user.username)
    if not user_data or user_data["password"] != user.password:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.username, "role": user_data["role"]}, 
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
