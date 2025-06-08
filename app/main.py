from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from os.path import relpath

from app.routers.routs import router as routs_router, templates
from app.routers.db import router as db_router
from app.routers.safety import router as safety_router

app = FastAPI()

app.include_router(routs_router)
app.include_router(db_router)
app.include_router(safety_router)

app.mount('/static_files', StaticFiles(directory=relpath(f'{relpath(__file__)}/../static')), name='static')


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    if exc.status_code == 401:
        return templates.TemplateResponse(
            request=request,
            name="401_error.html",
            status_code=exc.status_code,
            headers=exc.headers,
        )
    if exc.status_code == 404:
        return templates.TemplateResponse(
            request=request,
            name="404_error.html",
            status_code=exc.status_code,
            headers=exc.headers,
        )