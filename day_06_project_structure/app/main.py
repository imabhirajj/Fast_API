from fastapi import FastAPI
from sqlmodel import SQLModel
from app.database import engine
from app.routes.notes import router as notes_router

# Initialize the FastAPI app
app = FastAPI(
    title="Day 06 Notes API",
    description="A refactored, modular CRUD API for Notes.",
    version="1.0.0"
)


# Create tables on database start
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


create_db_and_tables()

# Include the router in the main FastAPI application
app.include_router(notes_router)


# Root path endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to Day 06 Notes CRUD API! Visit /docs for documentation."
    }
