ARG IMAGE_TAG=3.9

FROM python:${IMAGE_TAG} as MWBASE
ARG USER_ID=1000
ARG USER_NAME=mindwiki
# ENV MINDWIKI_ADDR=0.0.0.0
# ENV MINDWIKI_PORT=1312
# ARG MINDWIKI_PORT

ARG DJANGO_MINDWIKI_LOC=./third_party/django-mindwiki
ARG EXTRA_PACKAGES
ARG MINDWIKI_SRC_DIR=/usr/src/mindwiki
ARG MINDWIKI_RUN_DIR=/run/mindwiki
ARG MINDWIKI_DATA_DIR=/var/lib/mindwiki

COPY ${DJANGO_MINDWIKI_LOC} /usr/src/django-mindwiki

RUN useradd -m -u ${USER_ID} -U ${USER_NAME} && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y bash-completion pipenv plantuml vim-nox ${EXTRA_PACKAGES} && \
    mkdir -p ${MINDWIKI_SRC_DIR} ${MINDWIKI_RUN_DIR} ${MINDWIKI_DATA_DIR} && \
    chown -R ${USER_NAME}:${USER_NAME} ${MINDWIKI_SRC_DIR} ${MINDWIKI_RUN_DIR} ${MINDWIKI_DATA_DIR}

COPY --chown=root:${USER_NAME} . ${MINDWIKI_SRC_DIR}/
WORKDIR ${MINDWIKI_SRC_DIR}
RUN pipenv install -e /usr/src/django-mindwiki


FROM MWBASE
ARG USER_NAME
ARG MINDWIKI_SRC_DIR

USER ${USER_NAME}
RUN pipenv install -d && echo 'export SHELL="/bin/bash"' >> ${HOME}/.bashrc && \
    echo '#pipenv shell' >> ${HOME}/.bashrc
EXPOSE 1312
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:1312"]
