# Day 05 - Response Models and Dependency Injection

## Objective

Learn:

* Response Models
* Dependency Injection using Depends()
* Cleaner and reusable database session management

---

# Response Models

## Problem

Previously:

```python
@app.get("/notes")
def get_notes():
```

FastAPI did not know what type of response would be returned.

---

## Solution

```python
@app.get(
    "/notes",
    response_model=list[Note]
)
```

Now FastAPI knows that this endpoint returns a list of Note objects.

---

# GET All Notes

```python
@app.get(
    "/notes",
    response_model=list[Note]
)
def get_notes(
    session: Session = Depends(get_session)
):
    notes = session.exec(
        select(Note)
    ).all()

    return notes
```

### Response

```json
[
    {
        "id": 1,
        "title": "React",
        "description": "Frontend",
        "content": "Hooks"
    }
]
```

---

# GET Single Note

```python
@app.get(
    "/notes/{note_id}",
    response_model=Note
)
```

### Why?

Because only one Note object is returned.

---

# Benefits of Response Models

## 1. Response Validation

FastAPI checks whether the returned data matches the expected schema.

Example:

Expected:

```python
response_model=list[Note]
```

Returned:

```python
{
    "hello": "world"
}
```

FastAPI raises a validation error.

---

## 2. Better Swagger Documentation

Swagger automatically displays:

```json
{
    "id": 1,
    "title": "React",
    "description": "Frontend",
    "content": "Hooks"
}
```

This improves API documentation.

---

# Dependency Injection

## Problem

Session creation code was repeated in every route.

Example:

```python
with Session(engine) as session:
```

Repeated in:

* POST
* GET
* GET ONE
* PUT
* DELETE

---

# Solution

Create a reusable dependency.

```python
def get_session():
    with Session(engine) as session:
        yield session
```

---

# Using Depends()

Instead of:

```python
with Session(engine) as session:
```

Use:

```python
session: Session = Depends(get_session)
```

Example:

```python
@app.get("/notes")
def get_notes(
    session: Session = Depends(get_session)
):
```

---

# Internal Flow

```text
Request
   ↓
Depends(get_session)
   ↓
Create Session
   ↓
Pass Session To Route
   ↓
Execute Route
   ↓
Close Session
```

---

# Benefits of Depends()

## 1. Less Code Repetition

Before:

```python
with Session(engine) as session:
```

Written in every route.

After:

```python
Depends(get_session)
```

Reusable everywhere.

---

## 2. Cleaner Code

Routes become easier to read.

---

## 3. Centralized Session Management

If session logic changes:

Only update:

```python
get_session()
```

No need to modify every route.

---

# Key Learning

## Response Model

```python
response_model=Note
response_model=list[Note]
```

Used for:

* Response Validation
* Better Swagger Documentation

---

## Dependency Injection

```python
Depends(get_session)
```

Used for:

* Reusability
* Cleaner Code
* Session Management

---

# Interview Questions

### Why use Response Models?

To validate API responses and improve Swagger documentation.

---

### Why use Depends(get_session)?

To avoid repeating session creation code and let FastAPI manage database sessions automatically.

---

# Summary

```text
Response Models
↓
Response Validation
↓
Better API Documentation

Depends()
↓
Dependency Injection
↓
Reusable Session Management
↓
Cleaner FastAPI Code
```
