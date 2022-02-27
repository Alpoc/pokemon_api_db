

# Dev installs for when not using docker
## base installs
sudo apt-get install python3.6
pip install pytest

## flask installs
sudo apt-get install python3-venv
. venv/bin/activate
pip install Flask
pip3 install flask-restful
pip3 install requests

### postgresql/flask stuff
pip install Flask-Script
pip install Flask-SQLAlchemy
pip install psycopg2-binary

## docker setup
### pick you flavor here
https://docs.docker.com/engine/install/ubuntu/


### docker 'connect: permission denied'
### this opens it up to everyone
sudo chmod 666 /var/run/docker.sock

## postgres docker build
docker build .

docker image rm <name>
docker container rm <name>


## get ip of container
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id

### safer root only
sudo chown root:docker /var/run/docker.sock

# commands to run

export FLASK_ENV=development
. venv/bin/activate
flask run
