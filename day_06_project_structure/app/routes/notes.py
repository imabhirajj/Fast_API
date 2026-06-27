from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.database import get_session
from app.models import Note, CreateNote

# Create an APIRouter instance
router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)


# CREATE
@router.post("", response_model=Note)
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
@router.get("", response_model=list[Note])
def get_notes(
    session: Session = Depends(get_session)
):
    notes = session.exec(select(Note)).all()
    return notes


# READ ONE
@router.get("/{note_id}", response_model=Note)
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
@router.put("/{note_id}", response_model=Note)
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
@router.delete("/{note_id}")
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
