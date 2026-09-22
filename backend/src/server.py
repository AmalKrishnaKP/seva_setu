from fastapi import FastAPI
from core.session import base, engine
from domain.user.model import User
from domain.user.router import router as user

app = FastAPI()

base.metadata.create_all(bind=engine)

app.include_router(user)
