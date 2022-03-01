import pytest
import sys

# rootdir is app so not sure why this is needed...
# sys.path.append('..')
import poke_app


@pytest.fixture()
def app():
    app = poke_app.create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    return app

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
