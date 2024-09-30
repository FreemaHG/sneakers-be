#!/bin/bash

# Создаем таблицы в БД
alembic upgrade head

# Импорт фикстур
python -m fixtures.import

# Запуск сервера
uvicorn src.main:app --proxy-headers --host 0.0.0.0 --port 8000 --reload