FROM python:3.9-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /server

# RUN pip install python-socketio[asyncio]
# RUN pip install sanic==20.9.1
# RUN pip install sanic
# RUN pip install uvicorn[standard]

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock ./

# RUN poetry add --editable ../my-package