from schemas.client import ClientSchema, Clients
from models.client import Mclient
from fastapi import APIRouter, Response, status
from config.database import conn
from fastapi import FastAPI, Depends, HTTPException
from auth import AuthHandler
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm



client = APIRouter() 

auth_handler = AuthHandler()
users = []

@client.get('/Client/all', response_model=Clients,
             description="Menampilkan semua data")
async def find_all_client(limit: int = 10, offset: int = 0):
    query = Mclient.select().offset(offset).limit(limit)
    data = conn.execute(query).fetchall()
    response = {"limit": limit, "offset": offset, "data": data}
    return response

# @karyawan.get('/Karyawan/id',
#              description="Menampilkan id data")
# async def find_karyawan(id: int):
#     query = Karyawan.select().where(Karyawan.c.id_karyawan == id)

#     #print(karyawan.c)
#     data = conn.execute(query).fetchone()
#     if data is None:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {"message": "data tidak ditemukan", "status": response.status_code}

#     response = {"message": f"sukses mengambil data dengan id", "id":id, "data": data}
#     return response

# @karyawan.post('/karyawan/',status_code=201,
#               description="Menambah data karyawan")
# async def insert_karyawan(auth_details : KaryawanSchema, response: Response):
#     def register(auth_details: UserReg):
#         if any(x['email_karyawan'] == auth_details.email_karyawan for x in users):
#             raise HTTPException(status_code=400, detail='Email is taken')
#     hashed_password = auth_handler.get_password_hash(auth_details.password)
#     users.append({
#         'email_karyawan': auth_details.email_karyawan,
#         'password': hashed_password    
#     })
#     cek_email = Karyawan.select().filter(Karyawan.c.email_karyawan == auth_details.email_karyawan)
#     cek_email = conn.execute(cek_email).fetchone()
#     if cek_email is not None:
#         response.status_code = status.HTTP_400_BAD_REQUEST
#         return {"status": response.status_code, "message": "email sudah digunakan"}

#     query = Karyawan.insert().values(
#         nama_karyawan = auth_details.nama_karyawan,
#         alamat_karyawan = auth_details.alamat_karyawan,
#         ttl_karyawan = auth_details.ttl_karyawan,
#         telp_karyawan = auth_details.telp_karyawan,
#         email_karyawan = auth_details.email_karyawan,
#         password = auth_details.password
#     )
#     # print(query)
#     conn.execute(query)
#     data = Karyawan.select().order_by(Karyawan.c.id_karyawan.desc())
#     response = {"message": f"sukses menambahkan data baru", "data": conn.execute(data).fetchone() }
#     return response

# @karyawan.post('/karyawan/{id}',
#               description="mengubah data karyawan")
# async def update_karyawan(id: int, kyw : KaryawanSchema, response: Response):

#     cek_email = Karyawan.select().filter(Karyawan.c.email_karyawan == kyw.email_karyawan, Karyawan.c.id_karyawan != id)
#     cek_email = conn.execute(cek_email).fetchone()
#     if cek_email is not None:
#         response.status_code = status.HTTP_400_BAD_REQUEST
#         return {"status": response.status_code, "message": "email sudah digunakan"}

#     query = Karyawan.update().values(
#         nama_karyawan = kyw.nama_karyawan,
#         alamat_karyawan = kyw.alamat_karyawan,
#         ttl_karyawan = kyw.ttl_karyawan,
#         telp_karyawan = kyw.telp_karyawan,
#         email_karyawan = kyw.email_karyawan
#     ).where(karyawan.c.id_karyawan == id)
#     # print(query)
#     conn.execute(query)
#     data = karyawan.select().where(karyawan.c.id_karyawan == id)
#     response = {"message": f"sukses mengubah data dengan id {id}", "data": conn.execute(data).fetchone() }
#     return response

# @karyawan.delete('/karyawan/{id}',
#               description="menghapus data karyawan")
# async def hapus_karyawan(id: int, response: Response):

#     query = Karyawan.select().where(Karyawan.c.id_karyawan == id)
#     data = conn.execute(query).fetchone()
#     if data is None:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {"message": "data tidak ditemukan", "status": response.status_code}

#     query = Karyawan.delete().where(Karyawan.c.id_karyawan == id)
#     conn.execute(query)
#     response = {"message": f"sukses menghapus data dengan id {id}" }
#     return response

