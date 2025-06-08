from fastapi import APIRouter, Request, status, Depends, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from typing import Annotated
from sqlmodel import SQLModel, Field

from .safety import TokenData, verify_token

router = APIRouter(tags=['Ручки'])

templates = Jinja2Templates(directory=['templates', 'app/templates', '../app/templates'])


class BlankData(SQLModel):
    blank_name: str | None = Field(default=None)


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


@router.post('/submit_nvo')
async def get_submit_nvo_page(
        request: Request,
        data: Annotated[BlankData, Form()],
):
    # validated_data = BlankData.model_validate(data)
    match data.blank_name:
        case "free_day_blank":
            return templates.TemplateResponse(request=request, name='submit_nvo.html')
        case "fireness_blank":
            return {"message":"sudauds"}
        case "payment_blank":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not find user",
                headers={"WWW-Authenticate": "Bearer"},
            )
        case "vacation_blank":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not find user",
                headers={"WWW-Authenticate": "Bearer"},
            )
