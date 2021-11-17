from schemas.client import ClientSchema, Clients, ClientRegno
from models.client import Client
from fastapi import APIRouter, Response, status, FastAPI, Query
from config.database import conn


client = APIRouter() 


@client.get('/Client/{regno}', 
             description="Masukan data Registrasi & Serial")
async def regno(regno: int, serial: str, response: Response):
    query = Client.select().where(Client.c.regno == regno and Client.c.serial == serial)
    data = conn.execute(query).fetchone()
    if data is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message" : "Masa Registrasi Anda telah berakhir", "status": response.status_code}
    response = {"message": f"Masa Registrasi anda berlaku {regno}", "status": data}
    return response

@client.get('/Client/{id}',
             description="Menampilkan id data client")
async def find_client(id: int, response: Response):
    query = Client.select().where(Client.c.id == id)

    #print(karyawan.c)
    data = conn.execute(query).fetchone()
    if data is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "data tidak ditemukan", "status": response.status_code}

    response = {"message": f"sukses mengambil data dengan id {id}", "data": data}
    return response
