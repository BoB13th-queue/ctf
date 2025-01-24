from contextlib import asynccontextmanager

import uvicorn
import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
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
            user_crud.register_admin(db, os.getenv("ADMIN_USER"), os.getenv("ADMIN_PASS"), "Admin User")
    yield

app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

for route in routers:
    app.include_router(route)

if __name__ == "__main__":
    uvicorn.run("main:app", **server_config.__dict__)
