import pytest
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# rootdir is app so not sure why this is needed...
# sys.path.append('..')
from database.database_actions import DatabaseActions
from poke_app import db, create_app

# @pytest.fixture
# def client():
#     db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
#     flaskr.app.config['TESTING'] = True
#
#     with flaskr.app.test_client() as client:
#         with flaskr.app.app_context():
#             flaskr.init_db()
#         yield client

@pytest.fixture()
def app():
    # TODO: docker server already running when tryig to test.
    #   Need to figure out better solution.
    app = create_app()
    # db = SQLAlchemy(app)
    # db.create_all()
    # app = poke_app.create_app()
    app.config.update({
        "TESTING": True,
    })


    yield app

    # with app.test_client() as client:
    #     yield client

    app.app_context.pop()
    db.session.close()

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_get_when_not_avaiable(app):
    dba = DatabaseActions()
    _, response_code = dba.query_by_id(-1)
    assert 404 == response_code


# def test_get_when_not_avaiable(app):
#     dba = DatabaseActions()
#     _, response_code = dba.query_by_name('bob')
#     assert 404 in response_code

#
# def test_new_poke_in_db(app):
#     dba = DatabaseActions()
#     poke = Pokemon(1, 'slowpoke', '{delicious_in: "slowpoke tail soup"}')
#     _, response_code = dba.insert_poke_into_db(poke)
#     assert 201 in response_code
#
#
# def test_poke_in_db_already(app):
#     dba = DatabaseActions()
#     poke = Pokemon(1, 'slowpoke', '{delicious_in: "slowpoke tail soup"}')
#     _, _ = dba.insert_poke_into_db(poke)
#     _, response_code = dba.insert_poke_into_db(poke)
#     assert 418 in response_code
#
#
# def test_get_lower(app):
#     dba = DatabaseActions()
#     _, response_code = dba.query_by_name('slowpoke')
#     assert 200 in response_code
#
#
# def test_get_uppers(app):
#     dba = DatabaseActions()
#     _, response_code = dba.query_by_name('SlOwPoKe')
#     assert 200 in response_code
#
#
# def test_get_id(app):
#     dba = DatabaseActions()
#     _, response_code = dba.query_by_id(1)
#     assert 200 in response_code
