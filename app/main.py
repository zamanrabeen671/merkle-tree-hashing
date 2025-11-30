from fastapi import FastAPI
from app.routes import files
from app.routes import auth
app = FastAPI()
app.include_router(files.router)
app.include_router(auth.router)