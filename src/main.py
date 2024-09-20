from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.config import FE_HOST, FE_PORT, DEBUG
from src.urls import register_routers


app = FastAPI(title='sneakers', debug=DEBUG)

# Регистрация роутеров
register_routers(app)

# URL, с которых разрешено делать запросы на сервер
origins = [
    f'http://{FE_HOST}:{FE_PORT}'
]

# Добавляем в middleware Cors для связки фронта и бэка
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)