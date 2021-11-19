from pymysql import cursors
from schemas.client import ClientSchema, Clients, ClientRegno
# from models.client_models import Client
from models import client_models
from fastapi import Depends, APIRouter, Response, status, FastAPI
from config.database import SessionLocal, conn
from sqlalchemy.orm import Session

client = APIRouter() 

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
        db.refresh()
        db.commit()
    except Exception:
        db.rollback()
    finally:
        db.close()

# def getregno(db: Session, regno: int, serial: str):
#     return db.query(client_models.User).filter("""SELECT CASE WHEN DATEDIFF(duedate,curdate()) < 0 THEN 0 ELSE 1 END as statuslisensi, DATEDIFF(duedate,curdate()) as jmlhari,dbname,dbport,localnetwork,localport,publicnetwork,publicport,`name` FROM mclient Where regno = %s AND serial = %s""").first()

@client.get('/Client/',
             description="Masukan data Registrasi & Serial")
def getregno(regno: int, serial: str, response: Response, db: Session = Depends(get_db)):
    # db_user = getregno(db, regno=regno, serial=serial)
    # query = Client.select().where(Client.c.regno == regno and Client.c.serial == serial)
    # query = """SELECT a.regno, a.serial FROM mclient as a"""
    query =("""SELECT CASE WHEN DATEDIFF(duedate,curdate()) < 0 THEN 0 ELSE 1 END as statuslisensi, DATEDIFF(duedate,curdate()) as jmlhari,dbname,dbport,localnetwork,localport,publicnetwork,publicport,`name` FROM mclient Where regno = %s AND serial = %s""")
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

