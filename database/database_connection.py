from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')


Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=True)
session = sessionmaker(autocommit=False, autoflush=True, bind=engine)