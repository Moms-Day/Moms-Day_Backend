import pytest

from app import create_app
from config.test import TestConfig


@pytest.fixture(scope='session')
def flask_app():
    app = create_app(TestConfig)
    app_context = app.app_context()
    app_context.push()

    yield app

    app_context.pop()


@pytest.fixture(scope='session')
def flask_client(flask_app):
    return flask_app.test_client()
