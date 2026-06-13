from sqlmodel import SQLModel, Session, select
from database import engine
from models import CreateNote, Note
from fastapi import FastAPI

app = FastAPI()

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

create_db_and_tables()


@app.post("/notes")
def create_note(note: CreateNote):
    db_note = Note(
        title=note.title,
        description=note.description,
        content=note.content
    )

    with Session(engine) as session:
        session.add(db_note)
        session.commit()
        session.refresh(db_note)

    return db_note

@app.get("/notes") # to get all Note
def get_notes():
    with Session(engine) as session:
        notes = session.exec(select(Note)).all()
    return notes

@app.get("/notes/{note_id}") # to get particular note object
def get_note(note_id: int):
    with Session(engine) as session:
        note = session.exec(
            select(Note).where(Note.id == note_id)
        ).first()

    return note
