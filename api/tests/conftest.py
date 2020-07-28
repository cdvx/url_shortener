import os

import pytest
from api import create_app
from flask import current_app

from ..models import db
from ..models.url import Link


@pytest.yield_fixture(scope='session')
def app():
    """
    Setup flask test app, this only gets executed once.
    :return: Flask app
    """

    os.environ['FLASK_ENV'] = 'testing'
    _app = create_app()

    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def client(app):
    """
    Setup an app client, this gets executed for each test function.
    :param app: Pytest fixture
    :return: Flask app client
    """
    yield app.test_client()
