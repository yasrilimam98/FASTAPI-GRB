from datetime import date
from pydantic import BaseModel, Field
from typing import List, Optional
from pydantic import BaseModel



class KaryawanSchema(BaseModel):
    nama_karyawan: str = Field(..., min_length=3, max_length=255)
    alamat_karyawan: str = Field(..., min_length=3, max_length=255)
    ttl_karyawan: date = Field(...)
    telp_karyawan: str = Field(..., min_length=3, max_length=255)
    email_karyawan: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=3, max_length=50)

class Karyawan(KaryawanSchema):
    id_karyawan: int

# list karyawan API
class Karyawans(BaseModel):
    limit: int = Field(default=5)
    offset: int = Field(default=0)
    data: List[Karyawan]

class UserLogin(BaseModel):
    email_karyawan: str
    password: str

class UserReg(BaseModel):
    nama_karyawan:str
    email_karyawan: str
    password:str

# List Token
class Token(BaseModel):
    """definition token Data model for"""
    access_token: str
    token_type: str
    

class TokenData(BaseModel):
    email_karyawan: Optional[str] = None


