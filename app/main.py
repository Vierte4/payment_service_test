from fastapi import FastAPI
from app.api import authorize

app = FastAPI(title="Payment Processing Service")

app.include_router(authorize.router)