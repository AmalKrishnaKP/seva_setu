from dotenv import load_dotenv
import os

load_dotenv()


from fastapi import FastAPI
from api.v1 import router as v1_router
from domain.user.model import User
from domain.worker.model import Worker
from domain.job.model import Job

app = FastAPI()

app.include_router(v1_router,prefix="/seva_setu")


