

# Dev installs for when not using docker
## base installs
sudo apt-get install python3.6

## flask installs
sudo apt-get install python3-venv
. venv/bin/activate
pip install Flask
pip3 install flask-restful
pip3 install requests
pip install Flask-SQLAlchemy
pip install Flask-Script

## docker setup
### pick you flavor here
https://docs.docker.com/engine/install/ubuntu/

### docker 'connect: permission denied'
### this opens it up to everyone
sudo chmod 666 /var/run/docker.sock


## postgres docker
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres


### safer root only
sudo chown root:docker /var/run/docker.sock

# commands to run

export FLASK_ENV=development
. venv/bin/activate
flask run
