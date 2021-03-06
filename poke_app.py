# app.py - Pokemon flask api using flask_restful
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import logging
from flask import jsonify
from database.database_actions import DatabaseActions
from pokemon_api.pokemon_api import PokemonAPI
import time
from os import path
# import yaml

app = Flask(__name__)
#                                                     username:pw                  db_name
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:docker@poke_db:5432/docker'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:docker@127.0.0.1:5432/docker'
db = SQLAlchemy(app)
logging.basicConfig(filename='logs/html.log',level=logging.DEBUG)


@app.route('/')
def hello():
    return "Hello and welcome to your new pokedex"


@app.route('/api_fetch/<path:value>')
def fetch_api_poke(value):
    """
    pull pokemon from api and insert into database
    :param value: value from http request
    :return: poke json or string
    """
    logging.info('api fetch requested, value: ' + value)
    poke, response_code = PokemonAPI.fetch_pokemon(value)
    if response_code == 200:
        dba = DatabaseActions()
        response = dba.insert_poke_into_db(poke)
        if response != 201:
            logging.error('something went wrong trying to insert pulled poke')

        return jsonify(poke.as_dict()), response
    else:
        return "could not pull from api"


@app.route('/poke_db/<path:name>')
def render_db_poke(name):
    """
    Renders pokemon json from database
    :param name: http request
    :return: poke json or string
    """
    logging.info('DB fetch requested, value: ' + name)
    dba = DatabaseActions()
    try:
        name = int(name)
        poke_obj, response_code = dba.query_by_id(name)
    except:
        pass
        poke_obj, response_code = dba.query_by_name(name)

    if response_code == 200:
        return poke_obj.as_dict(), response_code
    else:
        return 'could not locate ' + str(name) + '. Please request a db update', response_code

@app.route('/specs')
def return_specification():
    return render_template('specifications.html')


def create_app():
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
    return app


if __name__ == '__main__':
    # This is used in a pinch to get docker compose to behave correctly.
    # wait-for-it is not working since docker compose is using python.
    time.sleep(1)
    create_app()
