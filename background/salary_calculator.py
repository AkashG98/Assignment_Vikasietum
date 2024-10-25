
from fastapi import BackgroundTasks
from sqlalchemy.orm import Session
from models import Salary, Employee

def calculate_salary(db: Session, employee_id: int, base_salary: float, bonuses: float):
    total_salary = base_salary + bonuses
    employee = db.query(Employee).filter(Employee.employee_id == employee_id).first()
    if employee:
        employee.monthly_salary = total_salary
        db.commit()
