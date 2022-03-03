# Welcome, this app is a coding assessment for implementing a db api for the pokemon api.
This is a simple api that pulls from a pokemon api and stores it into a db. The app is build to show the ability to create an api that can serve data from a database. This app pull from https://pokeapi.co/. The database upon creation contains nothing. When a user pull from the pokemon api using the flask server provided it automatically updates the database. The user can then display that saved database entry. 

## The exposed URLs are
 - http://127.0.0.1:5000/poke_db/<pokemon id or name>
 - http://127.0.0.1:5000/api_fetch/<pokemon id or name>
 - http://127.0.0.1:5000/specs


## Prerequisites
 - docker
 - docker-compose

## Run Commands
 - docker-compose build
 - docker-compose up
