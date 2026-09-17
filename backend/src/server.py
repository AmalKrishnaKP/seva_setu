from core.session import base,engin
from sqlalchemy import Column,UUID,ForeignKey,String
import uuid



from fastapi import FastAPI

app=FastAPI()

base.metadata.create_all(bind=engin)