#!/usr/bin/env bash
set -euo pipefail

COMPOSE_FILE=${MINDWIKI_COMPOSE_FILE:-${HOME}/.local/share/mindwiki/docker-compose.yml}
DOCKER_COMPOSE=${MINDWIKI_DOCKER_COMPOSE:-$(which docker-compose)}

CALLED_AS=$(basename ${0})

OPTIONS_COMPOSE="--file ${COMPOSE_FILE} --project-name mindwiki"
OPTIONS_UP="--no-build -d"

case ${CALLED_AS} in
  "mindwiki-up")
    exec ${DOCKER_COMPOSE} ${OPTIONS_COMPOSE} up ${OPTIONS_UP}
    ;;
  "mindwiki-down")
    exec ${DOCKER_COMPOSE} ${OPTIONS_COMPOSE} down
    ;;
  *)
    echo "[ERROR] Action unknown: ${CALLED_AS}"
    ;;
esac
