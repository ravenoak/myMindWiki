FROM python:3.9
# ARG USER_ID=1000
# ENV MINDWIKI_ADDR=0.0.0.0
# ENV MINDWIKI_PORT=1312
# ARG MINDWIKI_PORT

RUN useradd -m -u 1000 -U mindwiki && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y bash-completion pipenv plantuml vim-nox && \
    mkdir -p /usr/src/mindwiki /run/mindwiki /var/lib/mindwiki && \
    chown -R mindwiki:mindwiki /usr/src/mindwiki /run/mindwiki /var/lib/mindwiki

COPY --chown=root:mindwiki . /usr/src/mindwiki/

USER mindwiki
WORKDIR /usr/src/mindwiki
RUN pipenv install && echo 'export SHELL="/bin/bash"' >> /home/mindwiki/.bashrc && \
    echo 'pipenv shell' >> /home/mindwiki/.bashrc
EXPOSE 1312
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:1312"]
