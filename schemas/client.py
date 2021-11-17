from datetime import date
from pydantic import BaseModel, Field
from typing import List, Optional
from pydantic import BaseModel



class ClientSchema(BaseModel):
    regno: int = Field(default=None)
    serial: str = Field(..., min_length=3, max_length=19)
    duedate: date = Field(...)
    name: str = Field(..., min_length=3, max_length=70)
    dbname: str = Field(..., min_length=3, max_length=25)
    dbport: str = Field(..., min_length=2, max_length=5)
    localnetwork: str = Field(..., min_length=3, max_length=12)
    localport: str = Field(..., min_length=3, max_length=5)
    publicnetwork: str = Field(..., min_length=10, max_length=150)
    publicport: str = Field(..., min_length=1, max_length=5)
    addressline1: str = Field(..., min_length=15, max_length=150)
    city: str = Field(..., min_length=5, max_length=50)
    stateprov: str = Field(..., min_length=1, max_length=50)
    zipcode: str = Field(..., min_length=2, max_length=6)
    delete: str = Field(..., min_length=1, max_length=1)

class Client(ClientSchema):
    id: int

# list karyawan API
class Clients(BaseModel):
    limit: int = Field(default=5)
    offset: int = Field(default=0)
    data: List[Client]




