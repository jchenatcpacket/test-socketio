FROM python:3.9-slim-bookworm

RUN apt update && apt install curl -y

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /server

RUN pip install \
    python-socketio[asyncio] \
    fastapi[standard] \
    uvicorn \
    pytest
