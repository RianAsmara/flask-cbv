#!/usr/bin/env bash

# Change this PATH Variable with your interpreter path
export PATH=$PATH:$YOUR_INTERPRETER_PATH

export API_VERSION="v0.1"
export APP_MODE="Your app mode [production, testing, development]"

export DABASE_URI="mysql+pymysql://username:password@localhost/database_name"

export SECRET_KEY="your secret key here"

export FLASK_APP=app

MIGRATE=migrations

if [[ ! -d "$PWD/$MIGRATE" ]]; then
    flask db init
fi

flask db migrate
flask db upgrade

#if [[ -d "$PWD/$MIGRATE" ]]; then
#    rm -rf $PWD/${MIGRATE}
#fi
