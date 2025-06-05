from typing import Annotated
from fastapi import APIRouter, Depends, Form, Request, Query, HTTPException, Body
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse
from passlib.context import CryptContext
from contextlib import asynccontextmanager

from .create_db_and_tables import engine, User, Base

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


session = Session(bind=engine)


def create_db_and_tables():
    Base.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


@asynccontextmanager
async def lifespan(router: APIRouter):
    create_db_and_tables()
    yield


router = APIRouter(tags=['База данных'], lifespan=lifespan)


# @router.post("/reg/", response_model=None)
# def create_user(user: Annotated[User, Body()], session: SessionDep, request: Request):
#     """
# Функция создает пользователя и добавляет его в базу данных.
#     :param user: Объект модели User
#     :param session: Сессия
#     :param request: Запрос. Требуется для Jinja2 для создания шаблона
#     :return: Шаблон Jinja2, говорящий об успешной регистрации
#     """
#     hashed_password = pwd_context.hash(user.password)
#     extra_data = {"hashed_password": hashed_password}
#     db_user = User.model_validate(user, update=extra_data)
#     session.add(db_user)
#     session.commit()
#     session.refresh(db_user)
#     # return templates.TemplateResponse(request=request, name="notification.html", context={
#     #     "message": redis_client.hget('successful_registration_page', 'message')
#     # })
#     return {"message":"all is fine!"}
