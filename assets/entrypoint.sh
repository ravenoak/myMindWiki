#!/usr/bin/env bash

if [ -n "${DATA_DIR}" ] && [ -d ${DATA_DIR} ]; then
  if [ ! -d ${DATA_DIR}/db ]; then
    mkdir ${DATA_DIR}/db
  fi
  if [ ! -d ${DATA_DIR}/media ]; then
    mkdir ${DATA_DIR}/media
  fi
fi

exec pipenv run python manage.py runserver 0.0.0.0:1312
