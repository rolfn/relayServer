Summary: Nodejs-basierte http-Server für Messaufgaben
Name: relayServer
Version: 11.12.5
Release: 3
License: ???
Group: Productivity/Networking/Web/Servers
BuildArch: noarch
Packager: Rolf Niepraschk
AutoReqProv: no
Requires: nodejs
%{?systemd_requires}

%description
Nodejs-basierte http-Server für Messaufgaben

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%dir /etc
%dir /etc/init
%dir /etc/init.d
%dir /usr
%dir /usr/lib
%dir /usr/lib/node_modules
%dir /usr/lib/systemd
%dir /usr/lib/systemd/system
%dir /usr/sbin
%dir /usr/local
%dir /usr/local/share
%dir /usr/local/share/vaclab
%dir /usr/local/share/vaclab/nodejs
%dir /usr/local/share/vaclab/nodejs/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/once
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/once/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/once/node_modules/wrappy
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/once/node_modules/wrappy/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/once/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/abbrev
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/supports-color
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/node_modules/minimist
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/node_modules/minimist/example
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/node_modules/minimist/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/examples
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/sprintf-js
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/sprintf-js/demo
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/sprintf-js/src
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/sprintf-js/dist
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/sprintf-js/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/utility
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/chain
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/number
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/date
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/action
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/action/store
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/action/append
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/help
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/argument
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/examples
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/type
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/type/js
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/schema
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/examples
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/dist
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/node_modules/sigmund
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/node_modules/sigmund/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/node_modules/lru-cache
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/node_modules/lru-cache/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/node_modules/lru-cache/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/node_modules/sigmund
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/node_modules/sigmund/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/node_modules/lru-cache
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/inherits
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/examples
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/tests
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/tests/fixtures
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/.bin
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/wordwrap
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/wordwrap/example
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/wordwrap/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/async
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/async/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/.bin
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esutils
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esutils/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esutils/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/node_modules/amdefine
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/lib/source-map
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/build
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/test/source-map
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esprima
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esprima/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esprima/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/estraverse
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/esprima
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/esprima/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/esprima/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/which
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/which/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/nopt
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/nopt/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/nopt/examples
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/nopt/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/nopt/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/tools
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/async
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/async/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/node_modules/amdefine
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/lib/source-map
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/build
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/test/source-map
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/test/compress
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/.bin
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/example
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/test/_
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/lib/handlebars
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/lib/handlebars/compiler
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/cjs
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/cjs/handlebars
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/cjs/handlebars/compiler
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/amd
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/amd/handlebars
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/amd/handlebars/compiler
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/example
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/biz
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/biz/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/biz/node_modules/grux
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/biz/node_modules/garply
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/biz/node_modules/garply/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/biz/node_modules/tiv
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/baz
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/without_basedir
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/without_basedir/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/quux
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/quux/foo
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/other_path
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/other_path/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/incorrect_main
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/bar
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/bar/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/bar/node_modules/foo
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/punycode
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/punycode/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/punycode/node_modules/punycode
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/dotdot
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/dotdot/abc
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/node_path
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/node_path/y
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/node_path/y/ccc
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/node_path/y/bbb
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/node_path/x
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/node_path/x/aaa
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/node_path/x/ccc
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/module_dir
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/module_dir/xmodules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/module_dir/xmodules/aaa
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/module_dir/zmodules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/module_dir/zmodules/bbb
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/module_dir/ymodules
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/module_dir/ymodules/aaa
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/store
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/assets
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/assets/vendor
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/command
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/command/common
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/util
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/report
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/report/common
%dir /usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/report/templates
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/nan
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/nan/build
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/commander
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/tinycolor
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/options
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/options/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/options/test
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/options/test/fixtures
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/src
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/build
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/tmp
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/.bin
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/xmlhttprequest
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/xmlhttprequest/example
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/xmlhttprequest/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/xmlhttprequest/tests
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/coverage
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/coverage/lcov-report
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/coverage/lcov-report/socket.io-client
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/coverage/lcov-report/socket.io-client/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/coverage/lcov-report/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/transports
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/gsolo
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/gsolo/encryption
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/prng
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/rsa
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/cert
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/math
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/adobe
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/adobe/net
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/adobe/net/proxies
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/dist
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/test
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io-client/test/node
%dir /usr/local/share/vaclab/nodejs/node_modules/winston
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/docs
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo/docs
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo/examples
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo/examples/subdir
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo/test
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/eyes
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/eyes/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/eyes/test
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/colors
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/colors/themes
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/async
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/async/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/cycle
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/oauth-sign
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/cookie-jar
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/cookie-jar/tests
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/mime
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/mime/types
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/example
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/boom
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/boom/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/boom/test
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/boom/images
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/sntp
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/sntp/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/sntp/examples
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/sntp/test
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/hoek
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/hoek/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/hoek/test
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/hoek/test/modules
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/hoek/images
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/cryptiles
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/cryptiles/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/cryptiles/test
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/test
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/images
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/node-uuid
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/node-uuid/benchmark
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/node-uuid/test
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/aws-sign
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/tunnel-agent
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/integration
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/json-stringify-safe
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/test
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/test/browser
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/forever-agent
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/ssl
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/ssl/ca
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/lib/winston
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/lib/winston/transports
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/lib/winston/config
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/examples
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/test
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/test/transports
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/test/fixtures
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/test/fixtures/keys
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/test/fixtures/logs
%dir /usr/local/share/vaclab/nodejs/node_modules/winston/test/fixtures/scripts
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/nan
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/nan/build
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/commander
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/tinycolor
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/options
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/options/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/options/test
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/options/test/fixtures
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/src
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/build
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/tmp
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/.bin
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/xmlhttprequest
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/xmlhttprequest/example
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/xmlhttprequest/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/xmlhttprequest/tests
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/component-json
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/visionmedia-debug
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/component-emitter
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/timoxley-to-array
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/component-bind
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/learnboost-socket.io-protocol
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/learnboost-engine.io-client
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/learnboost-engine.io-client/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/learnboost-engine.io-client/lib/transports
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/component-json-fallback
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/transports
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/gsolo
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/gsolo/encryption
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/prng
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/rsa
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/cert
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/math
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/adobe
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/adobe/net
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/adobe/net/proxies
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/dist
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/test
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/test/node
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/base64id
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/base64id/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/policyfile
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/policyfile/doc
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/policyfile/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/policyfile/tests
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/policyfile/tests/ssl
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/policyfile/examples
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/benches
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/benches/stress
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/benches/stress/speed
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/benches/stress/rpushblpop
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/benches/stress/pubsub
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/lib/parser
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/examples
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/transports
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/transports/websocket
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/stores
%dir /usr/local/share/vaclab/nodejs/node_modules/socket.io/benchmarks
%dir /usr/local/share/vaclab/nodejs/node_modules/vwebsocket
%dir /usr/local/share/vaclab/nodejs/node_modules/vwebsocket/test
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/debug
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/debug/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/debug/node_modules/ms
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/commander
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/node_modules/minimist
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/node_modules/minimist/example
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/node_modules/minimist/test
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/examples
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/test
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/.bin
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/growl
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/growl/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/testing
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/commander
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/commander/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/examples
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/test
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/nodes
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/diff
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/graceful-fs
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/graceful-fs/test
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/node_modules/sigmund
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/node_modules/sigmund/test
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/node_modules/lru-cache
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/test
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/test
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/inherits
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/examples
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/test
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/escape-string-regexp
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/templates
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/lib/interfaces
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/lib/browser
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/mocha/images
%dir /usr/local/share/vaclab/nodejs/node_modules/.bin
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/public-address
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/core-util-is
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/core-util-is/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/isarray
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/isarray/build
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/string_decoder
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/inherits
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/he
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/he/man
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/he/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/.bin
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/node_modules/rai
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/node_modules/rai/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/node_modules/rai/cert
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/node_modules/xoauth2
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/directmail
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/directmail/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mime
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mime/types
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/follow-redirects
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/follow-redirects/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/follow-redirects/node_modules/underscore
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/follow-redirects/test
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/dkim-signer
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/dkim-signer/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/dkim-signer/node_modules/punycode
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/dkim-signer/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/encodings
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/encodings/tables
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/test
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/addressparser
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/nodemailer/lib/engines
%dir /usr/local/share/vaclab/nodejs/node_modules/moment
%dir /usr/local/share/vaclab/nodejs/node_modules/moment/min
%dir /usr/local/share/vaclab/nodejs/node_modules/moment/tasks
%dir /usr/local/share/vaclab/nodejs/node_modules/moment/lang
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.isobject
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.isobject/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.isobject/node_modules/lodash._objecttypes
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys/node_modules/lodash._isnative
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys/node_modules/lodash._shimkeys
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys/node_modules/lodash._shimkeys/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys/node_modules/lodash._shimkeys/node_modules/lodash._objecttypes
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules/lodash._isnative
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules/lodash.noop
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._slice
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules/lodash._isnative
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules/lodash.noop
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules/lodash._isnative
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules/lodash.noop
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash.isfunction
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.support
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.support/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.support/node_modules/lodash._isnative
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.identity
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._objecttypes
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._releasearray
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._releasearray/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._releasearray/node_modules/lodash._maxpoolsize
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._releasearray/node_modules/lodash._arraypool
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._getarray
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._getarray/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._getarray/node_modules/lodash._arraypool
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash.forin
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash.isfunction
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.property
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._objecttypes
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash.keys
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash.keys/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash.keys/node_modules/lodash.isobject
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash.keys/node_modules/lodash._isnative
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash.keys/node_modules/lodash._shimkeys
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules/lodash._isnative
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules/lodash.noop
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._slice
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash.isobject
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules/lodash._isnative
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules/lodash.noop
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash.isobject
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules/lodash._isnative
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules/lodash.noop
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash.isfunction
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.support
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.support/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.support/node_modules/lodash._isnative
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.identity
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/.bin
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/commander
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/adler-32
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/colors
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/colors/themes
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/.bin
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/frac
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/voc
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/.bin
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/node_modules/core-util-is
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/node_modules/core-util-is/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/node_modules/isarray
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/node_modules/isarray/build
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/node_modules/string_decoder
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/typedarray
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/typedarray/example
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/typedarray/test
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/typedarray/test/server
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/inherits
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/test
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/test/server
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/.bin
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/voc
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/dist
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/cfb
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/cfb/dist
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/cfb/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/crc-32
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/vendor
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/inflate-pako-string
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/inflate-zlib
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/inflate-dankogai
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/deflate-pako
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/deflate-dankogai
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/deflate-zlib
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/deflate-pako-string
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/inflate-imaya
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/inflate-pako-untyped
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/deflate-gildas
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/deflate-imaya
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/inflate-pako
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/deflate-pako-untyped
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/samples
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/lib/zlib
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/lib/utils
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/dist
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/fixtures
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/fixtures/samples_deflated_raw
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/fixtures/samples
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/browser
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/dist
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/bin
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash._objecttypes
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash.keys
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash.keys/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash.keys/node_modules/lodash.isobject
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash.keys/node_modules/lodash._isnative
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash.keys/node_modules/lodash._shimkeys
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/test
%dir /usr/local/share/vaclab/nodejs/node_modules/node-xlsx/test/fixtures
%dir /usr/local/share/vaclab/nodejs/node_modules/vlogger
%dir /usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment
%dir /usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/min
%dir /usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/tasks
%dir /usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang
%dir /usr/local/share/vaclab/nodejs/node_modules/vlogger/test
%dir /usr/local/share/vaclab/nodejs/node_modules/temp
%dir /usr/local/share/vaclab/nodejs/node_modules/temp/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/temp/node_modules/.bin
%dir /usr/local/share/vaclab/nodejs/node_modules/temp/node_modules/rimraf
%dir /usr/local/share/vaclab/nodejs/node_modules/temp/node_modules/rimraf/test
%dir /usr/local/share/vaclab/nodejs/node_modules/temp/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/temp/examples
%dir /usr/local/share/vaclab/nodejs/node_modules/temp/test
%dir /usr/local/share/vaclab/nodejs/node_modules/underscore
%dir /usr/local/share/vaclab/nodejs/node_modules/vxi11
%dir /usr/local/share/vaclab/nodejs/node_modules/vxi11/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/request
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/oauth-sign
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/mime
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/mime/types
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/example
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/boom
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/boom/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/boom/test
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/boom/images
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/sntp
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/sntp/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/sntp/examples
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/sntp/test
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/hoek
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/hoek/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/hoek/test
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/hoek/test/modules
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/hoek/images
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/cryptiles
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/cryptiles/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/cryptiles/test
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/test
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/images
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/man
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/man/man3ctype
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tools
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctype
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctio
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctio/float
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctio/uint
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctio/int
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctf
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/assert-plus
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/asn1
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/asn1/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/asn1/lib/ber
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/asn1/tst
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/asn1/tst/ber
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/node-uuid
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/node-uuid/benchmark
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/node-uuid/test
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tunnel-agent
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/aws-sign2
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/async
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/async/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/integration
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/json-stringify-safe
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/qs
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/forever-agent
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tough-cookie
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tough-cookie/node_modules
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tough-cookie/node_modules/punycode
%dir /usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tough-cookie/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/request/lib
%dir /usr/local/share/vaclab/nodejs/node_modules/stack-trace
%dir /usr/local/share/vaclab/nodejs/node_modules/stack-trace/lib
%dir /usr/local/bin
"/usr/lib/systemd/system/relayServer.service" 
"/usr/local/share/vaclab/nodejs/response.js" 
"/usr/local/share/vaclab/nodejs/internal.js" 
"/usr/local/share/vaclab/nodejs/external.js" 
"/usr/local/share/vaclab/nodejs/udp.js" 
"/usr/local/share/vaclab/nodejs/rscript.js" 
"/usr/local/share/vaclab/nodejs/tcp.js" 
"/usr/local/share/vaclab/nodejs/excel.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/CHANGELOG.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/once/once.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/once/node_modules/wrappy/wrappy.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/once/node_modules/wrappy/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/once/node_modules/wrappy/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/once/node_modules/wrappy/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/once/node_modules/wrappy/test/basic.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/once/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/once/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/once/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/once/test/once.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/abbrev/abbrev.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/abbrev/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/abbrev/CONTRIBUTING.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/abbrev/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/abbrev/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/abbrev/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/supports-color/readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/supports-color/cli.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/supports-color/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/supports-color/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/readme.markdown" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/node_modules/minimist/readme.markdown" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/node_modules/minimist/example/parse.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/node_modules/minimist/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/node_modules/minimist/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/node_modules/minimist/test/default_bool.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/node_modules/minimist/test/parse_modified.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/node_modules/minimist/test/parse.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/node_modules/minimist/test/dotted.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/node_modules/minimist/test/long.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/node_modules/minimist/test/short.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/node_modules/minimist/test/dash.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/node_modules/minimist/test/whitespace.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/node_modules/minimist/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/node_modules/minimist/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/examples/pow.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/bin/cmd.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/bin/usage.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/test/umask_sync.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/test/race.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/test/rel.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/test/return.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/test/perm_sync.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/test/perm.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/test/opts_fs_sync.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/test/opts_fs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/test/sync.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/test/chmod.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/test/root.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/test/umask.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/test/clobber.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/test/mkdirp.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/test/return_sync.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/mkdirp/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/CHANGELOG.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/bower.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/CHANGELOG.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/sprintf-js/demo/angular.html" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/sprintf-js/bower.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/sprintf-js/src/angular-sprintf.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/sprintf-js/src/sprintf.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/sprintf-js/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/sprintf-js/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/sprintf-js/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/sprintf-js/gruntfile.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/sprintf-js/dist/angular-sprintf.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/sprintf-js/dist/sprintf.min.map" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/sprintf-js/dist/angular-sprintf.min.map" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/sprintf-js/dist/sprintf.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/sprintf-js/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/sprintf-js/test/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/negate.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/flowRight.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/spread.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/backflow.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/debounce.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/compose.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/bindKey.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/once.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/ary.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/flow.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/curry.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/partial.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/defer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/delay.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/partialRight.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/memoize.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/wrap.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/throttle.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/curryRight.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/after.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/bind.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/before.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/bindAll.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/function/rearg.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/shuffle.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/detect.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/foldr.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/foldl.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/inject.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/invoke.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/reduce.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/map.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/eachRight.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/groupBy.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/contains.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/size.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/includes.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/include.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/select.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/reduceRight.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/sortBy.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/sample.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/reject.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/partition.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/any.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/pluck.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/all.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/at.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/find.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/indexBy.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/each.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/countBy.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/every.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/collect.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/sortByAll.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/max.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/findLast.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/some.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/filter.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/findWhere.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/forEach.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/forEachRight.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/collection/where.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/date.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/indexOfNaN.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/createExtremum.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/toIterable.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/arrayCopy.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/charAtCallback.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/mergeData.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseForOwn.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseDifference.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/isLength.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/compareAscending.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseForIn.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/isSpace.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/equalByTag.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/trimmedLeftIndex.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/bindCallback.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/arrayMin.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseSortBy.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/reorder.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseMatches.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/pickByCallback.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/mapSet.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/isIterateeCall.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseFind.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseRandom.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseSome.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/createCtorWrapper.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseWrapperValue.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/unescapeHtmlChar.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/mapDelete.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/pickByArray.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/isIndex.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/cacheIndexOf.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseBindAll.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/sortedUniq.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseMatchesProperty.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseIndexOf.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/equalObjects.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/compareMultipleAscending.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/trimmedRightIndex.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseCallback.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseFill.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseFilter.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseToString.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseSetData.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseFlatten.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/MapCache.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/createBindWrapper.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/charsLeftIndex.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/charsRightIndex.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseFor.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/arrayEachRight.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseDelay.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/initCloneObject.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/arrayEach.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/mapHas.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseMap.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseReduce.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseSlice.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseInvoke.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/arrayFilter.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/arrayEvery.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/createHybridWrapper.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/setData.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/arrayReduce.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseCompareAscending.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/reEvaluate.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/replaceHolders.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/getView.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/createAggregator.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/arrayMap.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/escapeHtmlChar.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/shimKeys.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/binaryIndexBy.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseAt.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/getData.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/isStrictComparable.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/bufferClone.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/extremumBy.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/reEscape.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/initCloneArray.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/initCloneByTag.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/cachePush.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseProperty.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/SetCache.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseIsEqualDeep.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/composeArgs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/assignDefaults.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/assignOwnDefaults.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/lazyReverse.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/isBindable.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/basePullAt.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/isObjectLike.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/LazyWrapper.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/toObject.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/createAssigner.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/deburrLetter.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseEach.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/lazyClone.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseForOwnRight.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/shimIsPlainObject.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseIsEqual.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/LodashWrapper.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseAssign.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseEachRight.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/mapGet.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/createPartialWrapper.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/equalArrays.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseEvery.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/arrayReduceRight.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseMerge.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseMergeDeep.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/createPad.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseCreate.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/wrapperClone.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/lazyValue.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/createCompounder.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/arraySome.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/metaMap.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseFunctions.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/composeArgsRight.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseIsMatch.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseClone.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/createWrapper.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseForRight.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/reInterpolate.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseUniq.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/arrayMax.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/createCache.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/binaryIndex.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/escapeStringChar.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseValues.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/internal/baseCopy.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/support.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/utility/identity.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/utility/mixin.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/utility/attempt.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/utility/times.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/utility/constant.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/utility/matches.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/utility/noop.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/utility/propertyOf.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/utility/uniqueId.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/utility/iteratee.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/utility/range.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/utility/property.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/utility/matchesProperty.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/utility/callback.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/number.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/takeRight.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/tail.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/sortedLastIndex.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/flattenDeep.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/first.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/object.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/intersection.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/chunk.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/xor.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/without.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/lastIndexOf.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/findIndex.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/head.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/remove.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/indexOf.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/last.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/findLastIndex.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/flatten.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/uniq.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/difference.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/slice.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/takeRightWhile.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/dropWhile.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/unique.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/dropRight.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/initial.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/takeWhile.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/pull.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/fill.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/zipObject.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/pullAt.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/drop.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/union.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/take.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/rest.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/dropRightWhile.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/unzip.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/zip.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/compact.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array/sortedIndex.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/chain/wrapperPlant.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/chain/wrapperCommit.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/chain/lodash.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/chain/wrapperToString.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/chain/valueOf.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/chain/run.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/chain/plant.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/chain/wrapperReverse.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/chain/reverse.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/chain/thru.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/chain/commit.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/chain/chain.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/chain/tap.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/chain/value.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/chain/toJSON.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/chain/wrapperValue.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/chain/toString.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/chain/wrapperChain.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/number/random.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/isNumber.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/isTypedArray.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/isBoolean.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/isElement.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/isArray.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/isString.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/isNull.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/isMatch.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/isFinite.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/isError.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/toArray.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/isFunction.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/isEmpty.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/isArguments.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/cloneDeep.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/isEqual.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/isUndefined.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/isRegExp.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/isDate.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/isObject.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/isPlainObject.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/toPlainObject.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/isNaN.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/isNative.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang/clone.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/chain.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/utility.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/lang.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/parseInt.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/trim.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/template.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/escapeRegExp.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/snakeCase.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/startCase.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/camelCase.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/repeat.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/trimLeft.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/endsWith.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/trimRight.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/deburr.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/padLeft.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/padRight.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/pad.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/escape.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/words.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/capitalize.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/unescape.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/kebabCase.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/startsWith.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/templateSettings.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/string/trunc.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/values.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/findLastKey.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/merge.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/pick.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/omit.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/result.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/valuesIn.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/keys.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/invert.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/transform.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/defaults.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/pairs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/forInRight.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/keysIn.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/findKey.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/assign.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/forIn.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/methods.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/create.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/functions.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/has.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/forOwnRight.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/mapValues.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/extend.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/object/forOwn.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/date/now.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/node_modules/lodash/array.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/argparse.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/namespace.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/const.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/argument_parser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/action/store/constant.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/action/store/false.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/action/store/true.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/action/append.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/action/count.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/action/help.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/action/version.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/action/store.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/action/subparsers.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/action/append/constant.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/action.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/help/formatter.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/help/added_formatters.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/argument/exclusive.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/argument/group.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/argument/error.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/lib/action_container.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/examples/arguments.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/examples/parents.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/examples/testformatters.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/examples/nargs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/examples/help.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/examples/sub_commands.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/examples/choice.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/examples/sum.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/examples/prefix_chars.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/examples/constants.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/node_modules/argparse/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/common.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/dumper.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/type/omap.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/type/js/function.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/type/js/regexp.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/type/js/undefined.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/type/merge.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/type/binary.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/type/int.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/type/null.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/type/map.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/type/pairs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/type/str.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/type/set.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/type/seq.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/type/bool.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/type/timestamp.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/type/float.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/schema.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/schema/core.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/schema/default_full.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/schema/failsafe.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/schema/default_safe.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/schema/json.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/mark.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/type.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/exception.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/lib/js-yaml/loader.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/examples/sample_document.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/examples/dumper.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/examples/custom_types.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/examples/dumper.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/examples/sample_document.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/examples/custom_types.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/dist/js-yaml.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/dist/js-yaml.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/bin/js-yaml.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/js-yaml/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/minimatch.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/node_modules/sigmund/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/node_modules/sigmund/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/node_modules/sigmund/sigmund.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/node_modules/sigmund/bench.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/node_modules/sigmund/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/node_modules/sigmund/test/basic.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/node_modules/lru-cache/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/node_modules/lru-cache/CONTRIBUTORS" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/node_modules/lru-cache/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/node_modules/lru-cache/lib/lru-cache.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/node_modules/lru-cache/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/node_modules/lru-cache/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/node_modules/lru-cache/test/foreach.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/node_modules/lru-cache/test/basic.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/node_modules/lru-cache/test/memory-leak.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/test/extglob-ending-with-state-char.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/test/brace-expand.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/test/basic.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/test/defaults.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/minimatch/test/caching.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/minimatch.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/node_modules/sigmund/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/node_modules/sigmund/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/node_modules/sigmund/sigmund.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/node_modules/sigmund/bench.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/node_modules/sigmund/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/node_modules/sigmund/test/basic.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/CONTRIBUTORS" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/lib/lru-cache.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/test/foreach.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/test/basic.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/test/memory-leak.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/test/extglob-ending-with-state-char.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/test/brace-expand.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/test/basic.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/test/defaults.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/minimatch/test/caching.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/inherits/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/inherits/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/inherits/inherits_browser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/inherits/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/inherits/inherits.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/node_modules/inherits/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/examples/usr-local.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/examples/g.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/test/bash-results.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/test/readme-issue.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/test/00-setup.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/test/root-nomount.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/test/nocase-nomagic.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/test/bash-comparison.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/test/mark.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/test/pause-resume.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/test/root.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/test/globstar-match.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/test/zz-cleanup.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/test/new-glob-optional-options.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/test/cwd-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/test/stat.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/node_modules/glob/glob.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/LICENSE-MIT" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/lib/fileset.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/tests/helper.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/tests/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/tests/fixtures/an (odd) filename.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/fileset/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/.bin/supports-color" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/.bin/mkdirp" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/.bin/js-yaml" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/.bin/esgenerate" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/.bin/esvalidate" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/.bin/escodegen" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/.bin/which" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/.bin/nopt" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/.bin/esparse" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/.bin/handlebars" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/wordwrap/example/meat.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/wordwrap/example/center.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/wordwrap/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/wordwrap/README.markdown" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/wordwrap/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/wordwrap/test/wrap.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/wordwrap/test/break.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/wordwrap/test/idleness.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/wordwrap/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/async/component.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/async/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/async/lib/async.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/async/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/async/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/async/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/component.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/gulpfile.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/LICENSE.BSD" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/.bin/esvalidate" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/.bin/esparse" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esutils/.jshintrc" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esutils/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esutils/lib/utils.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esutils/lib/code.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esutils/lib/keyword.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esutils/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esutils/test/keyword.coffee" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esutils/test/code.coffee" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esutils/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/Makefile.dryice.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/CHANGELOG.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/node_modules/amdefine/amdefine.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/node_modules/amdefine/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/node_modules/amdefine/intercept.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/node_modules/amdefine/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/node_modules/amdefine/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/lib/source-map.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/lib/source-map/source-node.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/lib/source-map/util.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/lib/source-map/base64-vlq.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/lib/source-map/array-set.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/lib/source-map/source-map-generator.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/lib/source-map/source-map-consumer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/lib/source-map/binary-search.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/lib/source-map/base64.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/lib/source-map/mapping-list.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/build/suffix-browser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/build/prefix-source-map.jsm" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/build/test-suffix.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/build/assert-shim.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/build/suffix-source-map.jsm" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/build/test-prefix.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/build/suffix-utils.jsm" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/build/mini-require.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/build/prefix-utils.jsm" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/test/run-tests.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/test/source-map/util.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/test/source-map/test-api.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/test/source-map/test-util.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/test/source-map/test-binary-search.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/test/source-map/test-dog-fooding.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/test/source-map/test-source-map-consumer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/test/source-map/test-base64-vlq.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/test/source-map/test-array-set.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/test/source-map/test-source-node.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/test/source-map/test-source-map-generator.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/test/source-map/test-base64.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/source-map/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esprima/esprima.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esprima/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esprima/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esprima/bin/esparse.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esprima/bin/esvalidate.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esprima/test/compat.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esprima/test/runner.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esprima/test/run.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esprima/test/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/esprima/test/reflect.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/estraverse/LICENSE.BSD" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/estraverse/estraverse.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/estraverse/.jshintrc" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/estraverse/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/node_modules/estraverse/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/.jshintrc" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/LICENSE.source-map" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/escodegen.browser.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/escodegen.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/bin/esgenerate.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/escodegen/bin/escodegen.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/esprima/esprima.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/esprima/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/esprima/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/esprima/bin/esparse.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/esprima/bin/esvalidate.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/esprima/test/compat.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/esprima/test/runner.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/esprima/test/run.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/esprima/test/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/esprima/test/reflect.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/which/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/which/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/which/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/which/which.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/which/bin/which" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/nopt/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/nopt/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/nopt/lib/nopt.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/nopt/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/nopt/examples/my-program.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/nopt/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/nopt/bin/nopt.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/nopt/test/basic.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/release-notes.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/runtime.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/tools/node.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/async/component.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/async/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/async/lib/async.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/async/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/async/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/Makefile.dryice.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/CHANGELOG.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/node_modules/amdefine/amdefine.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/node_modules/amdefine/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/node_modules/amdefine/intercept.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/node_modules/amdefine/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/node_modules/amdefine/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/lib/source-map.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/lib/source-map/source-node.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/lib/source-map/util.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/lib/source-map/base64-vlq.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/lib/source-map/array-set.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/lib/source-map/source-map-generator.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/lib/source-map/source-map-consumer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/lib/source-map/binary-search.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/lib/source-map/base64.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/lib/source-map/mapping-list.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/build/suffix-browser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/build/prefix-source-map.jsm" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/build/test-suffix.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/build/assert-shim.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/build/suffix-source-map.jsm" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/build/test-prefix.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/build/suffix-utils.jsm" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/build/mini-require.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/build/prefix-utils.jsm" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/test/run-tests.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/test/source-map/util.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/test/source-map/test-api.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/test/source-map/test-util.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/test/source-map/test-binary-search.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/test/source-map/test-dog-fooding.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/test/source-map/test-source-map-consumer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/test/source-map/test-base64-vlq.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/test/source-map/test-array-set.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/test/source-map/test-source-node.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/test/source-map/test-source-map-generator.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/test/source-map/test-base64.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/node_modules/source-map/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/lib/output.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/lib/parse.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/lib/sourcemap.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/lib/transform.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/lib/compress.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/lib/scope.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/lib/utils.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/lib/mozilla-ast.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/lib/ast.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/bin/uglifyjs" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/test/run-tests.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/test/compress/dead-code.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/test/compress/issue-105.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/test/compress/issue-12.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/test/compress/blocks.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/test/compress/switch.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/test/compress/labels.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/test/compress/sequences.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/test/compress/drop-unused.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/test/compress/issue-44.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/test/compress/issue-22.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/test/compress/arrays.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/test/compress/loops.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/test/compress/conditionals.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/test/compress/properties.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/test/compress/issue-143.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/test/compress/debugger.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/test/compress/typeof.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/test/compress/issue-59.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/uglify-js/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/.bin/uglifyjs" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/readme.markdown" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/example/xup.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/example/boolean_double.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/example/line_count_options.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/example/line_count.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/example/boolean_single.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/example/divide.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/example/default_singles.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/example/line_count_wrap.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/example/nonopt.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/example/usage-options.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/example/short.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/example/default_hash.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/example/bool.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/example/reflect.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/example/string.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/test/parse.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/test/_/argv.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/test/_/bin.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/test/usage.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/test/_.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/node_modules/optimist/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/lib/handlebars.runtime.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/lib/handlebars.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/lib/handlebars/runtime.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/lib/handlebars/utils.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/lib/handlebars/base.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/lib/handlebars/compiler/javascript-compiler.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/lib/handlebars/compiler/printer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/lib/handlebars/compiler/base.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/lib/handlebars/compiler/compiler.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/lib/handlebars/compiler/parser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/lib/handlebars/compiler/ast.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/lib/handlebars/compiler/visitor.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/lib/handlebars/exception.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/lib/handlebars/safe-string.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/lib/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/handlebars.runtime.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/handlebars.runtime.amd.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/handlebars.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/handlebars.runtime.amd.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/cjs/handlebars.runtime.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/cjs/handlebars.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/cjs/handlebars/runtime.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/cjs/handlebars/utils.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/cjs/handlebars/base.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/cjs/handlebars/compiler/javascript-compiler.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/cjs/handlebars/compiler/printer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/cjs/handlebars/compiler/base.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/cjs/handlebars/compiler/compiler.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/cjs/handlebars/compiler/parser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/cjs/handlebars/compiler/ast.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/cjs/handlebars/compiler/visitor.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/cjs/handlebars/exception.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/cjs/handlebars/safe-string.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/amd/handlebars.runtime.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/amd/handlebars.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/amd/handlebars/runtime.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/amd/handlebars/utils.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/amd/handlebars/base.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/amd/handlebars/compiler/javascript-compiler.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/amd/handlebars/compiler/printer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/amd/handlebars/compiler/base.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/amd/handlebars/compiler/compiler.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/amd/handlebars/compiler/parser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/amd/handlebars/compiler/ast.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/amd/handlebars/compiler/visitor.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/amd/handlebars/exception.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/amd/handlebars/safe-string.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/handlebars.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/handlebars.amd.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/handlebars.amd.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/dist/handlebars.runtime.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/README.markdown" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/handlebars/bin/handlebars" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/readme.markdown" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/example/async.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/example/sync.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/lib/caller.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/lib/core.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/lib/core.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/lib/async.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/lib/sync.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/lib/node-modules-paths.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/node_path.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/biz/node_modules/grux/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/biz/node_modules/garply/lib/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/biz/node_modules/garply/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/biz/node_modules/tiv/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/foo.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/baz/quux.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/baz/doom.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/baz/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/without_basedir/main.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/without_basedir/node_modules/mymodule.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/quux/foo/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/other_path/lib/other-lib.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/other_path/root.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/cup.coffee" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/incorrect_main/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/incorrect_main/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/mug.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/bar/node_modules/foo/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/mug.coffee" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver/punycode/node_modules/punycode/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/mock.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/core.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/nonstring.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/dotdot.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/resolver_sync.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/filter_sync.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/dotdot/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/dotdot/abc/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/mock_sync.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/node_path/y/ccc/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/node_path/y/bbb/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/node_path/x/aaa/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/node_path/x/ccc/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/faulty_basedir.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/filter.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/module_dir/xmodules/aaa/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/module_dir/zmodules/bbb/main.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/module_dir/zmodules/bbb/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/module_dir/ymodules/aaa/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/test/module_dir.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/node_modules/resolve/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/.jshintrc" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/store/fslookup.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/store/tmp.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/store/memory.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/store/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/assets/vendor/prettify.css" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/assets/vendor/prettify.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/assets/sort-arrow-sprite.png" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/assets/sorter.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/assets/base.css" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/instrumenter.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/hook.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/register-plugins.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/object-utils.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/collector.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/cli.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/command/common/run-with-cover.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/command/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/command/check-coverage.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/command/help.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/command/instrument.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/command/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/command/report.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/command/cover.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/reporter.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/util/tree-summarizer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/util/yui-load-hook.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/util/meta.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/util/file-writer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/util/help-formatter.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/util/insertion-text.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/util/factory.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/util/writer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/util/input-error.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/util/file-matcher.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/config.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/report/common/defaults.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/report/teamcity.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/report/html.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/report/lcovonly.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/report/cobertura.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/report/lcov.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/report/text-summary.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/report/clover.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/report/text.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/report/none.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/report/templates/head.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/report/templates/foot.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/report/json-summary.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/report/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/lib/report/json.js" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/yui-coverage-comparison.md" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/istanbul/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/latest" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/nan/include_dirs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/nan/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/nan/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/nan/nan.h" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/nan/build/config.gypi" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/nan/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/nan/.dntrc" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/commander/Readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/commander/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/commander/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/tinycolor/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/tinycolor/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/tinycolor/example.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/tinycolor/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/tinycolor/tinycolor.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/options/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/options/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/options/lib/options.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/options/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/options/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/options/test/options.test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/node_modules/options/test/fixtures/test.conf" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/src/bufferutil.cc" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/src/validation.cc" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/History.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/builderror.log" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/lib/ErrorCodes.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/lib/Receiver.hixie.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/lib/WebSocket.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/lib/Validation.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/lib/BufferUtil.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/lib/BufferPool.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/lib/BufferUtil.fallback.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/lib/browser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/lib/WebSocketServer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/lib/Sender.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/lib/Validation.fallback.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/lib/Receiver.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/lib/Sender.hixie.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/binding.gyp" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/build/config.gypi" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/bin/wscat" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/ws/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/package.json~" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/README.org" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/uglify-js.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/lib/squeeze-more.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/lib/parse-js.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/lib/object-ast.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/lib/process.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/docstyle.css" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/tmp/uglify-hangs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/tmp/liftvars.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/tmp/hoist.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/tmp/uglify-hangs2.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/tmp/goto2.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/tmp/269.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/tmp/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/tmp/instrument.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/tmp/embed-tokens.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/tmp/app.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/tmp/goto.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/tmp/instrument2.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/bin/uglifyjs" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/beautify.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/scripts.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/ifreturn2.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue30.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/array4.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue21.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue54.1.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue68.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/ifreturn.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/const.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue9.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue28.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue53.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue16.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue4.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/var.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue278.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/assignment.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/mangle.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/with.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue11.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/forstatement.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/array2.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue17.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/array3.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/concatstring.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue29.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue48.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue10.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue34.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/if.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue27.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue25.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/empty-blocks.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue20.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/strict-equals.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue13.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue50.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue69.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue14.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/null_string.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/whitespace.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/array1.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/ifreturn2.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue30.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/array4.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue21.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue54.1.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue68.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/ifreturn.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/const.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue9.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue28.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue53.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue16.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue4.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/var.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue278.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/assignment.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/mangle.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/with.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue11.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/forstatement.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/array2.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue17.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/array3.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/concatstring.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue29.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue48.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue10.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue34.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/if.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue27.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue25.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/empty-blocks.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue20.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/strict-equals.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue13.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue50.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue69.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue14.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/null_string.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/whitespace.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/array1.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/test/testparser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/uglify-js/README.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/.bin/wscat" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/.bin/uglifyjs" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/xmlhttprequest/autotest.watchr" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/xmlhttprequest/example/demo.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/xmlhttprequest/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/xmlhttprequest/lib/XMLHttpRequest.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/xmlhttprequest/tests/test-request-protocols.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/xmlhttprequest/tests/testdata.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/xmlhttprequest/tests/test-events.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/xmlhttprequest/tests/test-headers.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/xmlhttprequest/tests/test-constants.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/xmlhttprequest/tests/test-request-methods.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/xmlhttprequest/tests/test-exceptions.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/xmlhttprequest/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/.test.js.un~" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/.package.json.un~" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/.gitignore" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/README" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/tests.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/unicodecategories.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/benchmark.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/test-tokenizer.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/Tokenizer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/test-parser.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/ZeParser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/.index.js.un~" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/Readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/.Readme.md.un~" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/..gitignore.un~" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/node_modules/active-x-obfuscator/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/History.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/coverage/lcov.info" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/coverage/lcov-report/socket.io-client/index.js.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/coverage/lcov-report/socket.io-client/lib/url.js.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/coverage/lcov-report/socket.io-client/lib/socket.js.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/coverage/lcov-report/socket.io-client/lib/on.js.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/coverage/lcov-report/socket.io-client/lib/manager.js.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/coverage/lcov-report/socket.io-client/lib/index.js.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/coverage/lcov-report/socket.io-client/lib/index.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/coverage/lcov-report/socket.io-client/index.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/coverage/lcov-report/lib/url.js.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/coverage/lcov-report/lib/index.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/coverage/lcov-report/prettify.css" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/coverage/lcov-report/index.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/coverage/lcov-report/prettify.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/coverage/coverage.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/namespace.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/util.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/socket.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/transports/xhr-polling.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/transports/xhr.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/transports/flashsocket.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/transports/websocket.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/transports/htmlfile.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/transports/jsonp-polling.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/build.sh" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/WebSocketMain.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/gsolo/encryption/MD5.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/prng/ARC4.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/prng/IPRNG.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/prng/Random.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/prng/TLSPRF.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/NullPad.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/AESKey.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/CFBMode.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/OFBMode.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/TripleDESKey.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/BlowFishKey.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/IPad.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/dump.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/IStreamCipher.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/CBCMode.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/PKCS5.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/aeskey.pl" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/IVMode.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/DESKey.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/ECBMode.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/XTeaKey.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/SimpleIVMode.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/ISymmetricKey.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/CFB8Mode.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/ICipher.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/SSLPad.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/CTRMode.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/TLSPad.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/IMode.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/Crypto.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash/IHash.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash/MD2.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash/MAC.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash/SHABase.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash/SHA1.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash/HMAC.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash/MD5.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash/SHA224.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash/IHMAC.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash/SHA256.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/SSLEvent.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/TLSError.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/TLSConfig.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/MACs.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/TLSSocket.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/IConnectionState.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/TLSEvent.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/ISecurityParameters.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/SSLConnectionState.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/TLSSecurityParameters.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/TLSConnectionState.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/CipherSuites.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/KeyExchanges.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/TLSTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/BulkCiphers.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/TLSEngine.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/SSLSecurityParameters.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/TLSSocketEvent.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/rsa/RSAKey.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/cert/X509CertificateCollection.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/cert/MozillaRootCertificates.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/cert/X509Certificate.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/CTRModeTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/CBCModeTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/TripleDESKeyTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/BigIntegerTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/TLSPRFTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/ECBModeTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/AESKeyTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/CFB8ModeTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/ARC4Test.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/RSAKeyTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/CFBModeTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/OFBModeTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/SHA1Test.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/MD5Test.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/BlowFishKeyTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/MD2Test.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/ITestHarness.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/SHA256Test.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/DESKeyTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/HMACTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/SHA224Test.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/TestCase.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/XTeaKeyTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/math/NullReduction.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/math/IReduction.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/math/bi_internal.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/math/MontgomeryReduction.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/math/BarrettReduction.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/math/BigInteger.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/math/ClassicReduction.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/Hex.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/Type.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/DER.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/UTCTime.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/PEM.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/PrintableString.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/ObjectIdentifier.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/Integer.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/ByteString.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/Sequence.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/IAsn1Type.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/OID.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/Set.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/ArrayUtil.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/Memory.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/Base64.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/adobe/net/proxies/RFC2817Socket.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/WebSocketEvent.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/IWebSocketLogger.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/WebSocketMainInsecure.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/WebSocket.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/web_socket.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/WebSocketMain.swf" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/sample.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/WebSocketMainInsecure.zip" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/vendor/web-socket-js/swfobject.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/transport.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/events.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/io.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/parser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/lib/json.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/dist/WebSocketMain.swf" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/dist/socket.io.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/dist/WebSocketMainInsecure.swf" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/dist/socket.io.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/bin/builder.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/test/events.test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/test/worker.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/test/node/builder.common.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/test/node/builder.test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/test/parser.test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/test/io.test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/test/socket.test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io-client/test/util.test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/docs/transports.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/CHANGELOG.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo/docs/docco.css" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo/docs/pkginfo.html" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo/lib/pkginfo.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo/examples/single-property.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo/examples/target-dir.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo/examples/array-argument.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo/examples/subdir/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo/examples/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo/examples/object-argument.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo/examples/all-properties.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo/examples/multiple-properties.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/pkginfo/test/pkginfo-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/eyes/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/eyes/lib/eyes.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/eyes/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/eyes/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/eyes/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/eyes/test/eyes-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/colors/colors.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/colors/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/colors/example.html" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/colors/MIT-LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/colors/ReadMe.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/colors/example.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/colors/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/colors/themes/winston-dark.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/colors/themes/winston-light.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/async/component.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/async/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/async/lib/async.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/async/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/async/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/cycle/cycle.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/cycle/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/cycle/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/oauth-sign/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/oauth-sign/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/oauth-sign/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/cookie-jar/tests/run.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/cookie-jar/tests/test-cookie.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/cookie-jar/tests/test-cookiejar.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/cookie-jar/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/cookie-jar/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/cookie-jar/jar.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/mime/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/mime/types/mime.types" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/mime/types/node.types" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/mime/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/mime/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/mime/mime.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/mime/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/example/usage.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/boom/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/boom/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/boom/lib/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/boom/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/boom/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/boom/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/boom/test/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/boom/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/boom/images/boom.png" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/boom/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/sntp/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/sntp/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/sntp/lib/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/sntp/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/sntp/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/sntp/examples/time.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/sntp/examples/offset.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/sntp/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/sntp/test/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/sntp/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/sntp/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/hoek/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/hoek/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/hoek/lib/escape.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/hoek/lib/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/hoek/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/hoek/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/hoek/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/hoek/test/modules/test2.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/hoek/test/modules/test3.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/hoek/test/modules/test1.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/hoek/test/escaper.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/hoek/test/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/hoek/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/hoek/images/hoek.png" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/hoek/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/cryptiles/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/cryptiles/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/cryptiles/lib/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/cryptiles/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/cryptiles/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/cryptiles/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/cryptiles/test/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/cryptiles/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/node_modules/cryptiles/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/lib/uri.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/lib/server.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/lib/utils.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/lib/crypto.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/lib/client.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/lib/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/test/uri.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/test/readme.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/test/server.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/test/utils.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/test/crypto.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/test/client.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/test/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/images/logo.png" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/images/hawk.png" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/hawk/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/node-uuid/component.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/node-uuid/uuid.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/node-uuid/LICENSE.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/node-uuid/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/node-uuid/benchmark/bench.gnu" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/node-uuid/benchmark/bench.sh" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/node-uuid/benchmark/benchmark.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/node-uuid/benchmark/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/node-uuid/benchmark/benchmark-native.c" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/node-uuid/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/node-uuid/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/node-uuid/test/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/node-uuid/test/compare_v1.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/node-uuid/test/test.html" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/aws-sign/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/aws-sign/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/tunnel-agent/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/tunnel-agent/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/License" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/License" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/License" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/.gitignore" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/lib/delayed_stream.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/Readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/common.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/run.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/integration/test-handle-source-errors.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/integration/test-delayed-stream.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/integration/test-proxy-readable.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/integration/test-delayed-stream-auto-pause.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/integration/test-delayed-http-upload.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/integration/test-pipe-resumes.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/integration/test-max-data-size.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/integration/test-delayed-stream-pause.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/lib/combined_stream.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/Readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/node_modules/combined-stream/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/lib/form_data.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/Readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/form-data/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/json-stringify-safe/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/json-stringify-safe/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/json-stringify-safe/stringify.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/json-stringify-safe/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/json-stringify-safe/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/component.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/History.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/benchmark.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/examples.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/Readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/.gitmodules" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/test/parse.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/test/stringify.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/test/browser/qs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/test/browser/jquery.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/test/browser/expect.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/test/browser/qs.css" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/test/browser/mocha.css" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/test/browser/mocha.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/test/browser/index.html" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/qs/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/forever-agent/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/node_modules/forever-agent/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-protocol-changing-redirect.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/ssl/test.crt" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/ssl/npm-ca.crt" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/ssl/ca/ca.csr" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/ssl/ca/server.csr" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/ssl/ca/server.key" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/ssl/ca/server.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/ssl/ca/ca.cnf" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/ssl/ca/ca.srl" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/ssl/ca/server.crt" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/ssl/ca/server.cnf" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/ssl/ca/ca.crl" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/ssl/ca/ca.crt" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/ssl/ca/ca.key" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/ssl/test.key" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-tunnel.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-body.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/unicycle.jpg" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-qs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/googledoodle.jpg" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-defaults.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/run.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/server.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-redirect.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-oauth.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-piped-redirect.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-hawk.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-httpModule.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/squid.conf" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-toJSON.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-basic-auth.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-https.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-follow-all-303.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-https-strict.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-headers.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-digest-auth.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-params.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-pipes.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-s3.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-pool.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-errors.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-proxy.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-timeout.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-form.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/tests/test-follow-all.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/node_modules/request/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/lib/winston/common.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/lib/winston/transports/daily-rotate-file.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/lib/winston/transports/http.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/lib/winston/transports/transport.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/lib/winston/transports/console.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/lib/winston/transports/file.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/lib/winston/transports/memory.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/lib/winston/transports/webhook.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/lib/winston/transports.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/lib/winston/container.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/lib/winston/logger.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/lib/winston/exception.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/lib/winston/config/syslog-config.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/lib/winston/config/npm-config.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/lib/winston/config/cli-config.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/lib/winston/config.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/lib/winston.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/examples/couchdb.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/examples/custom-levels.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/examples/webhook-post.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/examples/raw-mode.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/examples/exception.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/cli-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/logger-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/logger-levels-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/container-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/transports/memory-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/transports/daily-rotate-file-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/transports/console-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/transports/transport.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/transports/webhook-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/transports/file-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/transports/file-maxsize-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/transports/file-maxfiles-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/exception-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/helpers.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/custom-timestamp-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/winston-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/fixtures/keys/agent2-cert.pem" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/fixtures/keys/agent2-key.pem" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/fixtures/logs/.gitkeep" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/fixtures/scripts/default-exceptions.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/fixtures/scripts/unhandle-exceptions.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/fixtures/scripts/log-exceptions.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/fixtures/scripts/exit-on-error.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/fixtures/.gitkeep" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/log-rewriter-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/test/log-exception-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/winston/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/latest" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/nan/include_dirs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/nan/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/nan/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/nan/nan.h" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/nan/build/config.gypi" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/nan/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/nan/.dntrc" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/commander/Readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/commander/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/commander/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/tinycolor/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/tinycolor/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/tinycolor/example.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/tinycolor/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/tinycolor/tinycolor.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/options/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/options/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/options/lib/options.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/options/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/options/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/options/test/options.test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/node_modules/options/test/fixtures/test.conf" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/src/bufferutil.cc" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/src/validation.cc" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/History.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/builderror.log" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/lib/ErrorCodes.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/lib/Receiver.hixie.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/lib/WebSocket.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/lib/Validation.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/lib/BufferUtil.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/lib/BufferPool.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/lib/BufferUtil.fallback.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/lib/browser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/lib/WebSocketServer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/lib/Sender.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/lib/Validation.fallback.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/lib/Receiver.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/lib/Sender.hixie.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/binding.gyp" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/build/config.gypi" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/bin/wscat" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/ws/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/package.json~" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/README.org" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/uglify-js.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/lib/squeeze-more.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/lib/parse-js.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/lib/object-ast.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/lib/process.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/docstyle.css" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/tmp/uglify-hangs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/tmp/liftvars.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/tmp/hoist.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/tmp/uglify-hangs2.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/tmp/goto2.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/tmp/269.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/tmp/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/tmp/instrument.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/tmp/embed-tokens.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/tmp/app.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/tmp/goto.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/tmp/instrument2.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/bin/uglifyjs" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/beautify.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/scripts.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/ifreturn2.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue30.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/array4.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue21.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue54.1.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue68.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/ifreturn.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/const.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue9.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue28.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue53.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue16.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue4.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/var.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue278.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/assignment.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/mangle.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/with.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue11.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/forstatement.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/array2.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue17.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/array3.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/concatstring.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue29.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue48.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue10.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue34.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/if.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue27.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue25.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/empty-blocks.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue20.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/strict-equals.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue13.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue50.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue69.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/issue14.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/null_string.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/whitespace.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/expected/array1.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/ifreturn2.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue30.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/array4.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue21.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue54.1.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue68.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/ifreturn.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/const.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue9.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue28.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue53.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue16.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue4.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/var.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue278.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/assignment.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/mangle.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/with.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue11.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/forstatement.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/array2.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue17.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/array3.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/concatstring.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue29.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue48.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue10.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue34.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/if.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue27.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue25.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/empty-blocks.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue20.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/strict-equals.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue13.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue50.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue69.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/issue14.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/null_string.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/whitespace.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/unit/compress/test/array1.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/test/testparser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/uglify-js/README.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/.bin/wscat" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/.bin/uglifyjs" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/xmlhttprequest/autotest.watchr" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/xmlhttprequest/example/demo.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/xmlhttprequest/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/xmlhttprequest/lib/XMLHttpRequest.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/xmlhttprequest/tests/test-request-protocols.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/xmlhttprequest/tests/testdata.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/xmlhttprequest/tests/test-events.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/xmlhttprequest/tests/test-headers.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/xmlhttprequest/tests/test-constants.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/xmlhttprequest/tests/test-request-methods.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/xmlhttprequest/tests/test-exceptions.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/xmlhttprequest/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/.test.js.un~" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/.package.json.un~" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/.gitignore" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/README" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/tests.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/unicodecategories.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/benchmark.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/test-tokenizer.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/Tokenizer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/test-parser.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/ZeParser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/node_modules/zeparser/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/.index.js.un~" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/Readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/.Readme.md.un~" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/..gitignore.un~" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/node_modules/active-x-obfuscator/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/History.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/component-json/component.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/component-json/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/visionmedia-debug/component.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/visionmedia-debug/debug.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/visionmedia-debug/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/component-emitter/component.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/component-emitter/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/timoxley-to-array/component.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/timoxley-to-array/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/component-bind/component.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/component-bind/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/learnboost-socket.io-protocol/component.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/learnboost-socket.io-protocol/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/learnboost-engine.io-client/component.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/learnboost-engine.io-client/lib/emitter.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/learnboost-engine.io-client/lib/util.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/learnboost-engine.io-client/lib/socket.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/learnboost-engine.io-client/lib/transports/polling-jsonp.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/learnboost-engine.io-client/lib/transports/flashsocket.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/learnboost-engine.io-client/lib/transports/websocket.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/learnboost-engine.io-client/lib/transports/polling-xhr.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/learnboost-engine.io-client/lib/transports/polling.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/learnboost-engine.io-client/lib/transports/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/learnboost-engine.io-client/lib/transport.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/learnboost-engine.io-client/lib/parser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/learnboost-engine.io-client/lib/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/component-json-fallback/component.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/components/component-json-fallback/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/namespace.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/util.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/socket.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/transports/xhr-polling.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/transports/xhr.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/transports/flashsocket.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/transports/websocket.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/transports/htmlfile.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/transports/jsonp-polling.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/build.sh" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/WebSocketMain.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/gsolo/encryption/MD5.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/prng/ARC4.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/prng/IPRNG.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/prng/Random.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/prng/TLSPRF.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/NullPad.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/AESKey.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/CFBMode.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/OFBMode.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/TripleDESKey.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/BlowFishKey.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/IPad.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/dump.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/IStreamCipher.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/CBCMode.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/PKCS5.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/aeskey.pl" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/IVMode.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/DESKey.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/ECBMode.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/XTeaKey.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/SimpleIVMode.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/ISymmetricKey.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/CFB8Mode.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/ICipher.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/SSLPad.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/CTRMode.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/TLSPad.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/symmetric/IMode.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/Crypto.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash/IHash.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash/MD2.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash/MAC.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash/SHABase.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash/SHA1.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash/HMAC.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash/MD5.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash/SHA224.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash/IHMAC.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/hash/SHA256.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/SSLEvent.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/TLSError.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/TLSConfig.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/MACs.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/TLSSocket.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/IConnectionState.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/TLSEvent.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/ISecurityParameters.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/SSLConnectionState.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/TLSSecurityParameters.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/TLSConnectionState.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/CipherSuites.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/KeyExchanges.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/TLSTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/BulkCiphers.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/TLSEngine.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/SSLSecurityParameters.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tls/TLSSocketEvent.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/rsa/RSAKey.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/cert/X509CertificateCollection.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/cert/MozillaRootCertificates.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/cert/X509Certificate.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/CTRModeTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/CBCModeTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/TripleDESKeyTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/BigIntegerTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/TLSPRFTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/ECBModeTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/AESKeyTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/CFB8ModeTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/ARC4Test.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/RSAKeyTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/CFBModeTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/OFBModeTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/SHA1Test.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/MD5Test.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/BlowFishKeyTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/MD2Test.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/ITestHarness.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/SHA256Test.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/DESKeyTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/HMACTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/SHA224Test.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/TestCase.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/crypto/tests/XTeaKeyTest.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/math/NullReduction.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/math/IReduction.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/math/bi_internal.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/math/MontgomeryReduction.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/math/BarrettReduction.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/math/BigInteger.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/math/ClassicReduction.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/Hex.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/Type.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/DER.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/UTCTime.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/PEM.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/PrintableString.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/ObjectIdentifier.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/Integer.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/ByteString.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/Sequence.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/IAsn1Type.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/OID.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/der/Set.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/ArrayUtil.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/Memory.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/hurlant/util/Base64.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/com/adobe/net/proxies/RFC2817Socket.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/WebSocketEvent.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/IWebSocketLogger.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/WebSocketMainInsecure.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/flash-src/WebSocket.as" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/web_socket.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/WebSocketMain.swf" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/sample.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/WebSocketMainInsecure.zip" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/vendor/web-socket-js/swfobject.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/transport.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/events.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/io.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/parser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/lib/json.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/dist/WebSocketMain.swf" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/dist/socket.io.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/dist/WebSocketMainInsecure.swf" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/dist/socket.io.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/bin/builder.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/test/events.test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/test/worker.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/test/node/builder.common.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/test/node/builder.test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/test/parser.test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/test/io.test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/test/socket.test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/socket.io-client/test/util.test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/base64id/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/base64id/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/base64id/lib/base64id.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/base64id/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/policyfile/.gitignore" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/policyfile/doc/index.html" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/policyfile/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/policyfile/lib/server.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/policyfile/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/policyfile/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/policyfile/tests/ssl/ssl.crt" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/policyfile/tests/ssl/ssl.private.key" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/policyfile/tests/unit.test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/policyfile/examples/basic.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/policyfile/examples/basic.fallback.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/policyfile/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/policyfile/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/diff_multi_bench_output.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/changelog.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/benches/stress/speed/plot" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/benches/stress/speed/speed.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/benches/stress/speed/size-rate.png" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/benches/stress/speed/00" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/benches/stress/codec.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/benches/stress/rpushblpop/pub.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/benches/stress/rpushblpop/server.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/benches/stress/rpushblpop/run" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/benches/stress/pubsub/pub.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/benches/stress/pubsub/server.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/benches/stress/pubsub/run" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/benches/reconnect_test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/benches/re_sub_test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/benches/hiredis_parser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/benches/sub_quit_test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/benches/buffer_bench.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/mem.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/generate_commands.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/lib/commands.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/lib/util.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/lib/queue.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/lib/to_array.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/lib/parser/javascript.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/lib/parser/hiredis.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/examples/eval.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/examples/multi.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/examples/mget.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/examples/auth.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/examples/multi2.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/examples/web_server.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/examples/backpressure_drain.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/examples/file.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/examples/psubscribe.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/examples/subqueries.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/examples/pub_sub.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/examples/unix_socket.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/examples/subquery.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/examples/simple.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/examples/sort.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/examples/monitor.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/examples/extend.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/multi_bench.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/node_modules/redis/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/History.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/namespace.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/util.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/static.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/socket.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/transports/websocket/hybi-07-12.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/transports/websocket/hybi-16.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/transports/websocket/default.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/transports/websocket/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/transports/xhr-polling.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/transports/flashsocket.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/transports/http.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/transports/websocket.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/transports/htmlfile.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/transports/http-polling.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/transports/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/transports/jsonp-polling.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/manager.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/stores/redis.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/stores/memory.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/transport.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/store.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/socket.io.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/logger.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/lib/parser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/Readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/benchmarks/runner.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/benchmarks/decode.bench.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/benchmarks/encode.bench.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/socket.io/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/vwebsocket/server.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vwebsocket/socket.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vwebsocket/vlogger-test.log" 
"/usr/local/share/vaclab/nodejs/node_modules/vwebsocket/transport.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vwebsocket/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/vwebsocket/console.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vwebsocket/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/vwebsocket/vlogger-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vwebsocket/winston-mail.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vwebsocket/vWebsocket.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vwebsocket/s.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vwebsocket/index.html" 
"/usr/local/share/vaclab/nodejs/node_modules/vwebsocket/zz" 
"/usr/local/share/vaclab/nodejs/node_modules/vwebsocket/c.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vwebsocket/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/vwebsocket/test/s.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vwebsocket/test/c.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vwebsocket/vWebsocket0.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/debug/node.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/debug/component.json" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/debug/debug.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/debug/node_modules/ms/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/debug/node_modules/ms/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/debug/node_modules/ms/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/debug/node_modules/ms/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/debug/History.md" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/debug/.jshintrc" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/debug/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/debug/browser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/debug/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/debug/Readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/debug/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/commander/Readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/commander/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/commander/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/readme.markdown" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/node_modules/minimist/readme.markdown" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/node_modules/minimist/example/parse.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/node_modules/minimist/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/node_modules/minimist/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/node_modules/minimist/test/default_bool.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/node_modules/minimist/test/parse_modified.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/node_modules/minimist/test/parse.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/node_modules/minimist/test/dotted.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/node_modules/minimist/test/long.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/node_modules/minimist/test/short.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/node_modules/minimist/test/dash.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/node_modules/minimist/test/whitespace.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/node_modules/minimist/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/node_modules/minimist/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/examples/pow.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/bin/cmd.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/bin/usage.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/test/umask_sync.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/test/race.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/test/rel.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/test/return.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/test/perm_sync.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/test/perm.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/test/opts_fs_sync.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/test/opts_fs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/test/sync.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/test/chmod.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/test/root.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/test/umask.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/test/clobber.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/test/mkdirp.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/test/return_sync.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/mkdirp/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/.bin/mkdirp" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/.bin/jade" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/growl/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/growl/History.md" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/growl/lib/growl.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/growl/Readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/growl/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/testing/index.jade" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/testing/user.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/testing/layout.jade" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/testing/user.jade" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/testing/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/testing/head.jade" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/jade.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/jade.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/runtime.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/test.jade" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/runtime.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/commander/History.md" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/commander/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/commander/lib/commander.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/commander/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/commander/Readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/commander/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/commander/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/commander/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/.gitignore.orig" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/examples/pow.js.rej" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/examples/pow.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/examples/pow.js.orig" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/README.markdown" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/test/umask_sync.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/test/race.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/test/rel.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/test/perm_sync.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/test/perm.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/test/sync.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/test/chmod.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/test/umask.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/test/clobber.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/test/mkdirp.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/node_modules/mkdirp/.gitignore.rej" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/jade.md" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/inline-tags.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/jade.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/runtime.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/utils.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/self-closing.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/nodes/node.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/nodes/block.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/nodes/block-comment.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/nodes/mixin.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/nodes/case.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/nodes/doctype.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/nodes/text.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/nodes/code.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/nodes/each.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/nodes/literal.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/nodes/filter.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/nodes/attrs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/nodes/tag.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/nodes/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/nodes/comment.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/compiler.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/parser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/filters.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/doctypes.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/lib/lexer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/bin/jade" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/jade/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/diff/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/diff/diff.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/diff/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/graceful-fs/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/graceful-fs/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/graceful-fs/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/graceful-fs/polyfills.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/graceful-fs/graceful-fs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/graceful-fs/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/graceful-fs/test/readdir-sort.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/graceful-fs/test/open.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/minimatch.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/node_modules/sigmund/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/node_modules/sigmund/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/node_modules/sigmund/sigmund.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/node_modules/sigmund/bench.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/node_modules/sigmund/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/node_modules/sigmund/test/basic.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/CONTRIBUTORS" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/lib/lru-cache.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/test/foreach.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/test/basic.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/node_modules/lru-cache/test/memory-leak.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/test/extglob-ending-with-state-char.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/test/brace-expand.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/test/basic.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/test/defaults.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/minimatch/test/caching.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/inherits/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/inherits/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/inherits/inherits_browser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/inherits/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/inherits/inherits.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/node_modules/inherits/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/examples/usr-local.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/examples/g.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/test/bash-results.json" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/test/00-setup.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/test/root-nomount.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/test/nocase-nomagic.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/test/bash-comparison.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/test/mark.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/test/pause-resume.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/test/root.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/test/globstar-match.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/test/zz-cleanup.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/test/cwd-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/test/stat.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/glob/glob.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/escape-string-regexp/readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/escape-string-regexp/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/node_modules/escape-string-regexp/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/mocha.css" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/runner.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/nyan.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/html.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/landing.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/progress.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/base.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/markdown.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/json-stream.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/list.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/templates/script.html" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/templates/coverage.jade" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/templates/menu.jade" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/templates/style.html" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/xunit.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/html-cov.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/tap.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/doc.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/json-cov.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/json.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/spec.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/reporters/dot.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/hook.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/template.html" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/context.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/utils.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/suite.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/mocha.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/ms.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/interfaces/qunit.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/interfaces/exports.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/interfaces/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/interfaces/tdd.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/interfaces/bdd.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/browser/tty.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/browser/escape-string-regexp.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/browser/fs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/browser/debug.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/browser/path.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/browser/progress.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/browser/events.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/browser/diff.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/browser/glob.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/lib/runnable.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/mocha.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/bin/mocha" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/bin/_mocha" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/images/error.png" 
"/usr/local/share/vaclab/nodejs/node_modules/mocha/images/ok.png" 
"/usr/local/share/vaclab/nodejs/node_modules/.bin/istanbul" 
"/usr/local/share/vaclab/nodejs/node_modules/.bin/mocha" 
"/usr/local/share/vaclab/nodejs/node_modules/.bin/_mocha" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/CHANGELOG.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/public-address/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/public-address/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/public-address/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/public-address/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/passthrough.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/writable.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/transform.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/core-util-is/util.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/core-util-is/float.patch" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/core-util-is/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/core-util-is/lib/util.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/core-util-is/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/isarray/component.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/isarray/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/isarray/build/build.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/isarray/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/isarray/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/string_decoder/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/string_decoder/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/string_decoder/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/string_decoder/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/string_decoder/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/inherits/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/inherits/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/inherits/inherits_browser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/inherits/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/inherits/inherits.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/node_modules/inherits/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/float.patch" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/readable.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/lib/_stream_writable.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/lib/_stream_readable.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/lib/_stream_passthrough.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/lib/_stream_duplex.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/lib/_stream_transform.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/readable-stream/duplex.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/he/man/he.1" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/he/LICENSE-MIT.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/he/he.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/he/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/he/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/he/bin/he" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/.bin/he" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/CHANGELOG.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/node_modules/rai/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/node_modules/rai/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/node_modules/rai/lib/rai.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/node_modules/rai/lib/mockup.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/node_modules/rai/lib/starttls.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/node_modules/rai/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/node_modules/rai/cert/server.key" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/node_modules/rai/cert/server.crt" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/node_modules/rai/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/node_modules/rai/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/node_modules/xoauth2/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/node_modules/xoauth2/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/node_modules/xoauth2/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/node_modules/xoauth2/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/node_modules/xoauth2/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/lib/server.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/lib/simpleserver.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/lib/pool.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/lib/client.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/simplesmtp/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/directmail/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/directmail/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/directmail/lib/queue.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/directmail/lib/mailer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/directmail/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/directmail/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/directmail/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mime/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mime/types/mime.types" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mime/types/node.types" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mime/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mime/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mime/mime.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mime/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/follow-redirects/node_modules/underscore/underscore.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/follow-redirects/node_modules/underscore/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/follow-redirects/node_modules/underscore/underscore-min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/follow-redirects/node_modules/underscore/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/follow-redirects/node_modules/underscore/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/follow-redirects/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/follow-redirects/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/follow-redirects/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/follow-redirects/test/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/follow-redirects/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/dkim-signer/node_modules/punycode/LICENSE-MIT.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/dkim-signer/node_modules/punycode/LICENSE-GPL.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/dkim-signer/node_modules/punycode/punycode.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/dkim-signer/node_modules/punycode/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/dkim-signer/node_modules/punycode/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/dkim-signer/node_modules/punycode/punycode.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/dkim-signer/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/dkim-signer/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/dkim-signer/lib/dkim.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/dkim-signer/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/lib/streams.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/lib/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/lib/extend-node.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/README.md~" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/Changelog.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/encodings/internal.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/encodings/sbcs-data.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/encodings/dbcs-codec.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/encodings/dbcs-data.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/encodings/utf16.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/encodings/utf7.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/encodings/sbcs-data-generated.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/encodings/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/encodings/sbcs-codec.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/encodings/tables/big5-added.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/encodings/tables/shiftjis.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/encodings/tables/eucjp.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/encodings/tables/gb18030-ranges.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/encodings/tables/cp949.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/encodings/tables/cp936.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/encodings/tables/cp950.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/encodings/tables/gbk-added.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/node_modules/iconv-lite/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/lib/encoding.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/encoding/test/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/addressparser/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/addressparser/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/addressparser/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/addressparser/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/node_modules/addressparser/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/lib/content-types.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/lib/content-types-reversed.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/lib/mimelib.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/node_modules/mimelib/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/lib/mailcomposer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/lib/urlfetch.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/lib/topunycode.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/node_modules/mailcomposer/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/lib/nodemailer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/lib/helpers.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/lib/transport.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/lib/xoauth.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/lib/wellknown.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/lib/engines/smtp.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/lib/engines/ses.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/lib/engines/pickup.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/lib/engines/direct.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/lib/engines/stub.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/lib/engines/sendmail.js" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/nodemailer/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/composer.json" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/sauce_connect.log" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/f.coffee" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/component.json" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/.sauce-labs.creds" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/moment.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/bower.json" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/CONTRIBUTING.md" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/min/tests.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/min/moment.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/min/moment-with-langs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/min/langs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/min/moment-with-langs.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/min/langs.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/tasks/history.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/tasks/embed_languages.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/tasks/zones.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/tasks/size.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/tasks/component.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/tasks/check_sauce_creds.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/.vimrc-local" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/ar.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/fr.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/hi.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/sr.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/tzm-la.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/de.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/nn.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/nb.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/he.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/ta.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/cs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/ar-ma.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/fa.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/cv.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/id.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/en-au.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/lv.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/ja.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/gl.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/mk.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/ko.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/eu.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/vi.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/hu.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/br.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/cy.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/eo.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/lb.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/da.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/tzm.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/ka.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/fo.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/bs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/hr.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/lt.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/ms-my.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/bg.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/pt.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/sr-cyr.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/mr.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/zh-tw.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/uz.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/th.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/en-ca.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/pt-br.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/sq.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/ml.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/nl.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/hy-am.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/tl-ph.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/km.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/sv.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/es.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/sk.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/it.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/tr.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/zh-cn.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/en-gb.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/fi.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/et.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/el.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/ca.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/uk.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/fr-ca.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/pl.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/sl.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/ro.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/ne.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/ru.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/lang/is.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/ender.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/package.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/Gruntfile.js" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/foo.coffee" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/moment/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.isobject/node_modules/lodash._objecttypes/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.isobject/node_modules/lodash._objecttypes/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.isobject/node_modules/lodash._objecttypes/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.isobject/node_modules/lodash._objecttypes/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.isobject/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.isobject/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.isobject/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.isobject/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys/node_modules/lodash._isnative/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys/node_modules/lodash._isnative/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys/node_modules/lodash._isnative/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys/node_modules/lodash._isnative/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys/node_modules/lodash._shimkeys/node_modules/lodash._objecttypes/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys/node_modules/lodash._shimkeys/node_modules/lodash._objecttypes/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys/node_modules/lodash._shimkeys/node_modules/lodash._objecttypes/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys/node_modules/lodash._shimkeys/node_modules/lodash._objecttypes/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys/node_modules/lodash._shimkeys/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys/node_modules/lodash._shimkeys/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys/node_modules/lodash._shimkeys/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys/node_modules/lodash._shimkeys/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.keys/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules/lodash._isnative/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules/lodash._isnative/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules/lodash._isnative/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules/lodash._isnative/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules/lodash.noop/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules/lodash.noop/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules/lodash.noop/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules/lodash.noop/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._slice/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._slice/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._slice/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._slice/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules/lodash._isnative/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules/lodash._isnative/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules/lodash._isnative/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules/lodash._isnative/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules/lodash.noop/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules/lodash.noop/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules/lodash.noop/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules/lodash.noop/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules/lodash._isnative/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules/lodash._isnative/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules/lodash._isnative/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules/lodash._isnative/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules/lodash.noop/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules/lodash.noop/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules/lodash.noop/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules/lodash.noop/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash.isfunction/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash.isfunction/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash.isfunction/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash.isfunction/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.support/node_modules/lodash._isnative/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.support/node_modules/lodash._isnative/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.support/node_modules/lodash._isnative/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.support/node_modules/lodash._isnative/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.support/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.support/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.support/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.support/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.identity/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.identity/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.identity/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/node_modules/lodash.identity/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._basecreatecallback/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._objecttypes/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._objecttypes/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._objecttypes/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._objecttypes/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._releasearray/node_modules/lodash._maxpoolsize/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._releasearray/node_modules/lodash._maxpoolsize/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._releasearray/node_modules/lodash._maxpoolsize/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._releasearray/node_modules/lodash._maxpoolsize/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._releasearray/node_modules/lodash._arraypool/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._releasearray/node_modules/lodash._arraypool/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._releasearray/node_modules/lodash._arraypool/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._releasearray/node_modules/lodash._arraypool/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._releasearray/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._releasearray/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._releasearray/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._releasearray/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._getarray/node_modules/lodash._arraypool/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._getarray/node_modules/lodash._arraypool/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._getarray/node_modules/lodash._arraypool/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._getarray/node_modules/lodash._arraypool/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._getarray/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._getarray/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._getarray/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash._getarray/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash.forin/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash.forin/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash.forin/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash.forin/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash.isfunction/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash.isfunction/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash.isfunction/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/node_modules/lodash.isfunction/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash._baseisequal/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.property/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.property/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.property/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/node_modules/lodash.property/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.createcallback/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._objecttypes/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._objecttypes/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._objecttypes/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._objecttypes/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash.keys/node_modules/lodash.isobject/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash.keys/node_modules/lodash.isobject/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash.keys/node_modules/lodash.isobject/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash.keys/node_modules/lodash.isobject/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash.keys/node_modules/lodash._isnative/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash.keys/node_modules/lodash._isnative/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash.keys/node_modules/lodash._isnative/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash.keys/node_modules/lodash._isnative/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash.keys/node_modules/lodash._shimkeys/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash.keys/node_modules/lodash._shimkeys/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash.keys/node_modules/lodash._shimkeys/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash.keys/node_modules/lodash._shimkeys/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash.keys/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash.keys/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash.keys/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash.keys/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules/lodash._isnative/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules/lodash._isnative/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules/lodash._isnative/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules/lodash._isnative/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules/lodash.noop/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules/lodash.noop/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules/lodash.noop/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/node_modules/lodash.noop/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash._setbinddata/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._slice/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._slice/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._slice/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._slice/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash.isobject/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash.isobject/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash.isobject/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash.isobject/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules/lodash._isnative/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules/lodash._isnative/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules/lodash._isnative/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules/lodash._isnative/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules/lodash.noop/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules/lodash.noop/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules/lodash.noop/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/node_modules/lodash.noop/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/node_modules/lodash._basecreate/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basecreatewrapper/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash.isobject/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash.isobject/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash.isobject/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash.isobject/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules/lodash._isnative/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules/lodash._isnative/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules/lodash._isnative/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules/lodash._isnative/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules/lodash.noop/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules/lodash.noop/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules/lodash.noop/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/node_modules/lodash.noop/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/node_modules/lodash._basecreate/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash._basebind/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash.isfunction/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash.isfunction/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash.isfunction/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/node_modules/lodash.isfunction/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/node_modules/lodash._createwrapper/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.bind/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.support/node_modules/lodash._isnative/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.support/node_modules/lodash._isnative/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.support/node_modules/lodash._isnative/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.support/node_modules/lodash._isnative/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.support/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.support/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.support/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.support/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.identity/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.identity/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.identity/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/node_modules/lodash.identity/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/node_modules/lodash._basecreatecallback/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/node_modules/lodash.forown/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.map/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/.bin/xlsx" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/xlsxworker2.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/jszip.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/bower.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/commander/History.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/commander/Readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/commander/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/commander/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/adler-32/adler32.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/adler-32/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/adler-32/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/adler-32/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/ssf.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/colors/colors.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/colors/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/colors/example.html" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/colors/MIT-LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/colors/ReadMe.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/colors/example.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/colors/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/colors/themes/winston-dark.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/colors/themes/winston-light.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/.bin/voc" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/frac/frac.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/frac/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/frac/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/frac/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/frac/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/frac/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/frac/frac.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/frac/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/frac/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/voc/voc.njs" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/voc/marked.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/voc/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/voc/voc.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/voc/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/voc/mkdirp.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/node_modules/voc/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/ssf.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/ssf/bin/ssf.njs" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/.bin/ssf" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/.bin/codepage" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/.bin/cfb" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/passthrough.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/writable.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/transform.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/node_modules/core-util-is/util.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/node_modules/core-util-is/float.patch" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/node_modules/core-util-is/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/node_modules/core-util-is/lib/util.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/node_modules/core-util-is/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/node_modules/isarray/component.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/node_modules/isarray/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/node_modules/isarray/build/build.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/node_modules/isarray/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/node_modules/isarray/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/node_modules/string_decoder/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/node_modules/string_decoder/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/node_modules/string_decoder/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/node_modules/string_decoder/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/node_modules/string_decoder/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/float.patch" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/readable.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/lib/_stream_writable.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/lib/_stream_readable.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/lib/_stream_passthrough.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/lib/_stream_duplex.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/lib/_stream_transform.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/readable-stream/duplex.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/typedarray/readme.markdown" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/typedarray/example/tarray.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/typedarray/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/typedarray/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/typedarray/test/tarray.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/typedarray/test/server/undef_globals.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/typedarray/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/typedarray/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/inherits/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/inherits/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/inherits/inherits_browser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/inherits/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/inherits/inherits.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/node_modules/inherits/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/test/typedarray.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/test/buffer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/test/infer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/test/objects.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/test/nothing.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/test/string.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/test/server/ls.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/test/array.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/concat-stream/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/.bin/voc" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/voc/voc.njs" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/voc/marked.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/voc/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/voc/voc.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/voc/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/voc/mkdirp.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/node_modules/voc/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/cputils.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/cptable.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/dist/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/dist/cpexcel.full.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/codepage/bin/codepage.njs" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/cfb/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/cfb/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/cfb/dist/xlscfb.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/cfb/dist/cfb.min.map" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/cfb/dist/cfb.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/cfb/dist/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/cfb/dist/cfb.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/cfb/cfb.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/cfb/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/cfb/bin/cfb.njs" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/crc-32/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/crc-32/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/crc-32/crc32.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/crc-32/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/crc-32/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/CHANGES.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/.jshintignore" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/vendor/FileSaver.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/.jshintignore" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/HISTORY.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/bower.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/.ndocrc" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/.jshintrc" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/inflate-pako-string/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/inflate-zlib/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/inflate-dankogai/rawinflate.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/inflate-dankogai/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/deflate-pako/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/deflate-dankogai/rawdeflate.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/deflate-dankogai/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/deflate-zlib/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/deflate-pako-string/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/inflate-imaya/node-zlib.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/inflate-imaya/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/inflate-pako-untyped/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/deflate-gildas/deflate.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/deflate-gildas/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/deflate-imaya/node-zlib.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/deflate-imaya/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/inflate-pako/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/implementations/deflate-pako-untyped/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/benchmark.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/samples/lorem_1mb.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/benchmark/profile.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/lib/inflate.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/lib/zlib/inflate.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/lib/zlib/inffast.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/lib/zlib/adler32.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/lib/zlib/gzheader.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/lib/zlib/zstream.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/lib/zlib/crc32.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/lib/zlib/inftrees.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/lib/zlib/trees.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/lib/zlib/deflate.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/lib/zlib/messages.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/lib/zlib/constants.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/lib/deflate.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/lib/utils/common.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/lib/utils/strings.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/dist/pako_deflate.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/dist/pako_deflate.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/dist/pako.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/dist/pako_inflate.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/dist/pako.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/dist/pako_inflate.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/Gruntfile.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/inflate_cover_ported.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/inflate.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/deflate_cover.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/chunks.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/helpers.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/fixtures/gzip-joined.gz" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/fixtures/samples_deflated_raw/sheet2.compressed" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/fixtures/samples_deflated_raw/sheet4.compressed" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/fixtures/samples_deflated_raw/sheet3.compressed" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/fixtures/samples/lorem.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/fixtures/samples/blank.gif" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/fixtures/samples/lorem_en_100k.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/fixtures/samples/utf8.zip" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/fixtures/samples/lorem_utf_100k.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/fixtures/samples/lorem_cat.jpeg" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/fixtures/gzip-headers.gz" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/mocha.opts" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/deflate.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/strings.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/gzip_specials.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/browser/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/test/browser/test.html" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/node_modules/pako/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/.jshintrc" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/LICENSE.markdown" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/index.html.orig" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/object.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/nodeBuffer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/utf8.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/stringReader.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/compressions.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/deprecatedPublicUtils.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/zipEntry.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/load.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/support.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/defaults.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/utils.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/stringWriter.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/license_header.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/crc32.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/signature.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/zipEntries.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/base64.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/compressedObject.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/flate.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/dataReader.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/nodeBufferReader.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/uint8ArrayWriter.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/lib/uint8ArrayReader.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/CHANGES.md.orig" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/README.markdown" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/node_modules/jszip/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/xlsxworker1.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/ods.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/xlsx.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/dist/xlsx.full.min.map" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/dist/jszip.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/dist/xlsx.min.map" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/dist/xlsx.core.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/dist/ods.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/dist/cpexcel.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/dist/xlsx.full.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/dist/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/dist/xlsx.core.min.map" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/dist/xlsx.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/dist/xlsx.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/bin/xlsx.njs" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/xlsx/xlsxworker.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash._objecttypes/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash._objecttypes/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash._objecttypes/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash._objecttypes/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash.keys/node_modules/lodash.isobject/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash.keys/node_modules/lodash.isobject/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash.keys/node_modules/lodash.isobject/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash.keys/node_modules/lodash.isobject/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash.keys/node_modules/lodash._isnative/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash.keys/node_modules/lodash._isnative/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash.keys/node_modules/lodash._isnative/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash.keys/node_modules/lodash._isnative/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash.keys/node_modules/lodash._shimkeys/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash.keys/node_modules/lodash._shimkeys/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash.keys/node_modules/lodash._shimkeys/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash.keys/node_modules/lodash._shimkeys/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash.keys/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash.keys/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash.keys/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/node_modules/lodash.keys/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/LICENSE.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/node_modules/lodash.defaults/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/license.md" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/.jshintrc" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/lib/node-xlsx.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/test/build.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/test/parse.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/test/fixtures/test.xlsx" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/test/fixtures/test.json" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/node-xlsx/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/vlogger.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/composer.json" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/sauce_connect.log" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/component.json" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/.sauce-labs.creds" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/moment.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/bower.json" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/CONTRIBUTING.md" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/min/tests.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/min/moment.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/min/moment-with-langs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/min/langs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/min/moment-with-langs.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/min/langs.min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/tasks/history.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/tasks/embed_languages.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/tasks/zones.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/tasks/size.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/tasks/component.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/tasks/check_sauce_creds.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/.vimrc-local" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/ar.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/fr.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/hi.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/tzm-la.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/de.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/vn.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/nn.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/nb.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/he.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/ta.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/cs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/ar-ma.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/fa.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/cv.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/id.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/en-au.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/lv.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/ja.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/gl.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/mk.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/ko.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/eu.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/hu.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/br.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/cy.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/eo.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/lb.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/da.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/tzm.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/ka.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/fo.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/bs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/hr.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/lt.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/ms-my.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/bg.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/pt.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/mr.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/zh-tw.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/uz.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/th.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/en-ca.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/pt-br.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/sq.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/ml.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/nl.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/hy-am.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/tl-ph.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/sv.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/es.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/sk.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/it.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/tr.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/zh-cn.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/en-gb.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/fi.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/et.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/el.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/ca.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/uk.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/fr-ca.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/pl.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/sl.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/ro.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/rs.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/ne.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/ru.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/lang/is.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/ender.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/package.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/Gruntfile.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/foo.coffee" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/node_modules/moment/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/vlogger-test.log" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/vlogger-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/zz" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/vlogger/test/vlogger-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/temp/node_modules/.bin/rimraf" 
"/usr/local/share/vaclab/nodejs/node_modules/temp/node_modules/rimraf/rimraf.js" 
"/usr/local/share/vaclab/nodejs/node_modules/temp/node_modules/rimraf/AUTHORS" 
"/usr/local/share/vaclab/nodejs/node_modules/temp/node_modules/rimraf/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/temp/node_modules/rimraf/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/temp/node_modules/rimraf/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/temp/node_modules/rimraf/test/test-async.js" 
"/usr/local/share/vaclab/nodejs/node_modules/temp/node_modules/rimraf/test/run.sh" 
"/usr/local/share/vaclab/nodejs/node_modules/temp/node_modules/rimraf/test/test-sync.js" 
"/usr/local/share/vaclab/nodejs/node_modules/temp/node_modules/rimraf/test/setup.sh" 
"/usr/local/share/vaclab/nodejs/node_modules/temp/node_modules/rimraf/bin.js" 
"/usr/local/share/vaclab/nodejs/node_modules/temp/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/temp/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/temp/lib/temp.js" 
"/usr/local/share/vaclab/nodejs/node_modules/temp/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/temp/examples/pdfcreator.js" 
"/usr/local/share/vaclab/nodejs/node_modules/temp/examples/grepcount.js" 
"/usr/local/share/vaclab/nodejs/node_modules/temp/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/temp/test/temp-test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/temp/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/underscore/underscore.js" 
"/usr/local/share/vaclab/nodejs/node_modules/underscore/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/underscore/underscore-min.js" 
"/usr/local/share/vaclab/nodejs/node_modules/underscore/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/underscore/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/vxi11/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/vxi11/lib/vxi11.js" 
"/usr/local/share/vaclab/nodejs/node_modules/vxi11/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/vxi11/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/vxi11/NOTIZEN" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/oauth-sign/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/oauth-sign/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/oauth-sign/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/oauth-sign/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/oauth-sign/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/mime/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/mime/types/mime.types" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/mime/types/node.types" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/mime/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/mime/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/mime/mime.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/mime/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/example/usage.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/boom/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/boom/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/boom/lib/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/boom/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/boom/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/boom/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/boom/test/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/boom/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/boom/images/boom.png" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/boom/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/sntp/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/sntp/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/sntp/lib/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/sntp/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/sntp/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/sntp/examples/time.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/sntp/examples/offset.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/sntp/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/sntp/test/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/sntp/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/sntp/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/hoek/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/hoek/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/hoek/lib/escape.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/hoek/lib/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/hoek/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/hoek/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/hoek/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/hoek/test/modules/test2.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/hoek/test/modules/test3.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/hoek/test/modules/test1.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/hoek/test/escaper.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/hoek/test/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/hoek/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/hoek/images/hoek.png" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/hoek/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/cryptiles/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/cryptiles/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/cryptiles/lib/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/cryptiles/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/cryptiles/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/cryptiles/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/cryptiles/test/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/cryptiles/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/node_modules/cryptiles/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/lib/server.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/lib/utils.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/lib/crypto.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/lib/browser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/lib/client.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/lib/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/test/uri.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/test/readme.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/test/server.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/test/utils.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/test/message.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/test/crypto.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/test/browser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/test/client.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/test/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/images/logo.png" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/images/hawk.png" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/hawk/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/.dir-locals.el" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/http_signing.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/man/man3ctype/ctio.3ctype" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/README" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/ctype.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tools/jsl.conf" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tools/jsstyle" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctype/tst.basicr.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctype/tst.readSize.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctype/tst.oldwrite.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctype/tst.basicw.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctype/tst.endian.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctype/tst.writeStruct.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctype/tst.structw.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctype/tst.char.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctio/float/tst.wfloat.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctio/float/tst.rfloat.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctio/uint/tst.ruint.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctio/uint/tst.roundtrip.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctio/uint/tst.64.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctio/uint/tst.wuint.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctio/int/tst.wint.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctio/int/tst.wbounds.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctio/int/tst.64.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctio/int/tst.rint.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctf/psinfo.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctf/tst.float.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctf/tst.struct.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctf/int.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctf/tst.fail.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctf/tst.int.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctf/tst.psinfo.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctf/struct.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctf/typedef.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctf/float.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/tst/ctf/tst.typedef.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/ctf.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/ctio.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/CHANGELOG" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/ctype/README.old" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/assert-plus/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/assert-plus/assert.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/assert-plus/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/asn1/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/asn1/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/asn1/lib/ber/reader.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/asn1/lib/ber/errors.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/asn1/lib/ber/types.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/asn1/lib/ber/writer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/asn1/lib/ber/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/asn1/lib/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/asn1/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/asn1/tst/ber/reader.test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/asn1/tst/ber/writer.test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/node_modules/asn1/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/lib/util.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/lib/signer.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/lib/parser.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/lib/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/lib/verify.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/http-signature/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/node-uuid/component.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/node-uuid/uuid.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/node-uuid/LICENSE.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/node-uuid/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/node-uuid/benchmark/bench.gnu" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/node-uuid/benchmark/bench.sh" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/node-uuid/benchmark/benchmark.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/node-uuid/benchmark/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/node-uuid/benchmark/benchmark-native.c" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/node-uuid/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/node-uuid/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/node-uuid/test/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/node-uuid/test/compare_v1.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/node-uuid/test/test.html" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tunnel-agent/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tunnel-agent/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tunnel-agent/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tunnel-agent/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/aws-sign2/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/aws-sign2/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/aws-sign2/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/aws-sign2/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/License" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/async/component.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/async/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/async/lib/async.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/async/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/async/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/async/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/License" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/License" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/.gitignore" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/lib/delayed_stream.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/Readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/common.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/run.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/integration/test-handle-source-errors.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/integration/test-delayed-stream.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/integration/test-proxy-readable.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/integration/test-delayed-stream-auto-pause.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/integration/test-delayed-http-upload.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/integration/test-pipe-resumes.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/integration/test-max-data-size.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/node_modules/delayed-stream/test/integration/test-delayed-stream-pause.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/lib/combined_stream.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/Readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/node_modules/combined-stream/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/lib/form_data.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/Readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/form-data/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/json-stringify-safe/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/json-stringify-safe/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/json-stringify-safe/stringify.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/json-stringify-safe/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/json-stringify-safe/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/qs/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/qs/Readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/qs/.gitmodules" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/qs/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/qs/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/forever-agent/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/forever-agent/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/forever-agent/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/forever-agent/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tough-cookie/test.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tough-cookie/node_modules/punycode/LICENSE-MIT.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tough-cookie/node_modules/punycode/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tough-cookie/node_modules/punycode/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tough-cookie/node_modules/punycode/punycode.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tough-cookie/.jshintrc" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tough-cookie/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tough-cookie/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tough-cookie/public-suffix.txt" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tough-cookie/lib/memstore.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tough-cookie/lib/store.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tough-cookie/lib/cookie.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tough-cookie/lib/pubsuffix.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tough-cookie/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tough-cookie/generate-pubsuffix.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tough-cookie/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/node_modules/tough-cookie/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/request/README.md" 
"/usr/local/share/vaclab/nodejs/node_modules/request/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/request/lib/debug.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/lib/copy.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/lib/optional.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/lib/getSafe.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/lib/cookies.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/LICENSE" 
"/usr/local/share/vaclab/nodejs/node_modules/request/package.json" 
"/usr/local/share/vaclab/nodejs/node_modules/request/request.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/dns-request.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/index.js" 
"/usr/local/share/vaclab/nodejs/node_modules/request/.travis.yml" 
"/usr/local/share/vaclab/nodejs/node_modules/stack-trace/License" 
"/usr/local/share/vaclab/nodejs/node_modules/stack-trace/.npmignore" 
"/usr/local/share/vaclab/nodejs/node_modules/stack-trace/lib/stack-trace.js" 
"/usr/local/share/vaclab/nodejs/node_modules/stack-trace/Makefile" 
"/usr/local/share/vaclab/nodejs/node_modules/stack-trace/Readme.md" 
"/usr/local/share/vaclab/nodejs/node_modules/stack-trace/package.json" 
"/usr/local/share/vaclab/nodejs/latex.js" 
"/usr/local/share/vaclab/nodejs/http.js" 
"/usr/local/share/vaclab/nodejs/utils.js" 
"/usr/local/share/vaclab/nodejs/relayServer.js" 
"/usr/local/share/vaclab/nodejs/vlLogging.js" 
"/usr/local/share/vaclab/nodejs/email.js" 
"/usr/local/share/vaclab/nodejs/relay.js" 
"/usr/local/share/vaclab/nodejs/ldap.js" 
"/usr/local/share/vaclab/nodejs/config.js" 
"/usr/local/share/vaclab/nodejs/vxi.js" 
"/usr/local/share/vaclab/nodejs/relay-add.js" 
"/usr/local/share/vaclab/nodejs/tools.js" 
"/usr/local/bin/vlLogging" 
"/etc/init/relayServer.conf" 
%config(noreplace) 
%changelog
* Tue Mar 03 2015 Rolf.Niepraschk@ptb.de
- "UDP" kann auch empfangen. Timeout-Logik

* Tue Feb 24 2015 Rolf.Niepraschk@ptb.de
- html-Erzeugung zur Dokumentation

* Tue Feb 24 2015 Rolf.Niepraschk@ptb.de
- update "node-xlsx"; Funktionskommentare ergänzt

* Tue Feb 24 2015 Rolf.Niepraschk@ptb.de
- logger-Definition nach "config.js"

* Mon Feb 23 2015 Rolf.Niepraschk@ptb.de
- Fehlerbehandlung bei "external" korrigiert.

* Fri Feb 20 2015 Rolf.Niepraschk@ptb.de
- Neue Version vxi11-Bibliothek ("null" bei fehlender Geräteantwort)

* Fri Feb 13 2015 Rolf.Niepraschk@ptb.de
- "VxiTimeout=0" (Behandlung von fälschlichen Timeout-Meldungen)

* Mon Dec 08 2014 Rolf.Niepraschk@ptb.de
- "relayServer.conf" (upstart, Ubuntu)

* Mon Oct 20 2014 Rolf.Niepraschk@ptb.de
- gendertes vxi11-Modul (REQUEST_SIZE = 10000)

* Tue Sep 02 2014 Rolf.Niepraschk@ptb.de
- Code vom gitlab-hooks-Server weg; sonstige Bereinigung; neuer Name "relayServer"

* Mon Sep 01 2014 Rolf.Niepraschk@ptb.de
- Server für gitlab hooks lahmgelegt; später Extrapaket.

* Thu Aug 21 2014 Rolf.Niepraschk@ptb.de
- Korrigierte Version von "vxi11.js"

* Mon Aug 18 2014 Rolf.Niepraschk@ptb.de
- Fehler in "vxi.js" ("timeout"), Sonderbehandlung "VxiTimeout=0"

* Tue Jul 01 2014 Rolf.Niepraschk@ptb.de
- Error-Meldungen ("vxi", "tcp", "udp") verbessert

* Wed Jun 25 2014 Rolf.Niepraschk@ptb.de
- VXI-11-node-Module: Fehler "socket.destroy()"

* Mon Jun 02 2014 Rolf.Niepraschk@ptb.de
- Weitere Parameter fr "vxi11.js"

* Tue May 27 2014 Rolf.Niepraschk@ptb.de
- "getVaclabServer" zugefgt

* Thu May 22 2014 Rolf.Niepraschk@ptb.de
- VXI-11-Modul: encoding ('utf8', 'base64', 'binary')

* Wed May 21 2014 Rolf.Niepraschk@ptb.de
- VXI-11-Modul: "socket.end()" --> "socket.destroy()"

* Tue May 13 2014 Rolf.Niepraschk@ptb.de
- verbessertes VXI-11-Modul

* Mon May 12 2014 Rolf.Niepraschk@ptb.de
- timestamp verbessert

* Fri May 09 2014 Rolf.Niepraschk@ptb.de
- "ShortFormat"

* Thu May 08 2014 Rolf.Niepraschk@ptb.de
- http-Header-Erzeugung gendert; excel-Erzeugung ("XLSX-OUT" und "XLSX-IN")

* Tue May 06 2014 Rolf.Niepraschk@ptb.de
- Read-Error-Nummer

* Mon May 05 2014 Rolf.Niepraschk@ptb.de
- "noarch", timeout-Fehler

* Tue Apr 29 2014 Rolf.Niepraschk@ptb.de
- Node.js-Modul "vxi11"; C-Programm beseitigt.

* Tue Apr 01 2014 Rolf.Niepraschk@ptb.de
- login-Shell in "NodejsServers.service"

* Mon Mar 31 2014 Rolf.Niepraschk@ptb.de
- Umstellung auf systemd

* Fri Mar 21 2014 Rolf.Niepraschk@ptb.de
- Action "UDP"

* Thu Mar 20 2014 Rolf.Niepraschk@ptb.de
- Ergnzungen in "relay-add.js"

* Tue Feb 11 2014 Rolf.Niepraschk@ptb.de
- Im Startscript Runlevel 2 zugefgt

* Fri Jan 24 2014 Rolf.Niepraschk@ptb.de
- Neuer logger-Transport "vWebsocket". Zugriff nun via "vlLogging".

* Tue Dec 03 2013 Rolf.Niepraschk@ptb.de
- TEX wiederbelebt, umstrukturiert/vereinheitlicht.

* Tue Nov 05 2013 Rolf.Niepraschk@ptb.de
- Undefinierte Funktion "fdebug"

* Fri Oct 18 2013 Rolf.Niepraschk@ptb.de
- Jetzt logger-Funktion (winston)

* Fri Oct 11 2013 Rolf.Niepraschk@ptb.de
- utils.js: "repeat" umgeschrieben, wegen Fehlverhaltens

* Wed Oct 09 2013 Rolf.Niepraschk@ptb.de
- Update "gitlabhook"

* Tue Oct 08 2013 Rolf.Niepraschk@ptb.de
- GitLab-Webhook-Server (Port 3420) zugefügt.

* Thu Sep 19 2013 Rolf.Niepraschk@ptb.de
- Änderung von DEFAULT_TCP_TIMEOUT rückgängig (2000ms)

* Wed Sep 18 2013 Rolf.Niepraschk@ptb.de
- Neue intere "action" "_os_release"

* Thu Feb 14 2013 Rolf.Niepraschk@ptb.de
- TCP-Problem (vermutl. bei neunen node-Versionen) behoben.

* Thu Jan 17 2013 Rolf.Niepraschk@ptb.de
- js-Code weitgehend dokumentiert und formatiert.
- Erzeugung von temporärer Datei ausgelagert ("tools.createTempFile")

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

