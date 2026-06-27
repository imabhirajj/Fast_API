from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Session, select

from database import engine
from models import Note, CreateNote

app = FastAPI()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


create_db_and_tables()


# CREATE
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


# READ ALL
@app.get("/notes")
def get_notes():

    with Session(engine) as session:
        notes = session.exec(
            select(Note)
        ).all()

    return notes


# READ ONE
@app.get("/notes/{note_id}")
def get_note(note_id: int):

    with Session(engine) as session:

        note = session.get(Note, note_id)

        if not note:
            raise HTTPException(
                status_code=404,
                detail="Note not found"
            )

    return note


# UPDATE
@app.put("/notes/{note_id}")
def update_note(note_id: int, note: CreateNote):

    with Session(engine) as session:

        db_note = session.get(Note, note_id)

        if not db_note:
            raise HTTPException(
                status_code=404,
                detail="Note not found"
            )

        db_note.title = note.title
        db_note.description = note.description
        db_note.content = note.content

        session.add(db_note)
        session.commit()
        session.refresh(db_note)

    return db_note


# DELETE
@app.delete("/notes/{note_id}")
def delete_note(note_id: int):

    with Session(engine) as session:

        note = session.get(Note, note_id)

        if not note:
            raise HTTPException(
                status_code=404,
                detail="Note not found"
            )

        session.delete(note)
        session.commit()

    return {
        "message": "Note deleted successfully"
    }
