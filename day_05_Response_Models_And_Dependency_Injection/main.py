from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import SQLModel, select, Session

from database import engine, get_session
from models import Note, CreateNote

app = FastAPI()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


create_db_and_tables()


# CREATE
@app.post(
    "/notes",
    response_model=Note
)
def create_note(
    note: CreateNote,
    session: Session = Depends(get_session)
):

    db_note = Note(
        title=note.title,
        description=note.description,
        content=note.content
    )

    session.add(db_note)
    session.commit()
    session.refresh(db_note)

    return db_note


# READ ALL
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


# READ ONE
@app.get(
    "/notes/{note_id}",
    response_model=Note
)
def get_note(
    note_id: int,
    session: Session = Depends(get_session)
):

    note = session.get(Note, note_id)

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    return note


# UPDATE
@app.put(
    "/notes/{note_id}",
    response_model=Note
)
def update_note(
    note_id: int,
    note: CreateNote,
    session: Session = Depends(get_session)
):

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
def delete_note(
    note_id: int,
    session: Session = Depends(get_session)
):

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