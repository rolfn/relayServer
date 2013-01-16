
# Rolf Niepraschk, 2013-01-16, Rolf.Niepraschk@ptb.de

MAIN = vaclabServers
VERSION = $(shell awk -F"'" '/VERSION:/ {print $$2}' config.js)
RELEASE = 1 # >0!
LICENSE = "???"
GROUP = "Productivity/Networking/Web/Servers" 
SUMMARY = "Nodejs-basierte http-Server für Messaufgaben"
DESCRIPTION = $(SUMMARY)
PACKAGER = "Rolf Niepraschk"
BUILDARCH = $(shell arch)
JS_SOURCE = $(wildcard *.js)
BUILD_ROOT = dist
SPEC_FILE = $(MAIN).spec
VXI11_SRC = vxi11
DOC_CMD=/usr/bin/dox-foundation
DOC_DIR=_attachments
DOC_SRC=doc_src
DOC_DB=vaclab_doc
DOC_SERVER=a73434.berlin.ptb.de
ARCHIVNAME = $(MAIN)-$(shell date +%Y-%m-%d).zip
COMPACT=curl -H "Content-Type: application/json" -X POST

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
	@echo "" >> $(SPEC_FILE)
	@echo "%changelog" >> $(SPEC_FILE)
	@cat CHANGES >> $(SPEC_FILE)

# texcaller dazu?
dist : rm_buildroot vxi11
	mkdir -p $(BUILD_ROOT)/etc/init.d
	mkdir -p $(BUILD_ROOT)/usr/local/bin
	mkdir -p $(BUILD_ROOT)/usr/sbin
	mkdir -p $(BUILD_ROOT)/usr/local/share/vaclab/nodejs
	mkdir -p $(BUILD_ROOT)/usr/lib/node_modules
	cp -p nodejsServers vxiTransceiver $(BUILD_ROOT)/usr/local/bin/
	cp -p $(VXI11_SRC)/vxi11_transceiver $(BUILD_ROOT)/usr/local/bin/
	cp -p $(JS_SOURCE) $(BUILD_ROOT)/usr/local/share/vaclab/nodejs/
	cp -p NodejsServers $(BUILD_ROOT)/etc/init.d/
	cp -pr /usr/lib/node_modules/request $(BUILD_ROOT)/usr/lib/node_modules/
	cp -pr /usr/lib/node_modules/ldapjs $(BUILD_ROOT)/usr/lib/node_modules/
	cp -pr /usr/lib/node_modules/buffertools $(BUILD_ROOT)/usr/lib/node_modules/
	cd $(BUILD_ROOT)/usr/sbin/ && \
    ln -sf ../../etc/init.d/NodejsServers rcNodejsServers

vxi11 : $(VXI11_SRC)/vxi11_transceiver

$(VXI11_SRC)/vxi11_transceiver : 
	$(MAKE) -C $(VXI11_SRC)

docs : $(DOC_DIR)/index.html

$(DOC_SRC) : $(JS_SOURCE)
	@mkdir -p "$@"
	@cp $+ $@

$(DOC_DIR)/index.html : $(DOC_SRC)
	@mkdir -p "$(DOC_DIR)"
	$(DOC_CMD) --debug --title "$(MAIN)" --source $(DOC_SRC) --target "$(DOC_DIR)"
	@$(RM) -r $(DOC_SRC)

docs-install : docs
	echo $(MAIN) > _id
	erica -v --docid $(MAIN) push http://$(DOC_SERVER):5984/$(DOC_DB)
	$(COMPACT) http://$(DOC_SERVER):5984/$(DOC_DB)/_compact
  
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

.PHONY : dist vxi11 arch clean rpm src_rpm spec 
