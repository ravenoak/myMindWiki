MINDWIKI_INSTALL_LOC ?= ${HOME}/.local/share/mindwiki
MINDWIKI_BIN_DIR ?= ${HOME}/.local/bin
.PHONY: install

${MINDWIKI_INSTALL_LOC}:
	mkdir -p ${MINDWIKI_INSTALL_LOC}

install: ${MINDWIKI_INSTALL_LOC}
	cp dist/* ${MINDWIKI_INSTALL_LOC}/
	ln -s ${MINDWIKI_INSTALL_LOC}/mindwiki.sh ${MINDWIKI_BIN_DIR}/mindwiki-up
	ln -s ${MINDWIKI_INSTALL_LOC}/mindwiki.sh ${MINDWIKI_BIN_DIR}/mindwiki-down
