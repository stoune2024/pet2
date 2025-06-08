from fastapi import APIRouter, Request, status, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from typing import Annotated

from .safety import TokenData, verify_token

router = APIRouter(tags=['Ручки'])

templates = Jinja2Templates(directory=['templates', 'app/templates', '../app/templates'])


@router.get('/')
async def get_index(
        request: Request,
):
    user_token = request.cookies.get('access-token')
    """ Эндпоинт отображения главного раздела сайта """
    if user_token:
        return templates.TemplateResponse(request=request, name='index.html')
    return RedirectResponse('/auth', status_code=status.HTTP_303_SEE_OTHER)


@router.get('/auth')
async def get_auth_page(
        request: Request,
):
    """ Эндпоинт отображения страницы с авторизацией """
    return templates.TemplateResponse(request=request, name='oauth.html')


@router.get('/suc_auth')
async def get_auth_page(
        request: Request,
):
    """ Эндпоинт отображения страницы с авторизацией """
    return templates.TemplateResponse(request=request, name='suc_oauth.html')


@router.get('/submit')
async def get_submit_docs_page(
        request: Request,
        user_token: Annotated[TokenData, Depends(verify_token)],
):
    """ Эндпоинт отображения страницы с подачей документов """
    if user_token:
        return templates.TemplateResponse(request=request, name='submit_docs.html')


@router.get('/contacts')
async def get_contacts_page(
        request: Request,
        user_token: Annotated[TokenData, Depends(verify_token)],
):
    """ Эндпоинт отображения страницы с контактами """
    if user_token:
        return templates.TemplateResponse(request=request, name='contacts_page.html')


@router.get('/certificates')
async def get_certs_page(
        request: Request,
        user_token: Annotated[TokenData, Depends(verify_token)],
):
    """ Эндпоинт отображения страницы с удостоверениями """
    if user_token:
        return templates.TemplateResponse(request=request, name='my_certs_page.html')


@router.get('/exit')
async def get_exit_page(
        request: Request,
):
    """ Эндпоинт выхода из учетной записи """
    response = templates.TemplateResponse(request=request, name='log_out.html')
    response.delete_cookie(key='access-token')
    return response
