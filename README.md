# Fast_API

My FastAPI learning journey.

This repository tracks my daily learning progress as I build API projects using FastAPI, SQLModel, and SQLite.

---

## 📅 Learning Log

### [Day 1 - SQLModel and SQLite Basics](./day_01_sqlmodel_sqlite/README.md)
- **Topics**: FastAPI Setup, SQLModel configuration, SQLite setup, Session management, POST & GET routes.
- **Built**: A notes API connected to a SQLite database (`note.db`) with permanent note creation and list retrieval.

### [Day 2 - Database Persistence and Read Operations](./day_02_database_persistence/README.md)
- **Topics**: Models separation (`Note` and `CreateNote`), database persistence differences (RAM vs SQLite storage using commit), SQLModel filter operations (`select`, `where`, `first`, `all`).
- **Built**: Extended the notes API with detailed persistence logic and a route to fetch a single note by ID (`GET /notes/{note_id}`).

### [Day 3 - Complete CRUD API](./day_03_complete_crud_api/README.md)
- **Topics**: Complete CRUD operations (POST, GET, PUT, DELETE), SQLModel interaction (session `delete`, `commit`, `refresh`), API project architecture.
- **Built**: A full CRUD API for managing notes, supporting creating, listing, retrieving by ID, updating, and deleting notes, fully testable via Swagger UI.

### [Day 4 - HTTPException and Error Handling](./day_04_http_exception_and_error_handling/README.md)
- **Topics**: HTTPExceptions, Error Handling, API error responses.
- **Built**: Integrated HTTPException handling to return 404 responses for missing resources during read, update, and delete operations.

### [Day 5 - Response Models and Dependency Injection](./day_05_Response_Models_And_Dependency_Injection/ReadMe.md)
- **Topics**: Response Models, Dependency Injection (`Depends`), cleaner database session management.
- **Built**: Refactored the notes API to use structured response models and custom database session dependencies.

### [Day 7 - Path Parameters & Query Parameters](./day_06_project_structure/README.md)
- **Topics**: Path parameters (syntax, typing, Path validation), query parameters (syntax, default values, Query validation), differences, real-world use cases, best practices.
- **Built**: Documented comprehensive guides on path and query parameters with practice exercises.

---

## 🛠️ Next Steps
- Implement Authentication & Authorization.


