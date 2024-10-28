from sanic import Sanic
from sanic.response import text
import socketio
import uvicorn

sio = socketio.AsyncServer(async_mode='asgi')
sanic_app = Sanic(__name__)
# sio.attach(sanic_app)
socketio_app = socketio.ASGIApp(sio, sanic_app)


async def background_task():
    """Example of how to send server generated events to clients."""
    while True:
        await sio.sleep(5)
        print("emit event", flush=True)
        await sio.emit('my event', {'data': 'Server generated event'})


@sanic_app.listener('before_server_start')
def before_server_start(sanic_app, loop):
    sio.start_background_task(background_task)


@sanic_app.route('/')
async def index(request):
    return text("hello world")


@sio.event
async def my_event(sid, message):
    await sio.emit('my_response', {'data': message['data']}, room=sid)


@sio.event
async def connect(sid, environ):
    await sio.emit('my_response', {'data': 'Connected', 'count': 0}, room=sid)


@sio.event
def disconnect(sid):
    print('Client disconnected')

if __name__ == "__main__":
    uvicorn.run(socketio_app, host="0.0.0.0", port=8003, log_level="info")