# kinnow
GUI based network deployment


set JWT_SECRET_KEY=hello123
set JWT_REFRESH_SECRET_KEY=hello4321

# Kinnow API docs link
http://localhost:8000/api/docs/

## poetry common commands
poetry install # install dependencies
poetry shell # activate virtual environment
poetry update # update dependencies
poetry add <package> # add a new dependency
poetry remove <package> # remove a dependency
poetry run <command> # run a command inside the virtual environment
poetry build # build the package
poetry publish # publish the package
poetry config --list # list the current configuration
poetry env info # show information about the current virtual environment
poetry env use <interpreter> # use the given interpreter for the virtual environment
poetry check # check for problems


## poetry commands for development
poetry add --dev <package> # add a new dev dependency
poetry remove --dev <package> # remove a dev dependency
poetry run pytest # run tests
poetry run black . # run black

# Kinnow postgresql setup
sudo apt-get install postgresql postgresql-contrib
postgres url postgresql://kinnow:kinnow@192.168.232.129:5432/kinnow
sudo -u postgres createuser kinnow
sudo -u postgres createdb kinnow
sudo -u postgres psql
postgres=# CREATE DATABASE kinnow;
To create tables in postgres database run the following command in the terminal
python kinnow/create_tables.py


