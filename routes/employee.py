
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Employee
from schemas import EmployeeCreate
from database import get_db
from auth.auth_bearer import JWTBearer

router = APIRouter()

@router.post("/api/v1/employees", dependencies=[Depends(JWTBearer())])
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee
