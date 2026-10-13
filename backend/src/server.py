from dotenv import load_dotenv

import os

load_dotenv()


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1 import router as v1_router
from domain.user.model import User
from domain.worker.model import Worker
from domain.job.model import Job

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods="*",
    allow_headers="*"
)
app.include_router(v1_router,prefix="/seva_setu")


