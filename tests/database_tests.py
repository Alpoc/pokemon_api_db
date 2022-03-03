import pytest
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# rootdir is app so not sure why this is needed...
# sys.path.append('..')
import database.database_actions


def test_fetch_from_api_no_data(app):
    dba = DatabaseActions()
    _, response = dba.insert_poke_into_db(poke)
    assert 200 in response


def test_fetch_from_api_with_name(app):
    response = client.get('/api_fetch/bulbasaur')
    assert 'name:	"bulbasaur"' in response.data


def test_fetch_from_api_with_id(app):
    response = client.get('/api_fetch/1')
    assert 'name:	"bulbasaur"' in response.data
