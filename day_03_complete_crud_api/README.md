# Day 3 - Complete CRUD API using FastAPI + SQLModel + SQLite

## Objective

Build a complete CRUD (Create, Read, Update, Delete) API for Notes using:

* FastAPI
* SQLModel
* SQLite
* Swagger UI

---

# Project Flow

```text
Client
   ↓
Swagger UI
   ↓
FastAPI Route
   ↓
SQLModel
   ↓
SQLite Database
```

---

# Models

## Note

Actual database table.

```python
class Note(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    title: str
    description: str
    content: str
```

### Important

* table=True → create database table
* primary_key=True → unique identifier
* id generated automatically by database

---

## CreateNote

Request body model.

```python
class CreateNote(SQLModel):
    title: str
    description: str
    content: str
```

### Why separate model?

User sends:

```json
{
    "title": "React",
    "description": "Frontend",
    "content": "Hooks"
}
```

User should NOT send:

```json
{
    "id": 1
}
```

Database generates id automatically.

---

# Database Setup

```python
engine = create_engine(sqlite_url)
```

Engine is responsible for database connection.

---

# Session

```python
with Session(engine) as session:
```

Session is used to communicate with database.

Used for:

* Add data
* Read data
* Update data
* Delete data

---

# CREATE

## Route

```python
POST /notes
```

## Flow

```text
JSON
 ↓
CreateNote
 ↓
Note
 ↓
session.add()
 ↓
session.commit()
 ↓
Database
```

## Important Methods

### session.add()

Adds object to current session.

```python
session.add(db_note)
```

### session.commit()

Permanently saves changes.

```python
session.commit()
```

Without commit:

```text
RAM only
```

With commit:

```text
Database storage
```

### session.refresh()

Fetch latest data from database.

Useful for getting generated id.

```python
session.refresh(db_note)
```

---

# READ ALL

## Route

```python
GET /notes
```

## Query

```python
notes = session.exec(
    select(Note)
).all()
```

### Meaning

```text
Select all rows from Note table
```

### Output

```python
[
    Note1,
    Note2,
    Note3
]
```

---

# READ ONE

## Route

```python
GET /notes/{note_id}
```

## Query

```python
note = session.get(
    Note,
    note_id
)
```

### Meaning

```text
Find note by primary key
```

Example:

```python
session.get(Note, 2)
```

Returns:

```text
id = 2 note
```

---

# UPDATE

## Route

```python
PUT /notes/{note_id}
```

## Flow

```text
Fetch note
 ↓
Modify fields
 ↓
commit()
 ↓
Database updated
```

Example:

```python
db_note.title = note.title
db_note.description = note.description
db_note.content = note.content
```

Then:

```python
session.commit()
```

---

# DELETE

## Route

```python
DELETE /notes/{note_id}
```

## Flow

```text
Fetch note
 ↓
delete()
 ↓
commit()
```

Code:

```python
session.delete(note)
session.commit()
```

---

# Reading Data

## select()

```python
select(Note)
```

Equivalent SQL:

```sql
SELECT * FROM note
```

---

## where()

```python
select(Note).where(Note.id == 1)
```

Equivalent SQL:

```sql
SELECT * FROM note
WHERE id = 1
```

---

# .all() vs .first()

## .all()

Returns all matching rows.

```python
notes = session.exec(
    select(Note)
).all()
```

Output:

```python
[
    Note1,
    Note2,
    Note3
]
```

---

## .first()

Returns first matching row.

```python
note = session.exec(
    select(Note)
).first()
```

Output:

```python
Note1
```

---

# session.get() vs select().where()

## session.get()

Use when searching by primary key.

```python
session.get(Note, note_id)
```

---

## select().where()

Use when applying custom filters.

```python
select(Note).where(
    Note.title == "React"
)
```

---

# CRUD Summary

## Create

```python
POST /notes
```

Methods:

```python
add()
commit()
refresh()
```

---

## Read

```python
GET /notes
GET /notes/{id}
```

Methods:

```python
select()
get()
```

---

## Update

```python
PUT /notes/{id}
```

Methods:

```python
get()
commit()
```

---

## Delete

```python
DELETE /notes/{id}
```

Methods:

```python
get()
delete()
commit()
```

---

# Biggest Learning

```text
CreateNote
      ↓
Note
      ↓
Session
      ↓
Commit
      ↓
SQLite Database
```

This is the fundamental backend flow.
