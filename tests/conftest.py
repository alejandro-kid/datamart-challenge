import json
import pytest

from api.app import create_app


@pytest.fixture(scope="session")
def app():
    """
    Setup our flask test app, this only gets executed once.

    :return: Flask app
    """
    params = {"DEBUG": False, "TESTING": True, "WTF_CSRF_ENABLED": False}

    _app = create_app(settings_override=params)

    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope="function")
def client(app):
    """
    Setup an app client, this gets executed for each test function.

    :param app: Pytest fixture
    :return: Flask app client
    """
    yield app.test_client()


def helper(json_info)->any:
    for info in json_info:
        first_row = info.decode("utf-8")
        return json.loads(first_row)
