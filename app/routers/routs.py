from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from os.path import relpath

router = APIRouter(tags=['Ручки'])

templates = Jinja2Templates(directory=['templates', 'app/templates', '../app/templates'])

router.mount('/static_files', StaticFiles(directory=relpath(f'{relpath(__file__)}/../../static')), name='static')


@router.get('/')
async def get_index(
        request: Request,
):
    """ Эндпоинт отображения главного раздела сайта """
    return templates.TemplateResponse(request=request, name='index.html')

