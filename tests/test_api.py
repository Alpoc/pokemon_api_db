import pytest
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# rootdir is app so not sure why this is needed...
# sys.path.append('..')
import poke_app


@pytest.fixture()
def app():
    # TODO: docker server already running when tryig to test.
    #   Need to figure out better solution.
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:docker@poke_db:5432/docker'
    db = SQLAlchemy(app)

    # app = poke_app.create_app()
    app.config.update({
        "TESTING": True,
    })

    return app

    # clean up / reset resources here

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_fetch_from_api(app):
    response = client.get('/api_fetch/bulbasaur')
    assert 'could not locate' in response.data
