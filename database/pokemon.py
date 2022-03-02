from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from sqlalchemy.dialects.postgresql import JSON

app = Flask(__name__)
#                                                     username:pw                  db_name
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:docker@172.17.0.2:5432/docker'
db = SQLAlchemy(app)


class Pokemon(db.Model):
    __tablename__ = 'pokemon'
    pokemon_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    poke_json = db.Column(db.JSON, nullable=False)


    def __init__(self, id, pokemon_name, json_string):
        self.pokemon_id = id
        self.name = pokemon_name
        self.poke_json = json_string


    def __repr__(self):
        string = 'Pokemon ID: ' + str(self.pokemon_id) + '\n' \
               + 'Pokemon name: ' + str(self.name) + '\n'
        return string
