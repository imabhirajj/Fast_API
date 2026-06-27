# Day 07 - Path Parameters & Query Parameters

## Topics Covered
* Path Parameters
* Query Parameters
* Difference Between Path & Query Parameters
* Multiple Query Parameters
* Optional Query Parameters
* Query Validation
* Pagination Basics (`limit` & `skip`)
* Best Practices
* Interview Questions

---

# 1. Path Parameters

## Definition

Path Parameters are dynamic values placed inside the URL path to identify a specific resource.

### Syntax

```python
@router.get("/notes/{note_id}")
def get_note(note_id: int):
    ...
```

### Example

```
GET /notes/5
```

Returns the note whose ID is `5`.

---

# 2. Query Parameters

## Definition

Query Parameters are optional key-value pairs added after `?` in the URL. They are used to filter, search, sort, or paginate data.

### Syntax

```python
@router.get("/notes")
def get_notes(limit: int = 10):
    ...
```

### Example

```
GET /notes?limit=5
```

Returns the first 5 notes.

---

# 3. Difference

| Path Parameter                 | Query Parameter                  |
| ------------------------------ | -------------------------------- |
| Identifies a specific resource | Modifies or filters the response |
| Required                       | Usually optional                 |
| Part of URL path               | Comes after `?`                  |
| Example: `/notes/5`            | Example: `/notes?limit=5`        |

---

# 4. Multiple Query Parameters

```python
@router.get("/notes")
def get_notes(
    limit: int = 10,
    skip: int = 0
):
    ...
```

Example:

```
GET /notes?limit=10&skip=20
```

Meaning:

* Skip first 20 records
* Return next 10 records

---

# 5. Common Use Cases

## Path Parameters

* Get User by ID
* Get Product by ID
* Get Note by ID

Examples:

```
/users/10
/products/5
/notes/15
```

---

## Query Parameters

Filtering

```
/products?category=Shoes
```

Searching

```
/notes?search=python
```

Sorting

```
/products?sort=price
```

Pagination

```
/notes?limit=10&skip=20
```

---

# 6. Best Practices

* Use Path Parameters for resource identification.
* Use Query Parameters for filtering and pagination.
* Keep parameter names meaningful.
* Validate query parameters whenever required.
* Use pagination for large datasets.

---

# 7. Common Mistakes

❌ Using query parameters to identify a resource

```
/notes?id=5
```

✔ Better

```
/notes/5
```

---

❌ Forgetting default values

```python
limit: int
```

✔ Better

```python
limit: int = 10
```

---

# 8. Interview Ready Definitions

### Path Parameter

A Path Parameter identifies a specific resource and forms part of the URL path.

### Query Parameter

A Query Parameter modifies or filters the response without changing the endpoint.

---

# 9. Interview Questions

### 1. What are Path Parameters?
Path parameters are dynamic segments embedded directly inside the URL path structure used to locate a specific resource. In FastAPI, they are defined inside curly braces `{}` in the route decorator and received as function arguments.

**Example:**
```python
# URL: /notes/42
@app.get("/notes/{note_id}")
def read_note(note_id: int):
    return {"message": f"Fetching note with ID {note_id}"}
```

---

### 2. What are Query Parameters?
Query parameters are optional key-value pairs appended after the `?` in the URL (separated by `&`). They are used to filter, sort, or modify the response. In FastAPI, any function parameter not defined in the route decorator path is automatically treated as a query parameter.

**Example:**
```python
# URL: /notes?search=fastapi
@app.get("/notes")
def get_notes(search: str):
    return {"search_query": search}
```

---

### 3. What is the difference between them?
* **Path Parameters** are part of the URL path structure (e.g., `/notes/5`), are required to match the endpoint, and are used to **identify** a specific resource.
* **Query Parameters** are appended after the `?` (e.g., `/notes?limit=10`), do not affect route matching, are optional by default, and are used to **filter, search, sort, or paginate** results.

---

### 4. When should Path Parameters be used?
Use path parameters when you need to identify a **specific resource** or a **hierarchical relationship** between resources in your database.

**Example:**
* Fetching a single user: `GET /users/{user_id}`
* Fetching a specific comment on a specific post: `GET /posts/{post_id}/comments/{comment_id}`

---

### 5. When should Query Parameters be used?
Use query parameters when retrieving a list of resources and you want to **filter, sort, search, or paginate** the data without changing the REST endpoint path.

**Example:**
* Filter by status: `GET /orders?status=shipped`
* Sort by price: `GET /products?sort=price_low_high`
* Search by keyword: `GET /articles?q=python`

---

### 6. What is pagination?
Pagination is the practice of splitting a large database result set into smaller, manageable chunks (pages) when returning data to the client. This improves API response speed, reduces server memory consumption, and saves network bandwidth.

---

### 7. What do `limit` and `skip` do?
* **`skip`** (or offset): Specifies the number of records to skip from the beginning of the query result.
* **`limit`**: Specifies the maximum number of records to return in the current request.

**Example:**
```python
# URL: /notes?skip=20&limit=10
@app.get("/notes")
def get_notes(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    # Skips the first 20 records, returns the next 10
    notes = session.exec(select(Note).offset(skip).limit(limit)).all()
    return notes
```

---

### 8. Can an endpoint have both Path and Query Parameters?
Yes. An endpoint can identify a specific resource or parent category using a path parameter, while filtering, sorting, or paginating sub-resources using query parameters.

**Example:**
```python
# URL: /users/42/items?limit=5
@app.get("/users/{user_id}/items")
def get_user_items(user_id: int, limit: int = 10):
    return {"user_id": user_id, "limit": limit}
```

---

### 9. Are Query Parameters mandatory?
No, they are **optional by default** if they have default values (e.g., `limit: int = 10`) or are typed as optional (e.g., `q: str | None = None`). However, if you declare a query parameter without a default value, FastAPI treats it as **mandatory**, and omitting it will trigger a `422 Unprocessable Entity` error.

**Example:**
```python
@app.get("/search")
def run_search(
    query: str,                 # MANDATORY query param (no default)
    category: str | None = None # OPTIONAL query param (defaults to None)
):
    return {"query": query, "category": category}
```

---

### 10. Give real-world examples of both.
* **Path Parameter (Amazon Product):** `https://amazon.com/products/B08N5WRWNW`
  Here, `B08N5WRWNW` is a path parameter identifying a specific unique MacBook model in the products catalog.
* **Query Parameter (Amazon Search):** `https://amazon.com/search?q=laptop&brand=apple`
  Here, `q=laptop` and `brand=apple` filter the products list to show only Apple laptops, without changing the base search page route.

---

# Key Takeaways

* Path Parameters identify a resource.
* Query Parameters customize the returned data.
* Use `limit` and `skip` for pagination.
* Query Parameters are commonly used for filtering, searching, and sorting.
* Almost every production API uses Query Parameters.
