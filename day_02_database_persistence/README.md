# Day 2 - Database Persistence and Read Operations

## Topics Learned

### Models

#### Note
Database table model.
Fields:
- `id`
- `title`
- `description`
- `content`

#### CreateNote
Request body model. Used for validating incoming data before storing it in the database.

---

### Database Persistence

Learned the difference between:
```python
return note
```
and:
```python
session.add(note)
session.commit()
```

Without commit:
- Data stays in memory (RAM)
- Lost after server restart

With commit:
- Data stored permanently in SQLite
- Available after restarting the server

---

### Reading Data from Database

#### Get All Notes
```http
GET /notes
```
Concept:
```python
session.exec(select(Note)).all()
```
Returns all records from the Note table.

#### Get Single Note
```http
GET /notes/{note_id}
```
Concept:
```python
select(Note).where(Note.id == note_id)
```
Returns a specific note by `id`.

---

### Important Concepts

#### `select()`
Used to read data from database.
SQL equivalent:
```sql
SELECT * FROM note;
```

#### `where()`
Used to filter records.
SQL equivalent:
```sql
WHERE id = ?;
```

#### `all()`
Returns all matching records.
Output:
```python
[Note1, Note2, Note3]
```

#### `first()`
Returns only the first matching record.
Output:
```python
Note1
```

---

### Key Learning

Data saved using `session.add()` and `session.commit()` remains available even after `Ctrl + C` and server restart.

---

## Next Steps

- Complete GET `/notes/{id}`
- PUT `/notes/{id}`
- DELETE `/notes/{id}`
- Error handling
- Dependency Injection
- Authentication
