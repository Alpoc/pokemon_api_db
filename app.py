# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



from database.database_actions import DatabaseActions
from pokemon_api.pokemon_api import PokemonAPI

app = Flask(__name__)
#                                                     username:pw                  db_name
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:docker@172.17.0.2:5432/docker'
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/balb')
def fetch_balb():
    poke_id, name, poke_json = PokemonAPI.fetch_pokemon('2')
    dba = DatabaseActions(db)
    dba.insert_poke_into_db(poke_id, name, poke_json)
    return "Hello {}!".format(poke_json['name'])


@app.route('/db_balb')
def print_balb_db():
    dba = DatabaseActions(db)
    return str(dba.query_by_name('bulbasaur'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
