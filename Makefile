
# Rolf Niepraschk, 2015-02-24, Rolf.Niepraschk@ptb.de

MAIN = relayServer
VERSION = $(shell awk -F"'" '/VERSION:/ {print $$2}' config.js)
RELEASE = 2 # >0!
LICENSE = "???"
GROUP = "Productivity/Networking/Web/Servers"
SUMMARY = "Nodejs-basierte http-Server für Messaufgaben"
DESCRIPTION = $(SUMMARY)
PACKAGER = "Rolf Niepraschk"
#BUILDARCH = $(shell arch)
BUILDARCH = "noarch"
###JS_TEST = relay-add-test.js
JS_SOURCE = $(wildcard *.js)
###JS_SOURCE := $(filter-out $(JS_TEST),$(JS_SOURCE))
NODE_MODULES = node_modules
BUILD_ROOT = dist
SPEC_FILE = $(MAIN).spec
DOC_CMD=/usr/bin/dox-foundation
DOC_DIR=$(MAIN)
DOC_SRC=.,test
DOC_IGNORE=tmp,node_modules,coverage
DOC_DB=vaclab_doc
DOC_SERVER=a73434.berlin.ptb.de
DOC_SERVER_PORT=5984
DOC_DB_URL=http://$(DOC_SERVER):$(DOC_SERVER_PORT)/$(DOC_DB)
ARCHIVNAME = $(MAIN)-$(shell date +%Y-%m-%d).zip
COMPACT=curl -H "Content-Type: application/json" -X POST

ARCH=$(shell arch)
INSTALL_DIRS_PARENT = $$HOME/couch-apps/repos/
INSTALL_DIRS_ROOT = $(INSTALL_DIRS_PARENT)_attachments/
OS_RELEASES = openSUSE_11.4  openSUSE_12.2  openSUSE_12.3  openSUSE_13.1  SLE_11_SP3
INSTALL_DIRS = $(addsuffix /noarch, $(addprefix $(INSTALL_DIRS_ROOT), $(OS_RELEASES)))

### LANG=c date +"* %a %b %d %Y Rolf.Niepraschk@ptb.de"
### LANG=c date +"* %a %b %d %Y Rolf.Niepraschk@ptb.de" -d "2012-08-30"

rpm : spec
	rpmbuild --buildroot $(PWD)/$(BUILD_ROOT) -bb $(SPEC_FILE)

src_rpm : spec
	rpmbuild --buildroot $(PWD)/$(BUILD_ROOT) -bs $(SPEC_FILE)

dep : rpm
	alien --to-deb --scripts $(MAIN)-$(VERSION)-$(RELEASE).noarch.rpm
# erfordert root-Privilegien !?

spec : dist
	@LANG=de_DE.UTF-8 echo "Summary: $(SUMMARY)" > $(SPEC_FILE)
	@echo "Name: $(MAIN)" >> $(SPEC_FILE)
	@echo "Version: $(VERSION)" >> $(SPEC_FILE)
	@echo "Release: $(RELEASE)" >> $(SPEC_FILE)
	@echo "License: $(LICENSE)" >> $(SPEC_FILE)
	@echo "Group: $(GROUP)" >> $(SPEC_FILE)
	@echo "BuildArch: $(BUILDARCH)" >> $(SPEC_FILE)
	@echo "Packager: $(PACKAGER)" >> $(SPEC_FILE)
	@echo "AutoReqProv: no" >> $(SPEC_FILE)
	@echo "Requires: nodejs" >> $(SPEC_FILE)
	@echo "%{?systemd_requires}" >> $(SPEC_FILE)
	@echo "" >> $(SPEC_FILE)
	@echo "%description" >> $(SPEC_FILE)
	@echo "$(DESCRIPTION)" >> $(SPEC_FILE)
	@echo "" >> $(SPEC_FILE)
	@echo "%pre" >> $(SPEC_FILE)
	@echo "%service_add_pre %{name}.service" >> $(SPEC_FILE)
	@echo "" >> $(SPEC_FILE)
	@echo "%post" >> $(SPEC_FILE)
	@echo "%service_add_post %{name}.service" >> $(SPEC_FILE)
	@echo "" >> $(SPEC_FILE)
	@echo "%preun" >> $(SPEC_FILE)
	@echo "%service_del_preun %{name}.service" >> $(SPEC_FILE)
	@echo "" >> $(SPEC_FILE)
	@echo "%postun" >> $(SPEC_FILE)
	@echo "%service_del_postun %{name}.service" >> $(SPEC_FILE)
	@echo "" >> $(SPEC_FILE)
	@echo "%files" >> $(SPEC_FILE)
	@find $(BUILD_ROOT)/* -type d -name '*' -print | sed 's/^$(BUILD_ROOT)/%dir /' \
    >> $(SPEC_FILE)
# mindestens hier sind quotes bei Dateinamen nötig
	@find $(BUILD_ROOT) -type f -name '*' -exec echo '"{}" ' \; | \
	  sed -e 's/$(BUILD_ROOT)//' >> $(SPEC_FILE)
	@echo -n "%config(noreplace) " >> $(SPEC_FILE)
	@echo "" >> $(SPEC_FILE)
	@echo "%changelog" >> $(SPEC_FILE)
	@cat CHANGES >> $(SPEC_FILE)

dist : rm_buildroot vxi11
#	git pull
#	npm install
	mkdir -p $(BUILD_ROOT)/etc/init.d
	mkdir -p $(BUILD_ROOT)/usr/local/bin
	mkdir -p $(BUILD_ROOT)/usr/sbin
	mkdir -p $(BUILD_ROOT)/usr/local/share/vaclab/nodejs
	mkdir -p $(BUILD_ROOT)/usr/lib/node_modules
	mkdir -p $(BUILD_ROOT)/usr/lib/systemd/system
	mkdir -p $(BUILD_ROOT)/etc/init
	cp -p vlLogging $(BUILD_ROOT)/usr/local/bin/
	cp -p $(JS_SOURCE) $(BUILD_ROOT)/usr/local/share/vaclab/nodejs/
	cp -pLr $(NODE_MODULES) $(BUILD_ROOT)/usr/local/share/vaclab/nodejs/
	cp -p $(MAIN).service $(BUILD_ROOT)/usr/lib/systemd/system/
	cp -p $(MAIN).conf $(BUILD_ROOT)/etc/init/  # "upstart" (Ubuntu)

docs :
	rm -rf $(DOC_DIR) ; mkdir $(DOC_DIR)
	$(DOC_CMD) --debug --title "$(DOC_DIR) $(VERSION)" \
	  --source $(DOC_SRC) --target $(DOC_DIR) --ignore $(DOC_IGNORE)

docs-install : docs
	mv $(DOC_DIR) _attachments
	erica -v --is-ddoc false --docid $(DOC_DIR) push $(DOC_DB_URL)
	$(COMPACT) $(DOC_DB_URL)/_compact
	rm -rf $(DOC_DIR) _attachments

clean : rm_buildroot
	$(MAKE) -C $(VXI11_SRC) clean
	$(RM) $(SPEC_FILE)

rm_buildroot :
	rm -rf $(BUILD_ROOT)

arch :
	@ zip $(ARCHIVNAME) $(JS_SOURCE) Makefile CHANGES \
	  nodejsServers vxiTransceiver NodejsServers \
	  $(VXI11_SRC)/unescape.cpp $(VXI11_SRC)/vxi11_svc.c \
	  $(VXI11_SRC)/vxi11_user.cc $(VXI11_SRC)/vxi11_clnt.c \
	  $(VXI11_SRC)/vxi11_transceiver.cc $(VXI11_SRC)/vxi11_xdr.c \
	  $(VXI11_SRC)/unescape.h $(VXI11_SRC)/vxi11.h \
	  $(VXI11_SRC)/vxi11_user.h $(VXI11_SRC)/vxi11.x \
	  $(VXI11_SRC)/Makefile
	@echo
	@echo $(ARCHIVNAME)

debug :
	@echo $(VERSION)
	@echo $(JS_SOURCE)
	@echo $(INSTALL_DIRS)

install : rpm
	@echo "=== INSTALL ==="
	@target=$(shell ls -1t $$HOME/rpmbuild/RPMS/noarch/*.rpm | head -1) ; \
	$(foreach i, $(INSTALL_DIRS), cp -pv $$target $i ;)
	make -C $(INSTALL_DIRS_PARENT)

.PHONY : dist vxi11 arch clean rpm src_rpm spec
