# Welcome, this app is a coding assessment for implementing a db api for the pokemon api.
This is a simple api that pulls from a pokemon api and stores it into a db.
The two exposed URLs are
 - http://127.0.0.1:5000/poke_db/
 - http://127.0.0.1:5000/api_fetch/


## Prerequisites
 - docker
 - docker-compose

## Run Commands
### there is a bug that docker-compose depends_on is not working for my flask app.
so docker-compose up is used twice.

 - docker-compose build
 - docker-compose up

 ### after its up and running you can also run unit tests with
  - docker exec -it poke_flask_container py.test
