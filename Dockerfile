FROM python:3.11-slim
COPY requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt
COPY ./migrations /migrations
COPY alembic.ini /alembic.ini
COPY .env.prod .env
COPY ./src /src
COPY ./docker /docker
RUN chmod a+x docker/*.sh