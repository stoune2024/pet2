from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers.routs import router as routs_router, templates
from os.path import relpath

app = FastAPI()

app.include_router(routs_router)

app.mount('/static_files', StaticFiles(directory=relpath(f'{relpath(__file__)}/../static')), name='static')
