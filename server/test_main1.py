# test_main.py by GPT4o
import pytest
from unittest import mock
from server.main import sio, connect, message, disconnect

@pytest.fixture
def mock_sio():
    mock_sio = mock.MagicMock()
    sio._emit_internal = mock_sio.emit
    return mock_sio

def test_connect(mock_sio):
    sid = '1234'
    environ = {}

    connect(sid, environ)

    mock_sio.emit.assert_called_with('connected', {'data': 'Connected successfully'}, room=sid)

def test_message(mock_sio):
    sid = '1234'
    data = {'data': 'Hello'}

    message(sid, data)

    mock_sio.emit.assert_called_with('response', {'data': 'Message received'}, room=sid)

def test_disconnect(mock_sio):
    sid = '1234'

    disconnect(sid)

    # Disconnect event does not emit any message in this implementation
    mock_sio.emit.assert_not_called()
