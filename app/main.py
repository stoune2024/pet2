from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from os.path import relpath

from app.routers.routs import router as routs_router
from app.routers.db import router as db_router

app = FastAPI()

app.include_router(routs_router)
app.include_router(db_router)

app.mount('/static_files', StaticFiles(directory=relpath(f'{relpath(__file__)}/../static')), name='static')
