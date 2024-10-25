
from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from models import Salary, Employee
from schemas import SalaryCreate
from database import get_db
from background.salary_calculator import calculate_salary
from auth.auth_bearer import JWTBearer

router = APIRouter()

@router.post("/api/v1/salaries", dependencies=[Depends(JWTBearer())])
def create_salary(
    salary: SalaryCreate, 
    background_tasks: BackgroundTasks, 
    db: Session = Depends(get_db)
):
    employee = db.query(Employee).filter(Employee.employee_id == salary.employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    db_salary = Salary(
        employee_id=salary.employee_id,
        base_salary=salary.base_salary,
        bonuses=salary.bonuses
    )
    db.add(db_salary)
    db.commit()
    db.refresh(db_salary)

    background_tasks.add_task(
        calculate_salary, db=db, 
        employee_id=salary.employee_id, 
        base_salary=salary.base_salary, 
        bonuses=salary.bonuses
    )

    return {"message": "Salary processing initiated", "salary_id": db_salary.id}
