#!/bin/bash

set -o errexit
set -o nounset

export POETRY_PATH=$(poetry env info --path)
source $POETRY_PATH/bin/activate

sleep 10s

flask db init
flask db migrate
flask db upgrade
gunicorn -b :5000 manage:app