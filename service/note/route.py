from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette import status

from database.database import get_db
from database.models import Users
from service.user import crud as user_crud
from service.note import schema as note_schema
from service.note import crud as note_crud
from utils.oauth import get_current_user


router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)

# Create
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_note(note_data: note_schema.NoteReq, current_user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    print(note_data.dict(), current_user.id )
    note_crud.add_note(db, **note_data.dict(), user_id=current_user.id)

# Read
@router.get("/", response_model=note_schema.NoteListRes)
async def get_note_list(limit: int = 10, page: int = 1, db: Session = Depends(get_db)):
    return note_crud.get_note_list(db, limit, page)

@router.get("/{note_id}", response_model=note_schema.NoteRes)
async def get_note(note_id: int, db: Session = Depends(get_db)):
    return note_crud.get_note_by_id(db, note_id)

# Update
@router.put("/{note_id}", status_code=status.HTTP_200_OK)
async def update_note(note: note_schema.NoteReq, note_id: int, current_user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    note_author = note_crud.get_note_by_id(db, note_id)
    author = user_crud.get_user_by_username(db, note_author['author'])

    if current_user.id != author.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized!"
        )
    
    note_crud.update_note_info(db, note_id, **note.dict())

# Delete
@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(note_id: int, current_user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    note_author = note_crud.get_note_by_id(db, note_id)
    author = user_crud.get_user_by_username(db, note_author['author'])

    if current_user.id != author.id and current_user.role != 'admin':
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized!"
        )

    note_crud.delete_note(db, note_id)