#!/usr/bin/env bash

set -euo pipefail

DATA_DIR=${LOCAL_DATA_DIR:-/tmp/mindwiki}

if [ ! -d "${DATA_DIR}" ]; then
  mkdir "${DATA_DIR}"
fi

if [ ! -d "${DATA_DIR}/db" ]; then
  mkdir "${DATA_DIR}/db"
fi

if [ ! -d "${DATA_DIR}/media" ]; then
  mkdir "${DATA_DIR}/media"
fi
