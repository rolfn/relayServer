Summary: Nodejs-basierte http-Server für Messaufgaben
Name: vaclabServers
Version: 7.2
Release: 1 
License: ???
Group: Productivity/Networking/Web/Servers 
BuildArch: i686
Packager: Rolf Niepraschk
AutoReqProv: no
Requires: nodejs

%description
Nodejs-basierte http-Server für Messaufgaben

%files
%dir /etc
%dir /etc/init.d
%dir /usr
%dir /usr/lib
%dir /usr/lib/node_modules
%dir /usr/lib/node_modules/buffertools
%dir /usr/lib/node_modules/buffertools/build
%dir /usr/lib/node_modules/buffertools/build/Release
%dir /usr/lib/node_modules/buffertools/build/Release/.deps
%dir /usr/lib/node_modules/buffertools/build/Release/.deps/Release
%dir /usr/lib/node_modules/buffertools/build/Release/.deps/Release/obj.target
%dir /usr/lib/node_modules/buffertools/build/Release/.deps/Release/obj.target/buffertools
%dir /usr/lib/node_modules/buffertools/build/Release/obj.target
%dir /usr/lib/node_modules/buffertools/build/Release/obj.target/buffertools
%dir /usr/lib/node_modules/request
%dir /usr/lib/node_modules/request/vendor
%dir /usr/lib/node_modules/request/vendor/cookie
%dir /usr/lib/node_modules/request/tests
%dir /usr/lib/node_modules/request/tests/ssl
%dir /usr/lib/node_modules/request/tests/ssl/ca
%dir /usr/lib/node_modules/ldapjs
%dir /usr/lib/node_modules/ldapjs/docs
%dir /usr/lib/node_modules/ldapjs/docs/branding
%dir /usr/lib/node_modules/ldapjs/docs/branding/media
%dir /usr/lib/node_modules/ldapjs/docs/branding/media/js
%dir /usr/lib/node_modules/ldapjs/docs/branding/media/css
%dir /usr/lib/node_modules/ldapjs/tools
%dir /usr/lib/node_modules/ldapjs/tools/mk
%dir /usr/lib/node_modules/ldapjs/node_modules
%dir /usr/lib/node_modules/ldapjs/node_modules/.bin
%dir /usr/lib/node_modules/ldapjs/node_modules/buffertools
%dir /usr/lib/node_modules/ldapjs/node_modules/buffertools/build
%dir /usr/lib/node_modules/ldapjs/node_modules/buffertools/build/Release
%dir /usr/lib/node_modules/ldapjs/node_modules/buffertools/build/Release/.deps
%dir /usr/lib/node_modules/ldapjs/node_modules/buffertools/build/Release/.deps/Release
%dir /usr/lib/node_modules/ldapjs/node_modules/buffertools/build/Release/.deps/Release/obj.target
%dir /usr/lib/node_modules/ldapjs/node_modules/buffertools/build/Release/.deps/Release/obj.target/buffertools
%dir /usr/lib/node_modules/ldapjs/node_modules/buffertools/build/Release/obj.target
%dir /usr/lib/node_modules/ldapjs/node_modules/buffertools/build/Release/obj.target/buffertools
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/tools
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/tools/mk
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/node_modules
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/node_modules/extsprintf
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/node_modules/extsprintf/lib
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/node_modules/extsprintf/examples
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/lib
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/examples
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/lib
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/examples
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/lib
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/deps
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/javascriptlint
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/javascriptlint/pyspidermonkey
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/javascriptlint/pyspidermonkey_
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/deps/jsstyle
%dir /usr/lib/node_modules/ldapjs/node_modules/pooling/test
%dir /usr/lib/node_modules/ldapjs/node_modules/nopt
%dir /usr/lib/node_modules/ldapjs/node_modules/nopt/node_modules
%dir /usr/lib/node_modules/ldapjs/node_modules/nopt/node_modules/abbrev
%dir /usr/lib/node_modules/ldapjs/node_modules/nopt/node_modules/abbrev/lib
%dir /usr/lib/node_modules/ldapjs/node_modules/nopt/lib
%dir /usr/lib/node_modules/ldapjs/node_modules/nopt/examples
%dir /usr/lib/node_modules/ldapjs/node_modules/nopt/bin
%dir /usr/lib/node_modules/ldapjs/node_modules/assert-plus
%dir /usr/lib/node_modules/ldapjs/node_modules/bunyan
%dir /usr/lib/node_modules/ldapjs/node_modules/bunyan/tools
%dir /usr/lib/node_modules/ldapjs/node_modules/bunyan/lib
%dir /usr/lib/node_modules/ldapjs/node_modules/bunyan/examples
%dir /usr/lib/node_modules/ldapjs/node_modules/bunyan/bin
%dir /usr/lib/node_modules/ldapjs/node_modules/bunyan/test
%dir /usr/lib/node_modules/ldapjs/node_modules/bunyan/test/corpus
%dir /usr/lib/node_modules/ldapjs/node_modules/dtrace-provider
%dir /usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/libusdt
%dir /usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/build
%dir /usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/build/Release
%dir /usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/build/Release/.deps
%dir /usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/build/Release/.deps/Release
%dir /usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/build/Release/.deps/Release/obj.target
%dir /usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/build/Release/obj.target
%dir /usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/test
%dir /usr/lib/node_modules/ldapjs/node_modules/asn1
%dir /usr/lib/node_modules/ldapjs/node_modules/asn1/lib
%dir /usr/lib/node_modules/ldapjs/node_modules/asn1/lib/ber
%dir /usr/lib/node_modules/ldapjs/node_modules/asn1/tst
%dir /usr/lib/node_modules/ldapjs/node_modules/asn1/tst/ber
%dir /usr/lib/node_modules/ldapjs/lib
%dir /usr/lib/node_modules/ldapjs/lib/client
%dir /usr/lib/node_modules/ldapjs/lib/errors
%dir /usr/lib/node_modules/ldapjs/lib/messages
%dir /usr/lib/node_modules/ldapjs/lib/controls
%dir /usr/lib/node_modules/ldapjs/lib/filters
%dir /usr/lib/node_modules/ldapjs/deps
%dir /usr/lib/node_modules/ldapjs/deps/javascriptlint
%dir /usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey
%dir /usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src
%dir /usr/lib/node_modules/ldapjs/deps/javascriptlint/javascriptlint
%dir /usr/lib/node_modules/ldapjs/deps/javascriptlint/javascriptlint/pyspidermonkey
%dir /usr/lib/node_modules/ldapjs/deps/javascriptlint/javascriptlint/pyspidermonkey_
%dir /usr/lib/node_modules/ldapjs/deps/jsstyle
%dir /usr/lib/node_modules/ldapjs/examples
%dir /usr/lib/node_modules/ldapjs/bin
%dir /usr/lib/node_modules/ldapjs/test
%dir /usr/lib/node_modules/ldapjs/test/messages
%dir /usr/lib/node_modules/ldapjs/test/controls
%dir /usr/lib/node_modules/ldapjs/test/filters
%dir /usr/sbin
%dir /usr/local
%dir /usr/local/share
%dir /usr/local/share/vaclab
%dir /usr/local/share/vaclab/nodejs
%dir /usr/local/bin
/usr/lib/node_modules/buffertools/buffertools.cc
/usr/lib/node_modules/buffertools/test.js
/usr/lib/node_modules/buffertools/wscript
/usr/lib/node_modules/buffertools/AUTHORS
/usr/lib/node_modules/buffertools/README.md
/usr/lib/node_modules/buffertools/.npmignore
/usr/lib/node_modules/buffertools/binding.gyp
/usr/lib/node_modules/buffertools/buffertools.js
/usr/lib/node_modules/buffertools/.mailmap
/usr/lib/node_modules/buffertools/build/buffertools.target.mk
/usr/lib/node_modules/buffertools/build/Release/linker.lock
/usr/lib/node_modules/buffertools/build/Release/.deps/Release/buffertools.node.d
/usr/lib/node_modules/buffertools/build/Release/.deps/Release/obj.target/buffertools.node.d
/usr/lib/node_modules/buffertools/build/Release/.deps/Release/obj.target/buffertools/buffertools.o.d
/usr/lib/node_modules/buffertools/build/Release/buffertools.node
/usr/lib/node_modules/buffertools/build/Release/obj.target/buffertools/buffertools.o
/usr/lib/node_modules/buffertools/build/Release/obj.target/buffertools.node
/usr/lib/node_modules/buffertools/build/config.gypi
/usr/lib/node_modules/buffertools/build/binding.Makefile
/usr/lib/node_modules/buffertools/build/Makefile
/usr/lib/node_modules/buffertools/package.json
/usr/lib/node_modules/buffertools/BoyerMoore.h
/usr/lib/node_modules/request/aws2.js
/usr/lib/node_modules/request/main.js
/usr/lib/node_modules/request/forever.js
/usr/lib/node_modules/request/uuid.js
/usr/lib/node_modules/request/vendor/cookie/index.js
/usr/lib/node_modules/request/vendor/cookie/jar.js
/usr/lib/node_modules/request/README.md
/usr/lib/node_modules/request/LICENSE
/usr/lib/node_modules/request/tests/ssl/test.crt
/usr/lib/node_modules/request/tests/ssl/npm-ca.crt
/usr/lib/node_modules/request/tests/ssl/ca/ca.csr
/usr/lib/node_modules/request/tests/ssl/ca/server.csr
/usr/lib/node_modules/request/tests/ssl/ca/server.key
/usr/lib/node_modules/request/tests/ssl/ca/server.js
/usr/lib/node_modules/request/tests/ssl/ca/ca.cnf
/usr/lib/node_modules/request/tests/ssl/ca/ca.srl
/usr/lib/node_modules/request/tests/ssl/ca/server.crt
/usr/lib/node_modules/request/tests/ssl/ca/server.cnf
/usr/lib/node_modules/request/tests/ssl/ca/ca.crl
/usr/lib/node_modules/request/tests/ssl/ca/ca.crt
/usr/lib/node_modules/request/tests/ssl/ca/ca.key
/usr/lib/node_modules/request/tests/ssl/test.key
/usr/lib/node_modules/request/tests/test-tunnel.js
/usr/lib/node_modules/request/tests/test-body.js
/usr/lib/node_modules/request/tests/test-qs.js
/usr/lib/node_modules/request/tests/test-defaults.js
/usr/lib/node_modules/request/tests/run.js
/usr/lib/node_modules/request/tests/server.js
/usr/lib/node_modules/request/tests/test-redirect.js
/usr/lib/node_modules/request/tests/test-oauth.js
/usr/lib/node_modules/request/tests/googledoodle.png
/usr/lib/node_modules/request/tests/test-httpModule.js
/usr/lib/node_modules/request/tests/squid.conf
/usr/lib/node_modules/request/tests/test-toJSON.js
/usr/lib/node_modules/request/tests/test-https.js
/usr/lib/node_modules/request/tests/test-https-strict.js
/usr/lib/node_modules/request/tests/test-headers.js
/usr/lib/node_modules/request/tests/test-params.js
/usr/lib/node_modules/request/tests/test-pipes.js
/usr/lib/node_modules/request/tests/test-s3.js
/usr/lib/node_modules/request/tests/test-pool.js
/usr/lib/node_modules/request/tests/test-errors.js
/usr/lib/node_modules/request/tests/test-proxy.js
/usr/lib/node_modules/request/tests/test-timeout.js
/usr/lib/node_modules/request/tests/test-cookie.js
/usr/lib/node_modules/request/tests/test-cookiejar.js
/usr/lib/node_modules/request/tunnel.js
/usr/lib/node_modules/request/oauth.js
/usr/lib/node_modules/request/mimetypes.js
/usr/lib/node_modules/request/aws.js
/usr/lib/node_modules/request/package.json
/usr/lib/node_modules/ldapjs/docs/errors.md
/usr/lib/node_modules/ldapjs/docs/filters.md
/usr/lib/node_modules/ldapjs/docs/dn.md
/usr/lib/node_modules/ldapjs/docs/guide.md
/usr/lib/node_modules/ldapjs/docs/branding/media/js/jquery-1.4.2.min.js
/usr/lib/node_modules/ldapjs/docs/branding/media/css/style.css
/usr/lib/node_modules/ldapjs/docs/branding/footer.html.in
/usr/lib/node_modules/ldapjs/docs/branding/header.html.in
/usr/lib/node_modules/ldapjs/docs/index.md
/usr/lib/node_modules/ldapjs/docs/persistent_search.md
/usr/lib/node_modules/ldapjs/docs/examples.md
/usr/lib/node_modules/ldapjs/docs/server.md
/usr/lib/node_modules/ldapjs/docs/client.md
/usr/lib/node_modules/ldapjs/.dir-locals.el
/usr/lib/node_modules/ldapjs/tools/jsl.node.conf
/usr/lib/node_modules/ldapjs/tools/mk/Makefile.defs
/usr/lib/node_modules/ldapjs/tools/mk/Makefile.targ
/usr/lib/node_modules/ldapjs/tools/mk/Makefile.deps
/usr/lib/node_modules/ldapjs/tools/jsstyle.conf
/usr/lib/node_modules/ldapjs/node_modules/buffertools/buffertools.cc
/usr/lib/node_modules/ldapjs/node_modules/buffertools/test.js
/usr/lib/node_modules/ldapjs/node_modules/buffertools/wscript
/usr/lib/node_modules/ldapjs/node_modules/buffertools/AUTHORS
/usr/lib/node_modules/ldapjs/node_modules/buffertools/README.md
/usr/lib/node_modules/ldapjs/node_modules/buffertools/.npmignore
/usr/lib/node_modules/ldapjs/node_modules/buffertools/binding.gyp
/usr/lib/node_modules/ldapjs/node_modules/buffertools/buffertools.js
/usr/lib/node_modules/ldapjs/node_modules/buffertools/.mailmap
/usr/lib/node_modules/ldapjs/node_modules/buffertools/build/buffertools.target.mk
/usr/lib/node_modules/ldapjs/node_modules/buffertools/build/Release/linker.lock
/usr/lib/node_modules/ldapjs/node_modules/buffertools/build/Release/.deps/Release/buffertools.node.d
/usr/lib/node_modules/ldapjs/node_modules/buffertools/build/Release/.deps/Release/obj.target/buffertools.node.d
/usr/lib/node_modules/ldapjs/node_modules/buffertools/build/Release/.deps/Release/obj.target/buffertools/buffertools.o.d
/usr/lib/node_modules/ldapjs/node_modules/buffertools/build/Release/buffertools.node
/usr/lib/node_modules/ldapjs/node_modules/buffertools/build/Release/obj.target/buffertools/buffertools.o
/usr/lib/node_modules/ldapjs/node_modules/buffertools/build/Release/obj.target/buffertools.node
/usr/lib/node_modules/ldapjs/node_modules/buffertools/build/config.gypi
/usr/lib/node_modules/ldapjs/node_modules/buffertools/build/binding.Makefile
/usr/lib/node_modules/ldapjs/node_modules/buffertools/build/Makefile
/usr/lib/node_modules/ldapjs/node_modules/buffertools/package.json
/usr/lib/node_modules/ldapjs/node_modules/buffertools/BoyerMoore.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/.dir-locals.el
/usr/lib/node_modules/ldapjs/node_modules/pooling/tools/jsl.node.conf
/usr/lib/node_modules/ldapjs/node_modules/pooling/tools/mk/Makefile.defs
/usr/lib/node_modules/ldapjs/node_modules/pooling/tools/mk/Makefile.targ
/usr/lib/node_modules/ldapjs/node_modules/pooling/tools/mk/Makefile.deps
/usr/lib/node_modules/ldapjs/node_modules/pooling/tools/jsstyle.conf
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/Makefile.targ
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/jsl.node.conf
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/Makefile.targ
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/jsl.node.conf
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/node_modules/extsprintf/Makefile.targ
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/node_modules/extsprintf/jsl.node.conf
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/node_modules/extsprintf/Makefile.deps
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/node_modules/extsprintf/README.md
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/node_modules/extsprintf/lib/extsprintf.js
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/node_modules/extsprintf/LICENSE
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/node_modules/extsprintf/Makefile
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/node_modules/extsprintf/examples/simple.js
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/node_modules/extsprintf/.gitmodules
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/node_modules/extsprintf/package.json
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/Makefile.deps
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/README.md
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/.npmignore
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/lib/verror.js
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/LICENSE
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/Makefile
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/examples/missingcause.js
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/examples/simple.js
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/.gitmodules
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/node_modules/verror/package.json
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/Makefile.deps
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/README.md
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/.npmignore
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/lib/vasync.js
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/LICENSE
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/Makefile
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/examples/foreach-parallel.js
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/examples/queue-stat.js
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/examples/pipeline.js
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/examples/queue-serializer.js
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/examples/nofail.js
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/examples/parallel.js
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/.gitmodules
/usr/lib/node_modules/ldapjs/node_modules/pooling/node_modules/vasync/package.json
/usr/lib/node_modules/ldapjs/node_modules/pooling/README.md
/usr/lib/node_modules/ldapjs/node_modules/pooling/.npmignore
/usr/lib/node_modules/ldapjs/node_modules/pooling/lib/pool.js
/usr/lib/node_modules/ldapjs/node_modules/pooling/lib/index.js
/usr/lib/node_modules/ldapjs/node_modules/pooling/Makefile
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/README
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jstypes.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jspubtd.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsinterp.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsprf.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsOS240.def
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsfile.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsgc.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsdbgapi.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsify.pl
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jskeyword.tbl
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsfun.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsprf.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsapi.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsatom.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsdate.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsscope.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jslock.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsatom.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/win32.order
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsotypes.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/plify_jsdhash.sed
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsprvtd.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsregexp.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/SpiderMonkey.rsp
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsiter.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jslog2.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/prmjtime.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsopcode.tbl
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsexn.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsosdep.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsfun.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsarray.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsstr.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsregexp.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsinterp.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsdate.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jslong.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/prmjtime.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsfile.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jscntxt.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsemit.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jshash.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/resource.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jskwgen.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsapi.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsscan.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsmath.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/js.msg
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsobj.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsdtoa.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsstddef.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsnum.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsbool.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jshash.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsdtoa.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsfile.msg
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsparse.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsdhash.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsxdrapi.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/perfect.js
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsscript.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsutil.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsiter.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsdhash.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsscan.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jscompat.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jscpucfg.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsopcode.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsarray.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/Y.js
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsscope.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/Makefile
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jslocko.asm
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jslock.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsmath.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jscpucfg.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsutil.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsdbgapi.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsopcode.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsarena.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsproto.tbl
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsobj.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsnum.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsscript.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsclist.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsconfig.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsxml.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jslong.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsbit.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/js.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsbool.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsexn.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/js.mdp
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsstr.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsxml.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsgc.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsparse.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jscntxt.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/js.pkg
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsarena.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsemit.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/README.html
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsshell.msg
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jslibmath.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/spidermonkey/src/jsxdrapi.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/README.md
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/.npmignore
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/javascriptlint/pyspidermonkey/nodepos.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/javascriptlint/pyspidermonkey/tokens.tbl
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/javascriptlint/pyspidermonkey/nodepos.h
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/javascriptlint/pyspidermonkey/pyspidermonkey.c
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/javascriptlint/lint.py
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/javascriptlint/pyspidermonkey_/__init__.py
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/javascriptlint/visitation.py
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/javascriptlint/jsparse.py
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/javascriptlint/htmlparse.py
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/javascriptlint/conf.py
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/javascriptlint/jsl
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/javascriptlint/util.py
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/javascriptlint/jsl.py
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/javascriptlint/fs.py
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/javascriptlint/spidermonkey.py
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/javascriptlint/__init__.py
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/javascriptlint/warnings.py
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/Makefile
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/javascriptlint/COPYING
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/jsstyle/README.md
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/jsstyle/.npmignore
/usr/lib/node_modules/ldapjs/node_modules/pooling/deps/jsstyle/jsstyle
/usr/lib/node_modules/ldapjs/node_modules/pooling/.gitmodules
/usr/lib/node_modules/ldapjs/node_modules/pooling/package.json
/usr/lib/node_modules/ldapjs/node_modules/pooling/test/helper.js
/usr/lib/node_modules/ldapjs/node_modules/pooling/test/pool.test.js
/usr/lib/node_modules/ldapjs/node_modules/nopt/node_modules/abbrev/README.md
/usr/lib/node_modules/ldapjs/node_modules/nopt/node_modules/abbrev/lib/abbrev.js
/usr/lib/node_modules/ldapjs/node_modules/nopt/node_modules/abbrev/LICENSE
/usr/lib/node_modules/ldapjs/node_modules/nopt/node_modules/abbrev/package.json
/usr/lib/node_modules/ldapjs/node_modules/nopt/README.md
/usr/lib/node_modules/ldapjs/node_modules/nopt/.npmignore
/usr/lib/node_modules/ldapjs/node_modules/nopt/lib/nopt.js
/usr/lib/node_modules/ldapjs/node_modules/nopt/LICENSE
/usr/lib/node_modules/ldapjs/node_modules/nopt/examples/my-program.js
/usr/lib/node_modules/ldapjs/node_modules/nopt/package.json
/usr/lib/node_modules/ldapjs/node_modules/nopt/bin/nopt.js
/usr/lib/node_modules/ldapjs/node_modules/assert-plus/README.md
/usr/lib/node_modules/ldapjs/node_modules/assert-plus/assert.js
/usr/lib/node_modules/ldapjs/node_modules/assert-plus/package.json
/usr/lib/node_modules/ldapjs/node_modules/bunyan/foo.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/CHANGES.md
/usr/lib/node_modules/ldapjs/node_modules/bunyan/follow.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/TODO.md
/usr/lib/node_modules/ldapjs/node_modules/bunyan/tools/statsd-notes.txt
/usr/lib/node_modules/ldapjs/node_modules/bunyan/tools/timechild.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/tools/screenshot1.pxm
/usr/lib/node_modules/ldapjs/node_modules/bunyan/tools/timesrc.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/tools/cutarelease.py
/usr/lib/node_modules/ldapjs/node_modules/bunyan/tools/timeguard.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/tools/jsstyle
/usr/lib/node_modules/ldapjs/node_modules/bunyan/tools/screenshot1.png
/usr/lib/node_modules/ldapjs/node_modules/bunyan/AUTHORS
/usr/lib/node_modules/ldapjs/node_modules/bunyan/README.md
/usr/lib/node_modules/ldapjs/node_modules/bunyan/.npmignore
/usr/lib/node_modules/ldapjs/node_modules/bunyan/lib/bunyan.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/Makefile
/usr/lib/node_modules/ldapjs/node_modules/bunyan/examples/hi.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/examples/unstringifyable.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/examples/multi.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/examples/server.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/examples/level.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/examples/err.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/examples/handle-fs-error.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/examples/ringbuffer.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/examples/src.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/examples/raw-stream.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/bar.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/34.patch
/usr/lib/node_modules/ldapjs/node_modules/bunyan/package.json
/usr/lib/node_modules/ldapjs/node_modules/bunyan/bin/bunyan
/usr/lib/node_modules/ldapjs/node_modules/bunyan/test/cycles.test.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/test/cli.test.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/test/corpus/log1.log
/usr/lib/node_modules/ldapjs/node_modules/bunyan/test/corpus/withreq.log
/usr/lib/node_modules/ldapjs/node_modules/bunyan/test/corpus/extrafield.log
/usr/lib/node_modules/ldapjs/node_modules/bunyan/test/corpus/log2.log
/usr/lib/node_modules/ldapjs/node_modules/bunyan/test/corpus/log1.log.gz
/usr/lib/node_modules/ldapjs/node_modules/bunyan/test/corpus/all.log
/usr/lib/node_modules/ldapjs/node_modules/bunyan/test/corpus/simple.log
/usr/lib/node_modules/ldapjs/node_modules/bunyan/test/corpus/bogus.log
/usr/lib/node_modules/ldapjs/node_modules/bunyan/test/error-event.test.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/test/other-api.test.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/test/std-serializers.test.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/test/ringbuffer.test.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/test/log.test.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/test/raw-stream.test.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/test/buffer.test.js
/usr/lib/node_modules/ldapjs/node_modules/bunyan/test/ctor.test.js
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/CHANGES.md
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/dtrace-provider.js
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/TODO.md
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/libusdt-build.sh
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/dtrace_probe.cc
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/wscript
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/README.md
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/.npmignore
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/LICENCE
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/binding.gyp
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/libusdt/usdt_dof_file.c
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/libusdt/usdt_tracepoints_i386.s
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/libusdt/usdt_dof.c
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/libusdt/usdt_probe.c
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/libusdt/usdt_internal.h
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/libusdt/usdt_dof_sections.c
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/libusdt/usdt.h
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/libusdt/README.md
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/libusdt/.npmignore
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/libusdt/LICENCE
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/libusdt/Makefile
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/libusdt/usdt.c
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/libusdt/test_usdt.c
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/libusdt/README.md~
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/libusdt/usdt_tracepoints_x86_64.s
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/libusdt/test.pl
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/dtrace_provider.h
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/.gitmodules
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/README.md~
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/build/Release/DTraceProviderBindings.node
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/build/Release/linker.lock
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/build/Release/.deps/Release/DTraceProviderBindings.node.d
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/build/Release/.deps/Release/obj.target/DTraceProviderBindings.node.d
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/build/Release/.deps/Release/obj.target/libusdt.stamp.d
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/build/Release/obj.target/DTraceProviderBindings.node
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/build/Release/obj.target/libusdt.stamp
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/build/libusdt.target.mk
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/build/config.gypi
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/build/binding.Makefile
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/build/Makefile
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/build/DTraceProviderBindings.target.mk
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/dtrace_provider.cc
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/package.json
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/test/dtpc.js
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/test/enabled_again.js
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/test/enabled-disabled.js
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/test/not-enabled.js
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/test/dtp.js
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/test/enabled-again.js
/usr/lib/node_modules/ldapjs/node_modules/dtrace-provider/test/gc.js
/usr/lib/node_modules/ldapjs/node_modules/asn1/README.md
/usr/lib/node_modules/ldapjs/node_modules/asn1/.npmignore
/usr/lib/node_modules/ldapjs/node_modules/asn1/lib/ber/reader.js
/usr/lib/node_modules/ldapjs/node_modules/asn1/lib/ber/errors.js
/usr/lib/node_modules/ldapjs/node_modules/asn1/lib/ber/types.js
/usr/lib/node_modules/ldapjs/node_modules/asn1/lib/ber/writer.js
/usr/lib/node_modules/ldapjs/node_modules/asn1/lib/ber/index.js
/usr/lib/node_modules/ldapjs/node_modules/asn1/lib/index.js
/usr/lib/node_modules/ldapjs/node_modules/asn1/LICENSE
/usr/lib/node_modules/ldapjs/node_modules/asn1/tst/ber/reader.test.js
/usr/lib/node_modules/ldapjs/node_modules/asn1/tst/ber/writer.test.js
/usr/lib/node_modules/ldapjs/node_modules/asn1/package.json
/usr/lib/node_modules/ldapjs/README.md
/usr/lib/node_modules/ldapjs/.npmignore
/usr/lib/node_modules/ldapjs/lib/client/pool.js
/usr/lib/node_modules/ldapjs/lib/client/client.js
/usr/lib/node_modules/ldapjs/lib/client/index.js
/usr/lib/node_modules/ldapjs/lib/url.js
/usr/lib/node_modules/ldapjs/lib/server.js
/usr/lib/node_modules/ldapjs/lib/errors/index.js
/usr/lib/node_modules/ldapjs/lib/messages/bind_request.js
/usr/lib/node_modules/ldapjs/lib/messages/ext_request.js
/usr/lib/node_modules/ldapjs/lib/messages/search_reference.js
/usr/lib/node_modules/ldapjs/lib/messages/result.js
/usr/lib/node_modules/ldapjs/lib/messages/add_request.js
/usr/lib/node_modules/ldapjs/lib/messages/message.js
/usr/lib/node_modules/ldapjs/lib/messages/modify_request.js
/usr/lib/node_modules/ldapjs/lib/messages/bind_response.js
/usr/lib/node_modules/ldapjs/lib/messages/del_request.js
/usr/lib/node_modules/ldapjs/lib/messages/search_entry.js
/usr/lib/node_modules/ldapjs/lib/messages/moddn_response.js
/usr/lib/node_modules/ldapjs/lib/messages/compare_response.js
/usr/lib/node_modules/ldapjs/lib/messages/unbind_response.js
/usr/lib/node_modules/ldapjs/lib/messages/ext_response.js
/usr/lib/node_modules/ldapjs/lib/messages/modify_response.js
/usr/lib/node_modules/ldapjs/lib/messages/add_response.js
/usr/lib/node_modules/ldapjs/lib/messages/unbind_request.js
/usr/lib/node_modules/ldapjs/lib/messages/parser.js
/usr/lib/node_modules/ldapjs/lib/messages/del_response.js
/usr/lib/node_modules/ldapjs/lib/messages/abandon_response.js
/usr/lib/node_modules/ldapjs/lib/messages/abandon_request.js
/usr/lib/node_modules/ldapjs/lib/messages/search_request.js
/usr/lib/node_modules/ldapjs/lib/messages/index.js
/usr/lib/node_modules/ldapjs/lib/messages/compare_request.js
/usr/lib/node_modules/ldapjs/lib/messages/search_response.js
/usr/lib/node_modules/ldapjs/lib/messages/moddn_request.js
/usr/lib/node_modules/ldapjs/lib/attribute.js
/usr/lib/node_modules/ldapjs/lib/controls/paged_results_control.js
/usr/lib/node_modules/ldapjs/lib/controls/entry_change_notification_control.js
/usr/lib/node_modules/ldapjs/lib/controls/control.js
/usr/lib/node_modules/ldapjs/lib/controls/persistent_search_control.js
/usr/lib/node_modules/ldapjs/lib/controls/index.js
/usr/lib/node_modules/ldapjs/lib/protocol.js
/usr/lib/node_modules/ldapjs/lib/persistent_search.js
/usr/lib/node_modules/ldapjs/lib/filters/presence_filter.js
/usr/lib/node_modules/ldapjs/lib/filters/or_filter.js
/usr/lib/node_modules/ldapjs/lib/filters/ge_filter.js
/usr/lib/node_modules/ldapjs/lib/filters/approx_filter.js
/usr/lib/node_modules/ldapjs/lib/filters/not_filter.js
/usr/lib/node_modules/ldapjs/lib/filters/escape.js
/usr/lib/node_modules/ldapjs/lib/filters/equality_filter.js
/usr/lib/node_modules/ldapjs/lib/filters/ext_filter.js
/usr/lib/node_modules/ldapjs/lib/filters/substr_filter.js
/usr/lib/node_modules/ldapjs/lib/filters/filter.js
/usr/lib/node_modules/ldapjs/lib/filters/index.js
/usr/lib/node_modules/ldapjs/lib/filters/and_filter.js
/usr/lib/node_modules/ldapjs/lib/filters/le_filter.js
/usr/lib/node_modules/ldapjs/lib/dtrace.js
/usr/lib/node_modules/ldapjs/lib/dn.js
/usr/lib/node_modules/ldapjs/lib/change.js
/usr/lib/node_modules/ldapjs/lib/index.js
/usr/lib/node_modules/ldapjs/LICENSE
/usr/lib/node_modules/ldapjs/Makefile
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/README
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jstypes.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jspubtd.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsinterp.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsprf.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsOS240.def
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsfile.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsgc.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsdbgapi.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsify.pl
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jskeyword.tbl
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsfun.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsprf.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsapi.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsatom.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsdate.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsscope.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jslock.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsatom.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/win32.order
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsotypes.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/plify_jsdhash.sed
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsprvtd.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsregexp.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/SpiderMonkey.rsp
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsiter.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jslog2.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/prmjtime.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsopcode.tbl
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsexn.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsosdep.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsfun.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsarray.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsstr.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsregexp.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsinterp.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsdate.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jslong.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/prmjtime.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsfile.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jscntxt.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsemit.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jshash.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/resource.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jskwgen.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsapi.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsscan.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsmath.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/js.msg
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsobj.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsdtoa.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsstddef.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsnum.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsbool.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jshash.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsdtoa.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsfile.msg
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsparse.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsdhash.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsxdrapi.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/perfect.js
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsscript.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsutil.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsiter.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsdhash.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsscan.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jscompat.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jscpucfg.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsopcode.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsarray.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/Y.js
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsscope.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/Makefile
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jslocko.asm
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jslock.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsmath.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jscpucfg.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsutil.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsdbgapi.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsopcode.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsarena.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsproto.tbl
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsobj.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsnum.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsscript.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsclist.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsconfig.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsxml.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jslong.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsbit.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/js.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsbool.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsexn.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/js.mdp
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsstr.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsxml.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsgc.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsparse.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jscntxt.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/js.pkg
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsarena.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsemit.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/README.html
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsshell.msg
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jslibmath.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/spidermonkey/src/jsxdrapi.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/README.md
/usr/lib/node_modules/ldapjs/deps/javascriptlint/.npmignore
/usr/lib/node_modules/ldapjs/deps/javascriptlint/javascriptlint/pyspidermonkey/nodepos.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/javascriptlint/pyspidermonkey/tokens.tbl
/usr/lib/node_modules/ldapjs/deps/javascriptlint/javascriptlint/pyspidermonkey/nodepos.h
/usr/lib/node_modules/ldapjs/deps/javascriptlint/javascriptlint/pyspidermonkey/pyspidermonkey.c
/usr/lib/node_modules/ldapjs/deps/javascriptlint/javascriptlint/lint.py
/usr/lib/node_modules/ldapjs/deps/javascriptlint/javascriptlint/pyspidermonkey_/__init__.py
/usr/lib/node_modules/ldapjs/deps/javascriptlint/javascriptlint/visitation.py
/usr/lib/node_modules/ldapjs/deps/javascriptlint/javascriptlint/jsparse.py
/usr/lib/node_modules/ldapjs/deps/javascriptlint/javascriptlint/htmlparse.py
/usr/lib/node_modules/ldapjs/deps/javascriptlint/javascriptlint/conf.py
/usr/lib/node_modules/ldapjs/deps/javascriptlint/javascriptlint/jsl
/usr/lib/node_modules/ldapjs/deps/javascriptlint/javascriptlint/util.py
/usr/lib/node_modules/ldapjs/deps/javascriptlint/javascriptlint/jsl.py
/usr/lib/node_modules/ldapjs/deps/javascriptlint/javascriptlint/fs.py
/usr/lib/node_modules/ldapjs/deps/javascriptlint/javascriptlint/spidermonkey.py
/usr/lib/node_modules/ldapjs/deps/javascriptlint/javascriptlint/__init__.py
/usr/lib/node_modules/ldapjs/deps/javascriptlint/javascriptlint/warnings.py
/usr/lib/node_modules/ldapjs/deps/javascriptlint/Makefile
/usr/lib/node_modules/ldapjs/deps/javascriptlint/COPYING
/usr/lib/node_modules/ldapjs/deps/jsstyle/README.md
/usr/lib/node_modules/ldapjs/deps/jsstyle/.npmignore
/usr/lib/node_modules/ldapjs/deps/jsstyle/jsstyle
/usr/lib/node_modules/ldapjs/examples/snoopldap.d
/usr/lib/node_modules/ldapjs/examples/pooled_client.js
/usr/lib/node_modules/ldapjs/examples/inmemory.js
/usr/lib/node_modules/ldapjs/.gitmodules
/usr/lib/node_modules/ldapjs/package.json
/usr/lib/node_modules/ldapjs/bin/ldapjs-add
/usr/lib/node_modules/ldapjs/bin/ldapjs-modify
/usr/lib/node_modules/ldapjs/bin/ldapjs-compare
/usr/lib/node_modules/ldapjs/bin/ldapjs-delete
/usr/lib/node_modules/ldapjs/bin/ldapjs-search
/usr/lib/node_modules/ldapjs/test/messages/bind_request.test.js
/usr/lib/node_modules/ldapjs/test/messages/add_request.test.js
/usr/lib/node_modules/ldapjs/test/messages/search_request.test.js
/usr/lib/node_modules/ldapjs/test/messages/search_response.test.js
/usr/lib/node_modules/ldapjs/test/messages/search_entry.test.js
/usr/lib/node_modules/ldapjs/test/messages/compare_response.test.js
/usr/lib/node_modules/ldapjs/test/messages/unbind_request.test.js
/usr/lib/node_modules/ldapjs/test/messages/moddn_response.test.js
/usr/lib/node_modules/ldapjs/test/messages/del_response.test.js
/usr/lib/node_modules/ldapjs/test/messages/bind_response.test.js
/usr/lib/node_modules/ldapjs/test/messages/del_request.test.js
/usr/lib/node_modules/ldapjs/test/messages/ext_request.test.js
/usr/lib/node_modules/ldapjs/test/messages/add_response.test.js
/usr/lib/node_modules/ldapjs/test/messages/moddn_request.test.js
/usr/lib/node_modules/ldapjs/test/messages/modify_response.test.js
/usr/lib/node_modules/ldapjs/test/messages/compare_request.test.js
/usr/lib/node_modules/ldapjs/test/messages/ext_response.test.js
/usr/lib/node_modules/ldapjs/test/messages/modify_request.test.js
/usr/lib/node_modules/ldapjs/test/attribute.test.js
/usr/lib/node_modules/ldapjs/test/laundry.test.js
/usr/lib/node_modules/ldapjs/test/controls/control.test.js
/usr/lib/node_modules/ldapjs/test/controls/entry_change_notification_control_test.js
/usr/lib/node_modules/ldapjs/test/controls/paged_results_control_test.js
/usr/lib/node_modules/ldapjs/test/controls/persistent_search_control.test.js
/usr/lib/node_modules/ldapjs/test/dn.test.js
/usr/lib/node_modules/ldapjs/test/filters/or.test.js
/usr/lib/node_modules/ldapjs/test/filters/eq.test.js
/usr/lib/node_modules/ldapjs/test/filters/approx.test.js
/usr/lib/node_modules/ldapjs/test/filters/ext.test.js
/usr/lib/node_modules/ldapjs/test/filters/and.test.js
/usr/lib/node_modules/ldapjs/test/filters/le.test.js
/usr/lib/node_modules/ldapjs/test/filters/parse.test.js
/usr/lib/node_modules/ldapjs/test/filters/ge.test.js
/usr/lib/node_modules/ldapjs/test/filters/substr.test.js
/usr/lib/node_modules/ldapjs/test/filters/not.test.js
/usr/lib/node_modules/ldapjs/test/filters/presence.test.js
/usr/lib/node_modules/ldapjs/test/change.test.js
/usr/lib/node_modules/ldapjs/test/url.test.js
/usr/lib/node_modules/ldapjs/test/client.test.js
/usr/lib/node_modules/ldapjs/.travis.yml
/usr/local/share/vaclab/nodejs/response.js
/usr/local/share/vaclab/nodejs/internal.js
/usr/local/share/vaclab/nodejs/nodejsServers.js
/usr/local/share/vaclab/nodejs/external.js
/usr/local/share/vaclab/nodejs/rscript.js
/usr/local/share/vaclab/nodejs/tcp.js
/usr/local/share/vaclab/nodejs/latex.js
/usr/local/share/vaclab/nodejs/http.js
/usr/local/share/vaclab/nodejs/utils.js
/usr/local/share/vaclab/nodejs/email.js
/usr/local/share/vaclab/nodejs/relay.js
/usr/local/share/vaclab/nodejs/ldap.js
/usr/local/share/vaclab/nodejs/config.js
/usr/local/share/vaclab/nodejs/relay-add.js
/usr/local/share/vaclab/nodejs/tools.js
/usr/local/bin/nodejsServers
/usr/local/bin/vxiTransceiver
/usr/local/bin/vxi11_transceiver
/etc/init.d/NodejsServers
/usr/lib/node_modules/ldapjs/node_modules/.bin/nopt
/usr/lib/node_modules/ldapjs/node_modules/.bin/bunyan
/usr/sbin/rcNodejsServers

%changelog
* Wed Jan 16 2013 Rolf.Niepraschk@ptb.de
- "getEnv" durch "process.env" ersetzt. "ldap" wegen "undefined symbol"
  (buffertools) entfernt. Dokumentation der Funktionen begonnen (dox). 

* Mon Jan 14 2013 Rolf.Niepraschk@ptb.de
- Aufteilung auf Module, Versionsnummer des rpm-Paketes identisch zu der von
  nodejsServers. Angabe zu "%changelog" aus eigener Datei CHANGES.

* Fri Jan 11 2013 Rolf.Niepraschk@ptb.de
- Änderungen zu t_start und t_stop (erste Tests)

* Fri Dec 14 2012 Rolf.Niepraschk@ptb.de 
- Korrekte Wandlung String nach Int/Float

* Thu Sep 27 2012 Rolf.Niepraschk@ptb.de
- Debug-Ausgabe optimiert.

* Wed Sep 26 2012 Rolf.Niepraschk@ptb.de
- Debug-Ausgabe optimiert.

* Tue Sep 25 2012 Rolf.Niepraschk@ptb.de
- timestamps für VXITRANSCEIVER

* Fri Aug 31 2012 Rolf.Niepraschk@ptb.de 
- Korrekturen zu filelist

* Thu Aug 30 2012 Rolf.Niepraschk@ptb.de
- Neue rpm-Erzeugung direkt mit "rpmbuild", "relay-add.js"ergänzt.

