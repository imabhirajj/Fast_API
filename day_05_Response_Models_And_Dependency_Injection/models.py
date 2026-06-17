from __future__ import annotations
from sqlmodel import SQLModel,Field

class Note(SQLModel,table=True):
  id: int | None = Field(
    default=None,
    primary_key=True
  )

  title: str
  description: str
  content: str


class CreateNote(SQLModel):
  title: str
  description: str
  content: str