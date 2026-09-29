from fastapi import FastAPI
from core.session import Base, engine
from domain.user.model import User
from domain.worker.model import Worker
from domain.job.model import Job
from core.twilo import setup,verifi,opt_send
# from src.domain.user.router import router as user

app = FastAPI()
print(verifi(754595))


# Base.metadata.create_all(bind=engine) # Removed because we use Alembic for migrations

# app.include_router(user)
