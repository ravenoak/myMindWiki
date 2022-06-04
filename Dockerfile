ARG IMAGE_TAG=3.9
ARG USER_ID=1000
ARG USER_NAME=mindwiki

ARG EXTRA_PACKAGES
ARG MINDWIKI_SRC_DIR=/usr/src/mindwiki
ARG MINDWIKI_RUN_DIR=/run/mindwiki
ARG MINDWIKI_DATA_DIR=/var/lib/mindwiki


FROM python:${IMAGE_TAG} as mwbase

ARG USER_ID
ARG USER_NAME
ARG EXTRA_PACKAGES
ARG MINDWIKI_SRC_DIR
ARG MINDWIKI_RUN_DIR
ARG MINDWIKI_DATA_DIR

RUN useradd -m -s /bin/bash -u ${USER_ID} -U ${USER_NAME} && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y plantuml sqlite3 vim-nox ${EXTRA_PACKAGES} && \
    mkdir -p ${MINDWIKI_SRC_DIR} ${MINDWIKI_RUN_DIR} ${MINDWIKI_DATA_DIR} && \
    chown -R ${USER_NAME}:${USER_NAME} ${MINDWIKI_SRC_DIR} ${MINDWIKI_RUN_DIR} ${MINDWIKI_DATA_DIR}

COPY --chown=${USER_NAME}:${USER_NAME} . ${MINDWIKI_SRC_DIR}/
RUN install ${MINDWIKI_SRC_DIR}/assets/entrypoint.sh /usr/local/bin/


FROM mwbase
ARG USER_NAME
ARG MINDWIKI_SRC_DIR

USER ${USER_NAME}
WORKDIR ${MINDWIKI_SRC_DIR}
RUN pip install --user pipenv && \
    /home/mindwiki/.local/bin/pipenv -v install -d && \
    echo 'export SHELL="/bin/bash"' >> ${HOME}/.bashrc && \
    echo '#pipenv shell' >> ${HOME}/.bashrc
EXPOSE 1312
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
