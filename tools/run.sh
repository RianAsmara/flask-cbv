#!/usr/bin/env bash

# Change this PATH Variable with your interpreter path
export PATH=$PATH:$YOUR_INTERPRETER_PATH

export API_VERSION="v0.1"

export APP_MODE="Your app mode [production, testing, development]"

export DABASE_URI="mysql+pymysql://username:password@localhost/database_name"

export SECRET_KEY="your secret key here"

python $PWD/manage.py runserver