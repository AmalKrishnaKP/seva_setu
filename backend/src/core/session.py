from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base
import os


load_dotenv()

db_url=os.getenv("DB_URL")
print(db_url)

engine=create_engine(db_url)

session= sessionmaker(autoflush=False,autocommit=False,bind=engine)

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()

base=declarative_base()