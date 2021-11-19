from pymysql import cursors
from schemas.client import ClientSchema, Clients, ClientRegno
from models.client import Client
from fastapi import APIRouter, Response, status, FastAPI, Query
from config.database import conn

client = APIRouter() 


@client.get('/Client/', 
             description="Masukan data Registrasi & Serial")
async def regno(regno: int, serial: str, response: Response):
    # query = Client.select().where(Client.c.regno == regno and Client.c.serial == serial)
    query = """SELECT CASE WHEN DATEDIFF(duedate,curdate()) < 0 THEN 0 ELSE 1 END as statuslisensi, DATEDIFF(duedate,curdate()) as jmlhari,dbname,dbport,localnetwork,localport,publicnetwork,publicport,`name` FROM mclient Where regno = %s AND serial = %s"""
    data = conn.execute(query,(regno),(serial)).fetchone()
    
    if data is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message" : "periksa kembali idclient dan serial", "status": response.status_code}
    else : 
         if data.statuslisensi == 1:
            response = {"message": f"Masa Registrasi anda berlaku", "status": data.statuslisensi}
         else : 
            response = {"message": f"Masa Registrasi anda berakhir", "status": data} 
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
