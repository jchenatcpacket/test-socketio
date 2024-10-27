FROM python:3.9-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /server

RUN pip install python-socketio[asyncio]
RUN pip install fastapi[standard]
RUN pip install uvicorn
