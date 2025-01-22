from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from sqlalchemy.orm import Session

from service import routers
from database import models
from database.database import engine
from core.config import server_config
from service.user import user_crud


@asynccontextmanager
async def lifespan(app: FastAPI):
    models.Base.metadata.create_all(bind=engine)

    with Session(engine) as db:
        if not user_crud.get_user_by_username(db, "admin"):
            user_crud.register_admin(db, "admin", "0000", "Admin User")
    yield

app = FastAPI(lifespan=lifespan)

for route in routers:
    app.include_router(route)

if __name__ == "__main__":
    uvicorn.run("main:app", **server_config.__dict__)
