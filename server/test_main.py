# test_main.py
import pytest


# pytest -s                  # disable all capturing
# pytest --capture=sys       # replace sys.stdout/stderr with in-mem files
# pytest --capture=fd        # also point filedescriptors 1 and 2 to temp file
# pytest --capture=tee-sys   # combines 'sys' and '-s', capturing sys.stdout/stderr
#                            # and passing it along to the actual sys.stdout/stderr

@pytest.mark.parametrize("sid,expected", [(123, "session id 123\n")])
def test_event(sid, expected, capsys):
    from main import my_event
    my_event(sid, "")
    captured = capsys.readouterr()
    assert captured.out == expected