from service.user import crud
from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database.database import get_db
from service.auth import crud as auth_crud
from service.auth import schema as auth_schema

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register", response_model=auth_schema.AuthRes)
async def register_user(register_req: auth_schema.RegisterReq, db: Session = Depends(get_db)):
    return auth_crud.add_user(db, **register_req.dict())


@router.post("/login", response_model=auth_schema.Token)
async def login(login_req: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return auth_crud.authenticate_user(db, login_req.username, login_req.password)
