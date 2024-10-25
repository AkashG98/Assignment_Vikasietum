
from pydantic import BaseModel
from datetime import date
from typing import Optional

class EmployeeCreate(BaseModel):
    employee_id: int
    name: str
    designation: str
    department: str
    joining_date: date

class EmployeeResponse(BaseModel):
    employee_id: int
    name: str
    designation: str
    department: str
    joining_date: date
    monthly_salary: Optional[float] = 0.0

    class Config:
        orm_mode = True

class SalaryCreate(BaseModel):
    employee_id: int
    base_salary: float
    bonuses: float

class SalaryResponse(BaseModel):
    employee_id: int
    base_salary: float
    bonuses: float

    class Config:
        orm_mode = True
