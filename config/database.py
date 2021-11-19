import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import configparser
import pymysql.cursors,sys

config = configparser.ConfigParser()
config.read('alembic.ini')

SQLALCHEMY_DATABASE_URL = config.get('alembic', 'sqlalchemy.url')

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

conn = engine.connect()

# try:
#     connmysql = pymysql.connect(
#         user="root",
#         password="",
#         host="localhost",
#         port=3308,
#         database="grbclient"
 
#     )
#     print(f"Connected")   
# except pymysql.Error as e:
#     print(f"Error connecting to MariaDB Platform: {e}")
#     sys.exit(1)
# # Base = declarative_base()
# querymsql1 = connmysql.cursor()
# querymsql1.close()

# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3308/grbclient"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()
# querymysql = engine.connect()
