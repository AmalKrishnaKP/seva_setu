from fastapi import FastAPI
from src.core.session import base, engin

app = FastAPI()

base.metadata.create_all(bind=engin)