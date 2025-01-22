from fastapi import HTTPException
from datetime import timedelta, datetime
from jose import jwt
from sqlalchemy.orm import Session
from starlette import status


from database.models import Users
from core.config import auth_config
from service.user import user_crud
from service.user import user_schema
from service.auth import auth_schema
from utils.passHash import hash_password, check_password


def add_user(db: Session, username: str, password: str, full_name: str, role: str = "user") -> user_schema.UserRes:
    if user_crud.get_user_by_username(db, username) is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists!"
        )

    new_user = Users(
        username=username,
        full_name=full_name,
        password=hash_password(password),
        role=role,
    )

    db.add(new_user)
    db.commit()

    return {
        "message": "User created successfully!",
        "user": {
            "username": new_user.username,
            "full_name": new_user.full_name,
            "role": new_user.role
        }
    }


def register_admin(db: Session,
                   username: str,
                   full_name: str,
                   password: str) -> dict:
    return add_user(db, username, password, full_name, 'admin')


def authenticate_user(db: Session, username: str, password: str) -> auth_schema.Token:
    user = db.query(Users).filter(Users.username == username).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if check_password(password, user.password) is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    data = {
        "sub": user.username,
        "exp": datetime.now() + timedelta(minutes=auth_config.ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(data, auth_config.SECRET_KEY, algorithm=auth_config.ALGORITHM)

    return auth_schema.Token(access_token=access_token, token_type="bearer", username=user.username, role=user.role)
