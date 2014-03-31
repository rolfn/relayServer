
# Rolf Niepraschk, 2014-03-31, Rolf.Niepraschk@ptb.de

MAIN = vaclabServers
VERSION = $(shell awk -F"'" '/VERSION:/ {print $$2}' config.js)
RELEASE = 2 # >0!
LICENSE = "???"
GROUP = "Productivity/Networking/Web/Servers"
SUMMARY = "Nodejs-basierte http-Server für Messaufgaben"
DESCRIPTION = $(SUMMARY)
PACKAGER = "Rolf Niepraschk"
BUILDARCH = $(shell arch)
JS_TEST = relay-add-test.js
JS_SOURCE = $(wildcard *.js)
JS_SOURCE := $(filter-out $(JS_TEST),$(JS_SOURCE))
CONFIG = gitlabhook.conf
NODE_MODULES = node_modules
BUILD_ROOT = dist
SPEC_FILE = $(MAIN).spec
VXI11_SRC = vxi11
DOC_CMD=/usr/bin/dox-foundation
DOC_DIR=_attachments
DOC_SRC=doc_src
DOC_DB=vaclab_doc
DOC_SERVER=a73434.berlin.ptb.de
DOC_SERVER_PORT=5984
DOC_DB_URL=http://$(DOC_SERVER):$(DOC_SERVER_PORT)/$(DOC_DB)
ARCHIVNAME = $(MAIN)-$(shell date +%Y-%m-%d).zip
COMPACT=curl -H "Content-Type: application/json" -X POST

ARCH=$(shell arch)
INSTALL_DIRS_ROOT = $$HOME/couch-apps/repos/_attachments/
OS_RELEASES = openSUSE_11.4  openSUSE_12.2  openSUSE_12.3  openSUSE_13.1  SLE_11_SP3
INSTALL_DIRS = $(addsuffix /$(ARCH), $(addprefix $(INSTALL_DIRS_ROOT), $(OS_RELEASES)))

### LANG=c date +"* %a %b %d %Y Rolf.Niepraschk@ptb.de"
### LANG=c date +"* %a %b %d %Y Rolf.Niepraschk@ptb.de" -d "2012-08-30"

rpm : spec
	rpmbuild --buildroot $(PWD)/$(BUILD_ROOT) -bb $(SPEC_FILE)

src_rpm : spec
	rpmbuild --buildroot $(PWD)/$(BUILD_ROOT) -bs $(SPEC_FILE)

spec : dist
	@echo "Summary: $(SUMMARY)" > $(SPEC_FILE)
	@echo "Name: $(MAIN)" >> $(SPEC_FILE)
	@echo "Version: $(VERSION)" >> $(SPEC_FILE)
	@echo "Release: $(RELEASE)" >> $(SPEC_FILE)
	@echo "License: $(LICENSE)" >> $(SPEC_FILE)
	@echo "Group: $(GROUP)" >> $(SPEC_FILE)
	@echo "BuildArch: $(BUILDARCH)" >> $(SPEC_FILE)
	@echo "Packager: $(PACKAGER)" >> $(SPEC_FILE)
	@echo "AutoReqProv: no" >> $(SPEC_FILE)
	@echo "Requires: nodejs" >> $(SPEC_FILE)
	@echo "" >> $(SPEC_FILE)
	@echo "%description" >> $(SPEC_FILE)
	@echo "$(DESCRIPTION)" >> $(SPEC_FILE)
	@echo "" >> $(SPEC_FILE)
	@echo "%files" >> $(SPEC_FILE)
	@find $(BUILD_ROOT)/* -type d -name '*' -print | sed 's/^$(BUILD_ROOT)/%dir /' \
    >> $(SPEC_FILE)
	@find $(BUILD_ROOT) -type f -name '*' -print | sed 's/^$(BUILD_ROOT)//' \
    >> $(SPEC_FILE)
	@find $(BUILD_ROOT) -type l -name '*' -print | sed 's/^$(BUILD_ROOT)//' \
    >> $(SPEC_FILE)
	@echo -n "%config(noreplace) " >> $(SPEC_FILE)
	@find $(BUILD_ROOT) -type f -name "$(CONFIG)" | sed 's/^$(BUILD_ROOT)//' \
    >> $(SPEC_FILE)
	@echo "" >> $(SPEC_FILE)
	@echo "%changelog" >> $(SPEC_FILE)
	@cat CHANGES >> $(SPEC_FILE)

# texcaller dazu?
dist : rm_buildroot vxi11
	git pull
#	npm install request nodemailer gitlabhook temp
	mkdir -p $(BUILD_ROOT)/etc/init.d
	mkdir -p $(BUILD_ROOT)/usr/local/bin
	mkdir -p $(BUILD_ROOT)/usr/sbin
	mkdir -p $(BUILD_ROOT)/usr/local/share/vaclab/nodejs
	mkdir -p $(BUILD_ROOT)/usr/lib/node_modules
	mkdir -p $(BUILD_ROOT)/usr/lib/systemd/system
	cp -p vxiTransceiver vlLogging $(BUILD_ROOT)/usr/local/bin/
##	cp -p nodejsServers vxiTransceiver vlLogging $(BUILD_ROOT)/usr/local/bin/
	cp -p $(VXI11_SRC)/vxi11_transceiver $(BUILD_ROOT)/usr/local/bin/
	cp -p $(JS_SOURCE) $(BUILD_ROOT)/usr/local/share/vaclab/nodejs/
	cp -pLr $(NODE_MODULES) $(BUILD_ROOT)/usr/local/share/vaclab/nodejs/
	cp -p $(CONFIG) $(BUILD_ROOT)/usr/local/share/vaclab/nodejs/
	cp -p NodejsServers.service $(BUILD_ROOT)/usr/lib/systemd/system/
##	cp -p NodejsServers $(BUILD_ROOT)/etc/init.d/
##	cp -pr /usr/lib/node_modules/request $(BUILD_ROOT)/usr/lib/node_modules/
##	cp -pr /usr/lib/node_modules/ldapjs $(BUILD_ROOT)/usr/lib/node_modules/
##	cp -pr /usr/lib/node_modules/buffertools $(BUILD_ROOT)/usr/lib/node_modules/
##	cp -pr /usr/lib/node_modules/nodemailer $(BUILD_ROOT)/usr/lib/node_modules/
##	cd $(BUILD_ROOT)/usr/sbin/ && \
##    ln -sf ../../etc/init.d/NodejsServers rcNodejsServers

vxi11 : $(VXI11_SRC)/vxi11_transceiver

$(VXI11_SRC)/vxi11_transceiver :
	$(MAKE) -C $(VXI11_SRC)

docs : $(DOC_DIR)/index.html

# Umkopieren, damit Rekursion von "dox-foundation" unschädlich ist.
$(DOC_SRC) : $(JS_SOURCE) $(JS_TEST)
	@mkdir -p "$@"
	cp $+ $@

$(DOC_DIR)/index.html : $(DOC_SRC)
	echo "###############################################"
	@mkdir -p "$(DOC_DIR)"
	$(DOC_CMD) --debug --title "$(MAIN) (ver. $(VERSION))" --source $(DOC_SRC) \
	  --target "$(DOC_DIR)"
	@$(RM) -r $(DOC_SRC)

docs-install : docs
	echo $(MAIN) > _id
	erica -v --is-ddoc --docid $(MAIN) push $(DOC_DB_URL)
	$(COMPACT) $(DOC_DB_URL)/_compact
	$(RM) $(DOC_DIR)/*.js.html $(DOC_DIR)/index.html

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
	@target=$(shell ls -1t $$HOME/rpmbuild/RPMS/$(ARCH)/*.rpm | head -1) ; \
	$(foreach i, $(INSTALL_DIRS), cp -pv $$target $i ;)

.PHONY : dist vxi11 arch clean rpm src_rpm spec
