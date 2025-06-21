from fastapi import APIRouter, Request, status, Depends, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from typing import Annotated
from sqlmodel import SQLModel, Field


from .safety import TokenData, verify_token
from .db import SessionDep, NvoTable

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


@router.post('/submit/docs')
async def get_submit_docs_page(
        request: Request,
        data: Annotated[BlankData, Form()],
        user_token: Annotated[TokenData, Depends(verify_token)],
):
    if user_token:
        match data.blank_name:
            case "free_day_blank":
                return templates.TemplateResponse(request=request, name='submit_nvo.html')
            case "fireness_blank":
                return {"message":"заявление об увольнении"}
            case "payement_blank":
                return {"message":"заявление о выплате"}
            case "vacation_blank":
                return {"message":"заявление на отпуск"}



@router.post('/submit/docs/nvo')
async def submit_nvo_blank(
        user_token: Annotated[TokenData, Depends(verify_token)],
        session: SessionDep,
        nvo_blank: Annotated[NvoTable, Form()]
):
    """ Эндпоинт добавления информации о заявлениях на НВО от работников """
    if user_token:
        session.add(nvo_blank)
        session.commit()
        session.refresh(nvo_blank)
        return {"message":"blank has been submitted!"}