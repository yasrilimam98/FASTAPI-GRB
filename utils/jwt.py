from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session

import sqlalchemy as sa
from config.database import conn
# from sqlapp.database import SessionLocal
# from sqlapp.schemas import *
# from sqlapp.crud import *



# If you need to get a new SECRET_KEY needs to run openssl rand -hex 32
SECRET_KEY = "bf3af7cd522a80657063b1eef7c6e54326656b286af90ab1eb79ea5eb68479d1"
# Define the algorithm used for encryption and decryption
ALGORITHM = "HS256"
# Validity period of token
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_db():
    try:
        db = conn()
        yield db
    finally:
        db.close()


# Create an encryption and decryption context (regardless of what these two sentences mean)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """establish tokens function
    :param data: Right use JWT of Payload Field, here is tokens Here is the user's information
    :param expires_delta: Default parameter, deadline
    :return:
    """
    # Deep copy data
    to_encode = data.copy()
    # If the deadline is carried, set the expiration time of tokens separately
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    # Coding, JWT tokens was born
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme),db: Session = Depends(get_db)):
    """Getting the current user information is actually a decryption token Process of
    :param token: Carried token
    :return:
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decrypt tokens
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Get the user name from the payload of tokens
        username: str = payload.get("sub")
        # If not, an exception is thrown
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    # Query user information from database
    user = get_user_by_email(db,email=username)
    if user is None:
        raise credentials_exception
    return user



async def get_current_active_user(current_user: User = Depends(get_current_user)):
    """Obtaining the current user information is actually used as a dependency and injected into other routes for use.
    :param current_user:
    :return:
    """
    return current_user