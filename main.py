import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.client import client
# from fastapi_simple_security import api_key_router, api_key_security
# from fastapi import Depends, FastAPI

app = FastAPI()

def cors_headers(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
        )
    return app

app.include_router(client)
@app.get("/")
async def root():
    return {"message": "TesAPI GRB"}
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
