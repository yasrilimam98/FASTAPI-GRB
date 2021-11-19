import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
import configparser
import pymysql.cursors

# config = configparser.ConfigParser()
# config.read('alembic.ini')

# SQLALCHEMY_DATABASE_URL = config.get('alembic', 'sqlalchemy.url')

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# conn = engine.connect()


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3308/grbclient"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
conn = engine.connect()
