from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database.models import Users
from service.user import schema

def get_user_by_username(db: Session, username: str):
    return db.query(Users).filter(Users.username == username).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(Users).filter(Users.id == user_id).first()

def get_user_list(db: Session, limit: int, page: int) -> dict:
    users = db.query(Users)
    cnt = users.count()

    users = users.limit(limit).offset(page * limit).all()
    users = [user.__dict__ for user in users]
    for user in users:
        user.pop('password')

    return {
        "cnt": cnt,
        "page": page,
        "limit": limit,
        "users": users
    }


def update_user_info(db: Session, username: str, role: str) -> dict:
    current_user = get_user_by_username(db, username)

    if current_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found!"
        )

    db.query(Users).filter(current_user.username == username).update({
        "role": role,
    })
    db.commit()

    return {"message": "User information updated successfully!"}


def delete_user(db: Session, user_id: int) -> dict:
    user = get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found!"
        )

    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully!"}