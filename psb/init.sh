#!/usr/bin/env bash

mkdir uploads

chmod +x ./run.sh
chmod +x ./migrate.sh && ./migrate.sh
python3 manage.py collectstatic

./run.sh