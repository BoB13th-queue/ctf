from fastapi import HTTPException
from datetime import timedelta, datetime
from jose import jwt
from sqlalchemy.orm import Session
from starlette import status


from database.models import Note
from core.config import auth_config
from service.user import crud as user_crud
from service.user import schema as user_schema
from service.auth import schema as auth_schema
from service.note import schema as note_schema

def add_note(db: Session, title: str, content: str, user_id: int) -> dict:
    new_note = Note(
        title=title,
        content=content,
        author=user_id,
        created_at=datetime.now(),
    )

    db.add(new_note)
    db.commit()

def get_note_list(db: Session, limit: int, page: int) -> dict:
    page -= 1
    notes = db.query(Note)
    cnt = notes.count()

    notes = notes.limit(limit).offset(page * limit).all()
    notes = [note.__dict__ for note in notes]
    
    notes = [
        {
            **n,
            "author": user_crud.get_user_by_id(db, n["author"]).username
        }
        for n in notes
    ]
    
    return {
        "cnt": cnt,
        "page": page+1,
        "limit": limit,
        "notes": notes
    }

def get_note_by_id(db: Session, note_id: int) -> dict:
    note = db.query(Note).filter(Note.id == note_id).first()

    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found!"
        )
    
    author = user_crud.get_user_by_id(db, note.author).username

    return {
        "id": note.id,
        "title": note.title,
        "content": note.content,
        "author": author,
        "created_at": note.created_at,
        "updated_at": note.updated_at
    }

def update_note_info(db: Session, note_id: int, title: str, content: str) -> dict:
    note = db.query(Note).filter(Note.id == note_id).first()

    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found!"
        )

    db.query(Note).filter(Note.id == note_id).update({
        "title": title,
        "content": content,
        "updated_at": datetime.now()
    })
    db.commit()

    return {"message": "Note updated successfully!"}


def delete_note(db: Session, note_id: int) -> dict:
    note = db.query(Note).filter(Note.id == note_id).first()

    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found!"
        )

    db.delete(note)
    db.commit()

    return {"message": "Note deleted successfully!"}