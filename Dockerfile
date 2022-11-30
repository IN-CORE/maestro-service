FROM python:3.9-slim

ARG WORKERS
ENV WORKERS=${WORKERS:-4}

ENV POETRY_VIRTUALENVS_CREATE false

RUN apt update && apt upgrade -y

WORKDIR /usr/src/maestro-service

COPY . .

RUN pip install -U pip
RUN pip install poetry
RUN poetry install

ENV POSTGRES_SERVER=localhost \
    POSTGRES_PORT=5432 \
    POSTGRES_USER=maestro \
    POSTGRES_PASSWORD=maestro \
    POSTGRES_DB=maestro \
    ROUTER_PREFIX="/maestro"

CMD gunicorn -b 0.0.0.0:8000 -w ${WORKERS} -k uvicorn.workers.UvicornWorker app.main:app

