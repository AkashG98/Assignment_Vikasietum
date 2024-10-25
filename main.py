
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routes import user, employee, salary

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Management API",
    description="API for managing employee data and salaries with JWT-based authentication",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, tags=["User Authentication"])
app.include_router(employee.router, tags=["Employee Management"])
app.include_router(salary.router, tags=["Salary Management"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Employee Management API"}
