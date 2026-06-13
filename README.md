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

---

## 🛠️ Next Steps
- Implement PUT and DELETE operations.
- Add robust error handling.
- Incorporate FastAPI's Dependency Injection.
- Implement Authentication & Authorization.
