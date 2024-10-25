
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Employee(Base):
    __tablename__ = "employees"
    
    employee_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    designation = Column(String)
    department = Column(String)
    joining_date = Column(Date)
    monthly_salary = Column(Float, default=0.0)

class Salary(Base):
    __tablename__ = "salaries"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.employee_id"))
    base_salary = Column(Float)
    bonuses = Column(Float)
    employee = relationship("Employee")
