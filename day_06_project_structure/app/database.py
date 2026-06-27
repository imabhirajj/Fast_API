import os
from sqlmodel import create_engine, Session

# Define the database file name
sqlite_file_name = "notes.db"

# Get the base directory (day_06_project_structure) to place notes.db there
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
database_path = os.path.join(base_dir, sqlite_file_name)

# Create the SQLite URL
sqlite_url = f"sqlite:///{database_path}"

# Create the engine with connect_args for SQLite single-threaded checks bypass
engine = create_engine(
    sqlite_url,
    connect_args={"check_same_thread": False}
)


# Dependency function to provide a database session
def get_session():
    with Session(engine) as session:
        yield session
