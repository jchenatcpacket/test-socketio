import time
import asyncio

import socketio
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def healthcheck():
    return Response(status_code=200)

# mgr = socketio.AsyncRedisManager('redis://')
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
sio_app = socketio.ASGIApp(sio)

app.mount("/", sio_app)

@sio.event
async def my_event(sid, data):
    print("session id", sid)
    print("data", data)

@sio.on('my custom event')
async def another_event(sid, data):
    print("session id", sid)
    print("data", data)

@sio.event
async def connect(sid, environ, auth):
    print('connect ', sid)

@sio.event
async def disconnect(sid):
    print('disconnect ', sid)

async def ongoing_emit():
    while True:
        await sio.emit('my event', {'data': 'foobar'})
        print("current time", time.strftime("%H:%M:%S"), flush=True)
        await asyncio.sleep(5)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(ongoing_emit())