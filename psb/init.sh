#!/usr/bin/env bash

mkdir uploads
mkdir uploads/banners

chmod +x ./run.sh
chmod +x ./migrate.sh && ./migrate.sh && ./run.sh
