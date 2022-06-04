MINDWIKI_INSTALL_LOC ?= ${HOME}/.local/share/mindwiki
MINDWIKI_BIN_DIR ?= ${HOME}/.local/bin
.PHONY: install container-build requirements

${MINDWIKI_INSTALL_LOC}:
	mkdir -p ${MINDWIKI_INSTALL_LOC}

install: ${MINDWIKI_INSTALL_LOC}
	install -C deployments/prod/docker-compose.yml ${MINDWIKI_INSTALL_LOC}/
	install -C -m 0755 assets/mindwiki.sh ${MINDWIKI_INSTALL_LOC}/
	ln -fs ${MINDWIKI_INSTALL_LOC}/mindwiki.sh ${MINDWIKI_BIN_DIR}/mindwiki-up
	ln -fs ${MINDWIKI_INSTALL_LOC}/mindwiki.sh ${MINDWIKI_BIN_DIR}/mindwiki-down

container-build:
	docker build --build-arg EXTRA_PACKAGES="bash-completion" -t 'ravenoak/mymindwiki:latest' .

requirements:
	pipenv lock -r --dev-only > dev-requirements.txt
	pipenv lock -r > requirements.txt
