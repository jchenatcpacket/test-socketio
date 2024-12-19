# test_main.py
import pytest


# pytest -s                  # disable all capturing
# pytest --capture=sys       # replace sys.stdout/stderr with in-mem files
# pytest --capture=fd        # also point filedescriptors 1 and 2 to temp file
# pytest --capture=tee-sys   # combines 'sys' and '-s', capturing sys.stdout/stderr
#                            # and passing it along to the actual sys.stdout/stderr

# @pytest.mark.parametrize("sid,expected", [(123, "session id 123\n")])
# def test_event(sid, expected, capsys):
#     from main import my_event
#     my_event(sid, "")
#     captured = capsys.readouterr()
#     assert captured.out == expected

# generate by sonnet following the above example

# test_main.py
import pytest
from unittest.mock import AsyncMock, patch
import time
import asyncio

@pytest.mark.parametrize("sid,expected", [(123, "session id 123\n")])
def test_my_event(sid, expected, capsys):
    from main import my_event
    asyncio.run(my_event(sid, ""))
    captured = capsys.readouterr()
    assert captured.out == expected

@pytest.mark.parametrize("sid,data,expected", [
    (123, "test_data", "session id 123\ndata test_data\n"),
    (456, {"key": "value"}, "session id 456\ndata {'key': 'value'}\n")
])
def test_my_custom_event(sid, data, expected, capsys):
    from main import another_event
    asyncio.run(another_event(sid, data))
    captured = capsys.readouterr()
    assert captured.out == expected

@pytest.mark.parametrize("sid,environ,auth,expected", [
    (123, {}, None, "connect  123\n"),
    (456, {"HTTP_USER_AGENT": "test"}, {"user": "test"}, "connect  456\n")
])
def test_connect(sid, environ, auth, expected, capsys):
    from main import connect
    asyncio.run(connect(sid, environ, auth))
    captured = capsys.readouterr()
    assert captured.out == expected

@pytest.mark.parametrize("sid,expected", [
    (123, "disconnect  123\n"),
    (456, "disconnect  456\n")
])
def test_disconnect(sid, expected, capsys):
    from main import disconnect
    asyncio.run(disconnect(sid))
    captured = capsys.readouterr()
    assert captured.out == expected

@pytest.mark.asyncio
async def test_ongoing_emit():
    from main import ongoing_emit
    with patch('server.main.sio.emit', new_callable=AsyncMock) as mock_emit:
        # Create a task for ongoing_emit
        task = asyncio.create_task(ongoing_emit())
        
        # Wait for a short time to allow the first emission
        await asyncio.sleep(0.1)
        
        # Cancel the task
        task.cancel()
        
        try:
            await task
        except asyncio.CancelledError:
            pass
        
        # Check that emit was called with correct arguments
        mock_emit.assert_called_with('my event', {'data': 'foobar'})

# @pytest.mark.asyncio
# async def test_startup_event():
#     from main import startup_event
#     with patch('asyncio.create_task') as mock_create_task:
#         await startup_event()
#         mock_create_task.assert_called_once()

# # Test the FastAPI endpoints
# def test_read_root():
#     from main import read_root
#     response = read_root()
#     assert response == {"Hello": "World"}

# def test_healthcheck():
#     from main import healthcheck
#     response = healthcheck()
#     assert response.status_code == 200