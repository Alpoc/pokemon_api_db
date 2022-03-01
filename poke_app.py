# app.py - Pokemon flask api using flask_restful
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import logging

from database.database_actions import DatabaseActions
from pokemon_api.pokemon_api import PokemonAPI

app = Flask(__name__)
#                                                     username:pw                  db_name
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:docker@poke_db:5432/docker'
db = SQLAlchemy(app)
logging.basicConfig(filename='logs/html.log',level=logging.DEBUG)


@app.route('/')
def hello():
    return "Hello and welcome to your new pokedex"


@app.route('/api_fetch/<path:value>')
def fetch_balb(value):
    logging.info('api fetch requested, value: ' + value)
    poke_id, name, poke_json = PokemonAPI.fetch_pokemon(value)
    if poke_id:
        dba = DatabaseActions()
        response = dba.insert_poke_into_db(poke_id, name, poke_json)
        return "{} pulled from API!".format(poke_json['name'])
    else:
        return "could not pull from api"


@app.route('/poke_db/<path:name>')
def print_balb_db(name):
    logging.info('DB fetch requested, value: ' + name)
    dba = DatabaseActions()
    poke_obj, response_code = dba.query_by_name(name)
    if response_code == 200:
        return str(poke_obj.name + ' pulled from DB')
    else:
        return 'could not locate ' + name + '. Please request a db update'


def create_app():
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
    return app


if __name__ == '__main__':
    create_app()