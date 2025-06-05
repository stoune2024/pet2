from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=['Ручки'])

templates = Jinja2Templates(directory=['templates', 'app/templates', '../app/templates'])


@router.get('/')
async def get_index(
        request: Request,
):
    """ Эндпоинт отображения главного раздела сайта """
    return templates.TemplateResponse(request=request, name='index.html')

@router.get('/auth')
async def get_auth_page(
        request: Request,
):
    """ Эндпоинт отображения страницы с авторизацией """
    return templates.TemplateResponse(request=request, name='oauth.html')

@router.get('/submit')
async def get_submit_docs_page(
        request: Request,
):
    """ Эндпоинт отображения страницы с подачей документов """
    return templates.TemplateResponse(request=request, name='submit_docs.html')

@router.get('/contacts')
async def get_contacts_page(
        request: Request,
):
    """ Эндпоинт отображения страницы с контактами """
    return templates.TemplateResponse(request=request, name='contacts_page.html')

@router.get('/certificates')
async def get_certs_page(
        request: Request,
):
    """ Эндпоинт отображения страницы с удостоверениями """
    return templates.TemplateResponse(request=request, name='my_certs_page.html')

@router.get('/exit')
async def get_exit_page(
        request: Request,
):
    """ Эндпоинт отображения страницы после выхода из учетной записи """
    return templates.TemplateResponse(request=request, name='log_out.html')