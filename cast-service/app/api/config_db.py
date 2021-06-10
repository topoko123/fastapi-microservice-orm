from sqlalchemy import create_engine, engine

from sqlalchemy.orm import session, sessionmaker

from sqlalchemy.ext.declarative import declarative_base

from dotenv.main import dotenv_values

from dotenv import load_dotenv

load_dotenv

config_env = dotenv_values(".env")


SQLALCHEMY_DATABASE_URL = config_env['SQLALCHEMY_DATABASE_CAST_URL']
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()