#! /bin/bash

# create a virtual environment if it doesn't exist yet
[ ! -d "venv" ] && virtualenv venv

# activate the virtual environment
source venv/bin/activate

#upgrading pip
python -m pip install --upgrade pip

# install requirements from requirements.txt
pip install -r requirements.txt

# migrate the database
python manage.py migrate

# running the server on default (8000) port
python manage.py runserver