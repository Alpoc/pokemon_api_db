import pytest
import sys

sys.path.append('..')

from app import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_fetch_from_api(app):
    response = app.fetch_balb('/db/1')
    assert b'balbasaur pulled from API!' in response.data
