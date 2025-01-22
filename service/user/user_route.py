from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database.database import get_db
from database.models import Users
from service.user import user_schema
from service.user import user_crud 
from utils.oauth import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# Create is in Auth.py

@router.get("/", response_model=user_schema.UserList)
async def get_user_list(limit: int = 10, page: int = 0, current_user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user.role != 'admin':
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized!"
        )
    return user_crud.get_user_list(db, limit, page)

@router.get("/{user_id}", response_model=user_schema.User)
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return user_crud.get_user_by_id(db, user_id)

# Update
@router.put("/{user_id}", response_model=user_schema.User)
async def update_user_info(user_id: int, update_info: user_schema.User, current_user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user.role != 'admin' and current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized!"
        )
    
    if current_user.role != 'admin' and current_user.username != update_info.username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized!"
        )

    if current_user.role != 'admin' and current_user.role != update_info.role:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized!"
        )

    return user_crud.update_user_info(db, **update_info.dict())


# Delete
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_endpoint(
        user_id: str,
        current_user: Users = Depends(get_current_user),
        db: Session = Depends(get_db)):
    if current_user.role != 'admin' and current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized!"
        )

    return user_crud.delete_user(db, user_id)
