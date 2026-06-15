from fastapi import FastAPI
from sqlmodel import SQLModel, Session, select

from database import engine
from models import Note, CreateNote

app = FastAPI()


# Create tables in database
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


create_db_and_tables()


# CREATE
@app.post("/notes")
def create_note(note: CreateNote):

    # Request body -> Database model
    db_note = Note(
        title=note.title,
        description=note.description,
        content=note.content
    )

    with Session(engine) as session:

        # Add note to session
        session.add(db_note)

        # Save permanently to database
        session.commit()

        # Get latest data (including auto-generated id)
        session.refresh(db_note)

    return db_note


# READ ALL
@app.get("/notes")
def get_notes():

    with Session(engine) as session:

        # Get all notes
        notes = session.exec(
            select(Note)
        ).all()

    return notes


# READ ONE
@app.get("/notes/{note_id}")
def get_note(note_id: int):

    with Session(engine) as session:

        # Find note by primary key
        note = session.get(Note, note_id)

    return note


# UPDATE
@app.put("/notes/{note_id}")
def update_note(note_id: int, note: CreateNote):

    with Session(engine) as session:

        # Get existing note
        db_note = session.get(Note, note_id)

        # If note not found
        if not db_note:
            return {"error": "Note not found"}

        # Update fields
        db_note.title = note.title
        db_note.description = note.description
        db_note.content = note.content

        # Save changes
        session.add(db_note)
        session.commit()
        session.refresh(db_note)

    return db_note


# DELETE
@app.delete("/notes/{note_id}")
def delete_note(note_id: int):

    with Session(engine) as session:

        # Find note
        note = session.get(Note, note_id)

        # If note doesn't exist
        if not note:
            return {"error": "Note not found"}

        # Delete note
        session.delete(note)

        # Save changes
        session.commit()

    return {"message": "Note deleted successfully"}