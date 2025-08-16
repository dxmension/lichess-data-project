import os
from dotenv import load_dotenv

from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)
db_session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

