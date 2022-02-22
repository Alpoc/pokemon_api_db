# app.py - a minimal flask api using flask_restful
from flask import Flask, jsonify
from flask_restful import Resource, Api
import requests
import json

# import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/pokemon'
db = SQLAlchemy(app)
# api = Api(app)


class PokemonDB(db.Model):
    __tablename__ = 'pokemon'
    pokemon_id = db.Column(db.String, primary_key=True, nullable=False)
    value = db.Column(db.String, nullable=False)

    def __init__(id, json_string):
        self.pokemon_id = id
        self.value = json_string

class AddPokemon(Resource):
    def get(self):

        # self.hello_world()

        url = 'https://pokeapi.co/api/v2/pokemon/1'
        req = requests.get(url)
        pokes = req.json()
        print(pokes)
        return pokes

# from models import Result

#
@app.route('/')
def hello():
    return "Hello World!"
#
#
@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

# api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    AddPokemon.get()
