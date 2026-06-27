from __future__ import annotations
from sqlmodel import SQLModel, Field

# Database Table Model (Response Model as well)
class Note(SQLModel, table=True):
    id: int | None = Field(
        default=None,
        primary_key=True
    )
    title: str
    description: str
    content: str


# Data Transfer Object (DTO) / Request Schema Model
class CreateNote(SQLModel):
    title: str
    description: str
    content: str
