%define build_test 0

# commandline overrides:
# rpm -ba|--rebuild --with 'xxx'
%{?_with_test: %{expand: %%global build_test 1}}
%{?_without_test: %{expand: %%global build_test 0}}

%define TAG Mandriva Linux
%define BASEPRODUCT Apache

Summary:	The most widely used Web server on the Internet
Name:		apache
Version:	2.2.4
Release:	%mkrel 12
Group:		System/Servers
License:	Apache License
URL:		http://www.apache.org
Source0:	http://archive.apache.org/dist/httpd/httpd-%{version}.tar.gz
Source1:	http://archive.apache.org/dist/httpd/httpd-%{version}.tar.gz.asc
Source2:	apache-README.urpmi
Source3:	apache2_transparent_png_icons.tar.bz2
Source4: 	perl-framework.tar.bz2
Source9: 	htcacheclean.init
Source10: 	htcacheclean.sysconfig
Source30:	30_mod_proxy.conf
Source31:	31_mod_proxy_ajp.conf
Source40: 	40_mod_ssl.conf
Source41: 	41_mod_ssl.default-vhost.conf
Source45: 	45_mod_dav.conf
Source46: 	46_mod_ldap.conf
Source47: 	47_mod_authnz_ldap.conf
Source55:	55_mod_cache.conf
Source56:	56_mod_disk_cache.conf
Source57:	57_mod_mem_cache.conf
Source58:	58_mod_file_cache.conf
Source59:	59_mod_deflate.conf
Source60:	60_mod_dbd.conf
Source61:	61_mod_authn_dbd.conf
Source67:	67_mod_userdir.conf
Source68:	default-vhosts.conf
Source100:	buildconf
Patch0:		httpd-2.0.45-deplibs.patch
Patch1:		httpd-encode.diff
Patch2:		httpd-2.0.40-xfsz.patch
Patch3:		httpd-2.0.48-corelimit.patch
Patch4:		httpd-2.0.48-debuglog.patch
# http://lists.debian.org/debian-apache/2003/11/msg00109.html
Patch5:		httpd-2.0.48-bsd-ipv6-fix.diff
# OE: prepare for the mod_limitipconn module found here:
# http://dominia.org/djao/limitipconn.html
Patch6:		apachesrc.diff
# JMD: fix suexec path so we can have both versions of Apache and both
# versions of suexec
Patch7:		apache2-suexec.patch
Patch8:		httpd-2.1.10-apxs.patch
Patch9:		httpd-2.1.10-disablemods.patch
Patch10:	httpd-2.1.10-pod.patch
Patch11:	httpd-2.2.0-mod_ssl_memcache.diff
# http://qa.mandriva.com/show_bug.cgi?id=19542
Patch12:	httpd-2.2.2-french_fixes.diff
Patch13:	httpd-2.2.0-authnoprov.patch
Patch14:	httpd-2.2.4-mod_rewrite-fcgi.diff
# http://issues.apache.org/bugzilla/show_bug.cgi?id=32524
Patch15:	httpd-ab_source_address.diff
# speedups by Allen Pulsifer
Patch16:	httpd-2.2.4-fix_extra_htaccess_check.diff
# security fixes
Patch50:	apache-2.2.4-CVE-2007-1862.diff
# http://home.samfundet.no/~sesse/mpm-itk/
Patch100:	apache2.2-mpm-itk-20070425-00.diff
BuildRequires:	apr-devel >= 1:1.2.2
BuildRequires:	apr-util-devel >= 1.2.2
BuildRequires:	apr_memcache-devel >= 0.7.0
BuildRequires:	distcache-devel
BuildRequires:	byacc
BuildRequires:	db4-devel
BuildRequires:	expat-devel
BuildRequires:	gdbm-devel
BuildRequires:	libsasl-devel
BuildRequires:	libtool >= 1.4.2
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel >= 5.0
BuildRequires:	perl >= 0:5.600
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
BuildRequires:	lynx
BuildRequires:	libcap-devel
%if %{build_test}
BuildRequires:	perl-CGI >= 1:3.11
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-libwww-perl
BuildRequires:	perl-Tie-IxHash
BuildRequires:	perl-URI
BuildRequires:	perl-BSD-Resource
#BuildRequires:	subversion
BuildRequires:	perl-HTTP-DAV
BuildRequires:	perl-doc
%endif
%if %mdkversion >= 1020
BuildRequires:	multiarch-utils >= 1.0.3
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package contains the main binary of apache, a powerful, full-featured,
efficient and freely-available Web server. Apache is also the most popular Web
server on the Internet.

This version of apache is fully modular, and many modules are available in
pre-compiled formats, like PHP and mod_auth_external.

Check for available Apache modules for Mandriva Linux at:
http://nux.se/apache/
(most of them can be installed from the contribs repository)

%package	mpm-prefork
Summary:	Implements a non-threaded, pre-forking web server (stable)
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre):	apache-conf >= %{version}
Requires(pre):	apache-base = %{version}-%{release}
Requires(pre):	apache-modules = %{version}-%{release}
Requires:	apache-conf >= %{version}
Requires:	apache-base = %{version}-%{release}
Requires:	apache-modules = %{version}-%{release}
Provides:	webserver
Provides:	apache = %{version}-%{release}, apache-mpm = %{version}-%{release}

%description	mpm-prefork
This Multi-Processing Module (MPM) implements a non-threaded, pre-forking web
server that handles requests in a manner similar to Apache 1.3. It is
appropriate for sites that need to avoid threading for compatibility with
non-thread-safe libraries. It is also the best MPM for isolating each request,
so that a problem with a single request will not affect any other.

This MPM is very self-regulating, so it is rarely necessary to adjust its
configuration directives. Most important is that MaxClients be big enough to
handle as many simultaneous requests as you expect to receive, but small enough
to assure that there is enough physical RAM for all processes.

Check for available Apache modules here: http://nux.se/apache/

%package	mpm-worker
Summary:	Implements a hybrid multi-threaded multi-process web server (experimental)
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre):	apache-conf >= %{version}
Requires(pre):	apache-base = %{version}-%{release}
Requires(pre):	apache-modules = %{version}-%{release}
Requires:	apache-conf >= %{version}
Requires:	apache-base = %{version}-%{release}
Requires:	apache-modules = %{version}-%{release}
Provides:	webserver
Provides:	apache = %{version}-%{release}, apache-mpm = %{version}-%{release}
Conflicts:	apache-mod_php apache-mod_php4 apache-mod_perl apache-mod_python

%description	mpm-worker
This Multi-Processing Module (MPM) implements a hybrid multi-process
multi-threaded server. By using threads to serve requests, it is able to serve
a large number of requests with less system resources than a process-based
server. Yet it retains much of the stability of a process-based server by
keeping multiple processes available, each with many threads.

The most important directives used to control this MPM are ThreadsPerChild,
which controls the number of threads deployed by each child process and
MaxClients, which controls the maximum total number of threads that may be
launched.

This package contains the main binary of apache, a powerful, full-featured,
efficient and freely-available Web server. Apache is also the most popular Web
server on the Internet.

This version of apache is fully modular, and many modules are available in
pre-compiled formats, like PHP and mod_auth_external.

Check for available Apache modules here: http://nux.se/apache/

I M P O R T A N T
-----------------
Note that the worker mpm (this package) requires thread safe modules. This 
package is totally experimental and may not be stable or suitable at any time,
in any way, or for any kind production usage. Be warned. You must manually
add HTTPD="/usr/sbin/httpd-worker" in the /etc/sysconfig/httpd configuration
file to be able to use this MPM.

%package	mpm-event
Summary:	Implements a hybrid multi-threaded multi-process web server (experimental)
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre):	apache-conf >= %{version}
Requires(pre):	apache-base = %{version}-%{release}
Requires(pre):	apache-modules = %{version}-%{release}
Requires:	apache-conf >= %{version}
Requires:	apache-base = %{version}-%{release}
Requires:	apache-modules = %{version}-%{release}
Provides:	webserver
Provides:	apache = %{version}-%{release}, apache-mpm = %{version}-%{release}
Conflicts:	apache-mod_php apache-mod_php4 apache-mod_perl apache-mod_python

%description	mpm-event
The event Multi-Processing Module (MPM) is designed to allow more requests to
be served simultaneously by passing off some processing work to supporting
threads, freeing up the main threads to work on new requests. It is based on
the worker MPM, which implements a hybrid multi-process multi-threaded server.
Run-time configuration directives are identical to those provided by worker.

This package contains the main binary of apache, a powerful, full-featured,
efficient and freely-available Web server. Apache is also the most popular Web
server on the Internet.

This version of apache is fully modular, and many modules are available in
pre-compiled formats, like PHP and mod_auth_external.

Check for available Apache modules here: http://nux.se/apache/

I M P O R T A N T
-----------------
Note that the worker mpm (this package) requires thread safe modules. This 
package is totally experimental and may not be stable or suitable at any time,
in any way, or for any kind production usage. Be warned. You must manually
add HTTPD="/usr/sbin/httpd-event" in the /etc/sysconfig/httpd configuration
file to be able to use this MPM.

%package	mpm-itk
Summary:	Implements a non-threaded, pre-forking web server (experimental)
Group:		System/Servers
URL:		http://home.samfundet.no/~sesse/mpm-itk/
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre):	apache-conf >= %{version}
Requires(pre):	apache-base = %{version}-%{release}
Requires(pre):	apache-modules = %{version}-%{release}
Requires:	apache-conf >= %{version}
Requires:	apache-base = %{version}-%{release}
Requires:	apache-modules = %{version}-%{release}
Provides:	webserver
Provides:	apache = %{version}-%{release}, apache-mpm = %{version}-%{release}

%description	mpm-itk
apache-mpm-itk (just mpm-itk for short) is an MPM (Multi-Processing Module) for
the Apache 2 web server (which you've probably heard of :-) ). mpm-itk allows
you to run each of your vhost under a separate uid and gid -- in short, the
scripts and configuration files for one vhost no longer have to be readable for
all the other vhosts.

There are already MPMs available that do this, namely the perchild and Metux
MPMs (the latter being based on the former, which is included in the standard
Apache 2 tree). However, both have their sets of problems; for instance, both
are threaded, which can be a problem for many extension modules. Second, AFAIK
both have issues with listening on multiple ports (ie. SSL etc), and I don't
know how well they really perform in practice. (If you only run CGI scripts,
suexec will also probably solve most of your problems.)

mpm-itk is based on the traditional prefork MPM, which means it's non-threaded;
in short, this means you can run non-thread-aware code (like many PHP
extensions) without problems. (On the other hand, you lose out to any
performance benefit you'd get with threads, of course; you'd have to decide for
yourself if that's worth it or not.)

I M P O R T A N T
-----------------
This package is totally experimental and may not be stable or suitable at any
time, in any way, or for any kind production usage. Be warned. You must
manually add HTTPD="/usr/sbin/httpd-itk" in the /etc/sysconfig/httpd
configuration file to be able to use this MPM.

%package	base
Summary:	Common files and utilities for apache
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper

%description	base
This package contains the apache utilities such as Apache Bench (ab) for stress
testing your apache installation and several tools for managing user databases,
access control, the apache logs and more.

%package	modules
Summary:	Standard modules for apache
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires:	apache-mpm = %{version}-%{release}
Provides:	apache-mod_actions = %{version}
Provides:	apache-mod_alias = %{version}
Provides:	apache-mod_asis = %{version}
Provides:	apache-mod_auth_basic = %{version}
Provides:	apache-mod_auth_digest = %{version}
Provides:	apache-mod_authn_anon = %{version}
Provides:	apache-mod_authn_dbm = %{version}
Provides:	apache-mod_authn_default = %{version}
Provides:	apache-mod_authn_file = %{version}
Provides:	apache-mod_authz_dbm = %{version}
Provides:	apache-mod_authz_default = %{version}
Provides:	apache-mod_authz_groupfile = %{version}
Provides:	apache-mod_authz_host = %{version}
Provides:	apache-mod_authz_owner = %{version}
Provides:	apache-mod_authz_user = %{version}
Provides:	apache-mod_autoindex = %{version}
Provides:	apache-mod_bucketeer = %{version}
Provides:	apache-mod_case_filter = %{version}
Provides:	apache-mod_case_filter_in = %{version}
Provides:	apache-mod_cern_meta = %{version}
Provides:	apache-mod_cgi = %{version}
Provides:	apache-mod_cgid = %{version}
Provides:	apache-mod_charset_lite = %{version}
Provides:	apache-mod_deflate = %{version}
Provides:	apache-mod_dir = %{version}
Provides:	apache-mod_dumpio = %{version}
Provides:	apache-mod_echo = %{version}
Provides:	apache-mod_env = %{version}
Provides:	apache-mod_example = %{version}
Provides:	apache-mod_expires = %{version}
Provides:	apache-mod_ext_filter = %{version}
Provides:	apache-mod_filter = %{version}
Provides:	apache-mod_headers = %{version}
Provides:	apache-mod_ident = %{version}
Provides:	apache-mod_imagemap = %{version}
Provides:	apache-mod_include = %{version}
Provides:	apache-mod_info = %{version}
Provides:	apache-mod_log_config = %{version}
Provides:	apache-mod_log_forensic = %{version}
Provides:	apache-mod_logio = %{version}
Provides:	apache-mod_mime_magic = %{version}
Provides:	apache-mod_mime = %{version}
Provides:	apache-mod_negotiation = %{version}
Provides:	apache-mod_optional_fn_export = %{version}
Provides:	apache-mod_optional_fn_import = %{version}
Provides:	apache-mod_optional_hook_export = %{version}
Provides:	apache-mod_optional_hook_import = %{version}
Provides:	apache-mod_rewrite = %{version}
Provides:	apache-mod_setenvif = %{version}
Provides:	apache-mod_speling = %{version}
Provides:	apache-mod_status = %{version}
Provides:	apache-mod_unique_id = %{version}
Provides:	apache-mod_usertrack = %{version}
Provides:	apache-mod_version = %{version}
Provides:	apache-mod_vhost_alias = %{version}
# these has been removed or has new names in 2.2.0
Obsoletes:	apache-mod_access apache-mod_imap apache-mod_auth apache-mod_auth_anon apache-mod_auth_dbm apache-mod_auth_digest

%description	modules
This package contains standard modules for apache. It is required
for normal operation of the web server.

%package	mod_dav
Summary:	Distributed Authoring and Versioning (WebDAV)
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre):	apache-conf >= %{version}
Requires(pre):	apache-base = %{version}-%{release}
Requires(pre):	apache-modules = %{version}-%{release}
Requires:	apache-conf >= %{version}
Requires:	apache-base = %{version}-%{release}
Requires:	apache-modules = %{version}-%{release}
Provides:	apache-mod_dav_fs = %{version}
Provides:	apache-mod_dav_lock = %{version}

%description	mod_dav
This module provides class 1 and class 2 WebDAV ('Web-based Distributed
Authoring and Versioning') functionality for Apache.

This extension to the HTTP protocol allows creating, moving, copying, and
deleting resources and collections on a remote web server.

%package	mod_ldap
Summary:	LDAP connection pooling and result caching DSO:s
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre):	apache-conf >= %{version}
Requires(pre):	apache-base = %{version}-%{release}
Requires(pre):	apache-modules = %{version}-%{release}
Requires:	apache-conf >= %{version}
Requires:	apache-base = %{version}-%{release}
Requires:	apache-modules = %{version}-%{release}
Provides:	apache-mod_authnz_ldap = %{version}
Obsoletes:	apache-mod_auth_ldap

%description	mod_ldap
This module was created to improve the performance of websites relying on
backend connections to LDAP servers. In addition to the functions provided by
the standard LDAP libraries, this module adds an LDAP connection pool and an
LDAP shared memory cache.

%package	mod_cache
Summary:	Content cache keyed to URIs
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre):	apache-conf >= %{version}
Requires(pre):	apache-base = %{version}-%{release}
Requires(pre):	apache-modules = %{version}-%{release}
Requires:	apache-conf >= %{version}
Requires:	apache-base = %{version}-%{release}
Requires:	apache-modules = %{version}-%{release}

%description	mod_cache
mod_cache implements an RFC 2616 compliant HTTP content cache that can be used
to cache either local or proxied content. mod_cache requires the services of
one or more storage management modules.

Two storage management modules are included in the base Apache distribution:

 * mod_disk_cache - implements a disk based storage manager for
   use with mod_proxy.
 * mod_mem_cache - implements an in-memory based storage manager.

mod_mem_cache can be configured to operate in two modes: caching open file
descriptors or caching objects in heap storage.

mod_mem_cache is most useful when used to cache locally generated content or to
cache backend server content for mod_proxy configured for ProxyPass (aka
reverse proxy)

%package	mod_disk_cache
Summary:	Implements a disk based storage manager
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre):	apache-conf >= %{version}
Requires(pre):	apache-base = %{version}-%{release}
Requires(pre):	apache-modules = %{version}-%{release}
Requires(pre):	apache-mod_cache = %{version}-%{release}
Requires:	apache-conf >= %{version}
Requires:	apache-base = %{version}-%{release}
Requires:	apache-modules = %{version}-%{release}
Requires:	apache-mod_cache = %{version}-%{release}
Requires:	apache-htcacheclean = %{version}-%{release}

%description	mod_disk_cache
mod_disk_cache implements a disk based storage manager. It is primarily of use
in conjunction with mod_proxy.

Content is stored in and retrieved from the cache using URI based keys. Content
with access protection is not cached.

%package	mod_mem_cache
Summary:	Implements a memory based storage manager
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre):	apache-conf >= %{version}
Requires(pre):	apache-base = %{version}-%{release}
Requires(pre):	apache-modules = %{version}-%{release}
Requires(pre):	apache-mod_cache = %{version}-%{release}
Requires:	apache-conf >= %{version}
Requires:	apache-base = %{version}-%{release}
Requires:	apache-modules = %{version}-%{release}
Requires:	apache-mod_cache = %{version}-%{release}

%description	mod_mem_cache
This module requires the service of mod_cache. It acts as a support module for
mod_cache and provides a memory based storage manager. mod_mem_cache can be
configured to operate in two modes: caching open file descriptors or caching
objects in heap storage. mod_mem_cache is most useful when used to cache
locally generated content or to cache backend server content for mod_proxy
configured for ProxyPass (aka reverse proxy).

Content is stored in and retrieved from the cache using URI based keys. Content
with access protection is not cached.

%package	mod_file_cache
Summary:	Caches a static list of files in memory
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre):	apache-conf >= %{version}
Requires(pre):	apache-base = %{version}-%{release}
Requires(pre):	apache-modules = %{version}-%{release}
Requires:	apache-conf >= %{version}
Requires:	apache-base = %{version}-%{release}
Requires:	apache-modules = %{version}-%{release}

%description	mod_file_cache
Caching frequently requested files that change very infrequently is a technique
for reducing server load. mod_file_cache provides two techniques for caching
frequently requested static files.

Through configuration directives, you can direct mod_file_cache to either open
then mmap()a file, or to pre-open a file and save the file's open file handle.
Both techniques reduce server load when processing requests for these files by
doing part of the work (specifically, the file I/O) for serving the file when
the server is started rather than during each request.

Notice: You cannot use this for speeding up CGI programs or other files which
are served by special content handlers. It can only be used for regular files
which are usually served by the Apache core content handler.

This module is an extension of and borrows heavily from the mod_mmap_static
module in Apache 1.3.

%package	mod_deflate
Summary:	Compress content before it is delivered to the client
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre):	apache-conf >= %{version}
Requires(pre):	apache-base = %{version}-%{release}
Requires(pre):	apache-modules = %{version}-%{release}
Requires:	apache-conf >= %{version}
Requires:	apache-base = %{version}-%{release}
Requires:	apache-modules = %{version}-%{release}
Obsoletes:	mod_gzip

%description	mod_deflate
The mod_deflate module provides the DEFLATE output filter that allows output
from your server to be compressed before being sent to the client over the
network.

%package	mod_proxy
Summary:	HTTP/1.1 proxy/gateway server
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre):	apache-conf >= %{version}
Requires(pre):	apache-base = %{version}-%{release}
Requires(pre):	apache-modules = %{version}-%{release}
Requires(pre):	apache-mod_cache = %{version}-%{release}
Requires(pre):	apache-mod_disk_cache = %{version}-%{release}
Requires:	apache-conf >= %{version}
Requires:	apache-base = %{version}-%{release}
Requires:	apache-modules = %{version}-%{release}
Requires:	apache-mod_cache = %{version}-%{release}
Requires:	apache-mod_disk_cache = %{version}-%{release}
Provides:	apache-mod_proxy_balancer = %{version}
Provides:	apache-mod_proxy_connect = %{version}
Provides:	apache-mod_proxy_ftp = %{version}
Provides:	apache-mod_proxy_http = %{version}

%description	mod_proxy
This module implements a proxy/gateway for Apache. It implements proxying
capability for FTP, CONNECT (for SSL), HTTP/0.9, HTTP/1.0, and HTTP/1.1. The
module can be configured to connect to other proxy modules for these and other
protocols.

This module was experimental in Apache 1.1.x. Improvements and bugfixes were
made in Apache v1.2.x and Apache v1.3.x, then the module underwent a major
overhaul for Apache v2.0. The protocol support was upgraded to HTTP/1.1, and
filter support was enabled.

Please note that the caching function present in mod_proxy up to Apache v2.0.39
has been removed from mod_proxy and is incorporated into a new module,
mod_cache.

%package	mod_proxy_ajp
Summary:	Provides support for the Apache JServ Protocol version 1.3 (AJP13)
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre):	apache-conf >= %{version}
Requires(pre):	apache-base = %{version}-%{release}
Requires(pre):	apache-modules = %{version}-%{release}
Requires(pre):	apache-mod_cache = %{version}-%{release}
Requires(pre):	apache-mod_proxy = %{version}-%{release}
Requires:	apache-conf >= %{version}
Requires:	apache-base = %{version}-%{release}
Requires:	apache-modules = %{version}-%{release}
Requires:	apache-mod_proxy = %{version}-%{release}

%description	mod_proxy_ajp
This module requires the service of mod_proxy. It provides support for the
Apache JServ Protocol version 1.3 (hereafter AJP13). Thus, in order to get the
ability of handling AJP13 protocol, mod_proxy and mod_proxy_ajp have to be
present in the server.

%package	mod_userdir
Summary:	User-specific directories
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre):	apache-conf >= %{version}
Requires(pre):	apache-base = %{version}-%{release}
Requires(pre):	apache-modules = %{version}-%{release}
Requires:	apache-conf >= %{version}
Requires:	apache-base = %{version}-%{release}
Requires:	apache-modules = %{version}-%{release}

%description	mod_userdir
This module allows user-specific directories to be accessed using the
http://example.com/~username/ syntax.

%package	mod_ssl
Summary:	Strong cryptography using the SSL, TLS and distcache protocols
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre):	apache-conf >= %{version}
Requires(pre):	apache-base = %{version}-%{release}
Requires(pre):	apache-modules = %{version}-%{release}
Requires:	apache-conf >= %{version}
Requires:	apache-base = %{version}-%{release}
Requires:	apache-modules = %{version}-%{release}
Requires:	openssl
Provides:	mod_ssl
Obsoletes:	mod_ssl

%description	mod_ssl
This module provides SSL v2/v3 and TLS v1 support for the Apache HTTP Server.
It was contributed by Ralf S. Engeschall based on his mod_ssl project and
originally derived from work by Ben Laurie.

This module relies on OpenSSL to provide the cryptography engine.

%package	mod_dbd
Summary:	Manages SQL database connections
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre):	apache-conf >= %{version}
Requires(pre):	apache-base = %{version}-%{release}
Requires(pre):	apache-modules = %{version}-%{release}
Requires(pre):	apr-util-dbd-sqlite3
Requires(pre):	apr-util-dbd-pgsql
Requires(pre):	apr-util-dbd-mysql
Requires:	apache-conf >= %{version}
Requires:	apache-base = %{version}-%{release}
Requires:	apache-modules = %{version}-%{release}
Requires:	apr-util-dbd-sqlite3
Requires:	apr-util-dbd-pgsql
Requires:	apr-util-dbd-mysql

%description	mod_dbd
mod_dbd manages SQL database connections using apr_dbd. It provides database
connections on request to modules requiring SQL database functions, and takes
care of managing databases with optimal efficiency and scalability for both
threaded and non-threaded MPMs.

%package	mod_authn_dbd
Summary:	User authentication using an SQL database
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre):	apache-conf >= %{version}
Requires(pre):	apache-base = %{version}-%{release}
Requires(pre):	apache-modules = %{version}-%{release}
Requires(pre):	apache-mod_dbd = %{version}-%{release}
Requires:	apache-conf >= %{version}
Requires:	apache-base = %{version}-%{release}
Requires:	apache-modules = %{version}-%{release}
Requires:	apache-mod_dbd = %{version}-%{release}

%description	mod_authn_dbd
This module provides authentication front-ends such as mod_auth_digest and
mod_auth_basic to authenticate users by looking up users in SQL tables. Similar
functionality is provided by, for example, mod_authn_file. This module relies
on mod_dbd to specify the backend database driver and connection parameters,
and manage the database connections.

%package	htcacheclean
Summary:	Clean up the disk cache (for apache-mod_disk_cache)
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper

%description	htcacheclean
htcacheclean is used to keep the size of mod_disk_cache's storage within a
certain limit. This tool can run either manually or in daemon mode. When
running in daemon mode, it sleeps in the background and checks the cache
directories at regular intervals for cached content to be removed.

%package	devel
Summary:	Module development tools for the apache web server
Group:		Development/C
Requires:	apr-devel >= 1:1.2.2
Requires:	apr-util-devel >= 1.2.2
Requires:	apr_memcache-devel >= 0.7.0
Requires:	byacc
Requires:	db4-devel
Requires:	distcache-devel
Requires:	expat-devel
Requires:	gdbm-devel
Requires:	libsasl-devel
Requires:	libtool >= 1.4.2
Requires:	openldap-devel
Requires:	openssl-devel
Requires:	pcre-devel >= 5.0
Requires:	perl >= 0:5.600
Requires:	pkgconfig
Requires:	zlib-devel
Requires:	autoconf2.5
Requires:	automake1.7

%description	devel
The apache-devel package contains the source code for the apache Web server and
the APXS binary you'll need to build Dynamic Shared Objects (DSOs) for apache.

If you are installing the apache Web server and you want to be able to compile
or develop additional modules for apache, you'll need to install this package.

%package	source
Summary:	The apache source code, including Mandriva patches
Group:		System/Servers

%description	source
The apache source code, including Mandriva patches. Use this package to build
your own customized apache if needed.

%prep
%setup -q -n httpd-%{version} -a4
%patch0 -p1 -b .deplibs.droplet
%patch1 -p1 -b .encode.droplet
%patch2 -p0 -b .xfsz.droplet
%patch3 -p1 -b .corelimit.droplet
%patch4 -p1 -b .debuglog.droplet
%patch5 -p1 -b .bsd-ipv6.droplet
%patch6 -p1 -b .apachesrc.droplet
%patch7 -p0 -b .apache2-suexec.droplet
%patch8 -p1 -b .apxs.droplet
%patch9 -p1 -b .disablemods.droplet
%patch10 -p1 -b .pod.droplet
%patch11 -p0 -b .memcache.droplet
%patch12 -p1 -b .french_fixes.droplet
%patch13 -p1 -b .authnoprov.droplet
%patch14 -p0 -b .fcgi.droplet
%patch15 -p0 -b .ab_source_address.droplet
%patch16 -p0 -b .fix_extra_htaccess_check.droplet

%patch50 -p0 -b .CVE-2007-1862.droplet

%patch100 -p1 -b .mpm-itk.droplet

# forcibly prevent use of bundled apr, apr-util, pcre
rm -rf srclib/{apr,apr-util,pcre}

# don't install or use bundled pcreposix.h
rm -f include/pcreposix.h

#Fix apxs
perl -pi -e 's|\@exp_installbuilddir\@|%{_libdir}/apache/build|;' support/apxs.in
perl -pi -e 's|get_vars\("prefix"\)|"%{_libdir}/apache/build"|;' support/apxs.in
perl -pi -e 's|get_vars\("sbindir"\) . "/envvars"|"\$installbuilddir/envvars"|;' support/apxs.in

#Correct perl paths
find -type f|xargs perl -pi -e "s|/usr/local/bin/perl|perl|g;\
        s|/usr/local/bin/perl5|perl|g;s|/path/to/bin/perl|perl|g;"

# this is really better and easier than a stupid static patch...
# for some reason you have to use ">>" here (!)

cat >> config.layout << EOF
<Layout NUX>
    prefix:        %{_sysconfdir}/httpd
    exec_prefix:   %{_prefix}
    bindir:        %{_bindir}
    sbindir:       %{_sbindir}
    libdir:        %{_libdir}
    libexecdir:    %{_libdir}/apache
    mandir:        %{_mandir}
    infodir:       %{_infodir}
    includedir:    %{_includedir}/apache
    sysconfdir:    %{_sysconfdir}/httpd/conf
    datadir:       /var/www
    installbuilddir: %{_libdir}/apache/build
    errordir:      /var/www/error
    iconsdir:      /var/www/icons
    htdocsdir:     /var/www/html
    manualdir:     
    cgidir:        /var/www/cgi-bin
    localstatedir: /var
    runtimedir:    /var/run
    logfiledir:    /var/log/httpd
    proxycachedir: /var/cache/httpd/mod_proxy
</Layout>     
EOF

#Fix DYNAMIC_MODULE_LIMIT
perl -pi -e "s/DYNAMIC_MODULE_LIMIT 64/DYNAMIC_MODULE_LIMIT 128/;" include/httpd.h

# don't try to touch srclib
perl -pi -e "s|^SUBDIRS = .*|SUBDIRS = os server modules support|g" Makefile.in

# bump server limit
perl -pi -e "s|DEFAULT_SERVER_LIMIT 256|DEFAULT_SERVER_LIMIT 1024|g" server/mpm/prefork/prefork.c

# tag it with the "legacy" name so that we can track this at netcraft...
perl -pi -e "s|^#define AP_SERVER_BASEPRODUCT .*|#define AP_SERVER_BASEPRODUCT \"%{BASEPRODUCT}\"|g" include/ap_release.h

# prepare the apache-source package
rm -rf $RPM_BUILD_DIR/tmp-httpd-%{version}; mkdir -p $RPM_BUILD_DIR/tmp-httpd-%{version}/usr/src
cp -dpR $RPM_BUILD_DIR/httpd-%{version} $RPM_BUILD_DIR/tmp-httpd-%{version}/usr/src/apache-%{version}
rm -rf $RPM_BUILD_DIR/tmp-httpd-%{version}/usr/src/apache-%{version}/perl-framework
rm -rf $RPM_BUILD_DIR/tmp-httpd-%{version}/usr/src/apache-%{version}/tmp-httpd-%{version}/usr/src
rm -f $RPM_BUILD_DIR/tmp-httpd-%{version}%{_usrsrc}/apache-%{version}/*.spec

# use my nice converted transparent png icons
tar -jxf %{SOURCE3}
mv icons/*.png docs/icons/

# add the changes file
cp %{SOURCE2} README.urpmi

# add the htcacheclean stuff
cp %{SOURCE9} htcacheclean.init
cp %{SOURCE10} htcacheclean.sysconfig

# add the module config files
cp %{SOURCE30} 30_mod_proxy.conf
cp %{SOURCE31} 31_mod_proxy_ajp.conf
cp %{SOURCE40} 40_mod_ssl.conf
cp %{SOURCE41} 41_mod_ssl.default-vhost.conf
cp %{SOURCE45} 45_mod_dav.conf
cp %{SOURCE46} 46_mod_ldap.conf
cp %{SOURCE47} 47_mod_authnz_ldap.conf
cp %{SOURCE55} 55_mod_cache.conf
cp %{SOURCE56} 56_mod_disk_cache.conf
cp %{SOURCE57} 57_mod_mem_cache.conf
cp %{SOURCE58} 58_mod_file_cache.conf
cp %{SOURCE59} 59_mod_deflate.conf
cp %{SOURCE60} 60_mod_dbd.conf
cp %{SOURCE61} 61_mod_authn_dbd.conf
cp %{SOURCE67} 67_mod_userdir.conf

# this will only work if configured correctly in the config (FullOs)...
cp server/core.c server/core.c.untagged

%build
%serverbuild

#########################################################################################
# configure and build phase
#
export WANT_AUTOCONF_2_5="1"

# use a minimal buildconf instead
cp %{SOURCE100} buildconf
sh ./buildconf

CFLAGS="$RPM_OPT_FLAGS"
CPPFLAGS="-DSSL_EXPERIMENTAL_ENGINE -DLDAP_DEPRECATED -DHAVE_APR_MEMCACHE"
if pkg-config openssl; then
    # configure -C barfs with trailing spaces in CFLAGS
    CFLAGS="$RPM_OPT_FLAGS $CPPFLAGS"
    CPPFLAGS="$CPPFLAGS `pkg-config --cflags openssl | sed 's/ *$//'`"
    AP_LIBS="$AP_LIBS `pkg-config --libs openssl`"
else
    CFLAGS="$RPM_OPT_FLAGS"
    CPPFLAGS="$CPPFLAGS"
    AP_LIBS="$AP_LIBS -lssl -lcrypto"
fi
export CFLAGS CPPFLAGS AP_LIBS

%if %mdkversion >= 200710
export CFLAGS="$CFLAGS -fstack-protector"
export CXXFLAGS="$CXXFLAGS -fstack-protector"
export FFLAGS="$FFLAGS -fstack-protector"
%endif

APVARS="--enable-layout=NUX \
    --cache-file=../config.cache \
    --prefix=%{_sysconfdir}/httpd \
    --exec-prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --sbindir=%{_sbindir} \
    --libexecdir=%{_libdir}/apache \
    --sysconfdir=%{_sysconfdir}/httpd/conf \
    --localstatedir=/var \
    --includedir=%{_includedir}/apache \
    --infodir=%{_infodir} \
    --mandir=%{_mandir} \
    --datadir=/var/www \
    --with-port=80 \
    --with-perl=%{_bindir}/perl \
    --with-apr=%{_bindir}/apr-1-config \
    --with-apr-util=%{_bindir}/apu-1-config \
    --with-pcre=%{_prefix} \
    --with-z=%{_prefix} \
    --enable-layout=NUX \
    --with-devrandom \
    --enable-exception-hook \
    --enable-forward \
    --with-program-name=httpd"

for mpm in worker event itk prefork; do
    mkdir build-${mpm}; pushd build-${mpm}
    ln -s ../configure .
    
    if [ ${mpm} = prefork ]; then
        %configure2_5x $APVARS \
    	    --with-mpm=prefork \
    	    --enable-modules=all \
	    --enable-mods-shared=all \
    	    --with-ldap --enable-ldap=shared --enable-authnz-ldap=shared \
	    --enable-cache=shared --enable-disk-cache=shared --enable-file-cache=shared --enable-mem-cache=shared \
    	    --enable-ssl --with-ssl=%{_prefix} --enable-distcache \
    	    --enable-deflate=shared \
    	    --enable-cgid=shared \
    	    --enable-proxy=shared --enable-proxy-connect=shared --enable-proxy-ftp=shared \
    	    --enable-proxy-http=shared --enable-proxy-ajp=shared --enable-proxy-balancer=shared \
    	    --enable-dav=shared --enable-dav-fs=shared --enable-dav-lock=shared \
    	    --enable-version=shared \
    	    --enable-bucketeer=shared --enable-case-filter=shared --enable-case-filter-in=shared --enable-echo=shared \
    	    --enable-example=shared --enable-optional-fn-export=shared --enable-optional-fn-import=shared \
    	    --enable-optional-hook-export=shared --enable-optional-hook-import=shared \
	    --enable-charset_lite=shared --enable-authn_alias=shared
    fi
    
    if [ ${mpm} = worker ]; then
	%configure2_5x $APVARS \
    	    --with-mpm=worker \
	    --enable-modules=none
    # don't build support tools
    perl -pi -e "s|^SUBDIRS = .*|SUBDIRS = os server modules|g" Makefile
    fi

    if [ ${mpm} = event ]; then
	%configure2_5x $APVARS \
    	    --with-mpm=event \
	    --enable-modules=none
    # don't build support tools
    perl -pi -e "s|^SUBDIRS = .*|SUBDIRS = os server modules|g" Makefile
    fi

    if [ ${mpm} = itk ]; then
	%configure2_5x $APVARS \
    	    --with-mpm=itk \
	    --enable-modules=none
    # don't build support tools
    perl -pi -e "s|^SUBDIRS = .*|SUBDIRS = os server modules|g" Makefile
    fi

    #Copy configure flags to a file in the apache-source rpm.
    cp config.nice $RPM_BUILD_DIR/tmp-httpd-%{version}%{_usrsrc}/apache-%{version}/config.nice.${mpm}

    # tag it with the mpm name too so that we can track this somehow at for example netcraft...
    MPM_NAME=`echo ${mpm}|tr "[a-z]" "[A-Z]"`
    cp ../server/core.c.untagged ../server/core.c
    perl -pi -e "s|\" PLATFORM \"|%{TAG}/${MPM_NAME}-%{release}|g" ../server/core.c

    # if libexpat0-devel is installed on x86_64 somehow the EXTRA_LDLAGS is set 
    # to -L/usr/lib, fix that with a conditional hack...
    %ifarch x86_64
	find -type f | xargs perl -pi -e "s|/usr/lib\b|%{_libdir}|g"
    %endif

    # there is no autofoo stuff the memcache addon yet
    perl -pi -e "s|-ldistcache -lnal|%{_libdir}/libapr_memcache.la -ldistcache -lnal|g" build/config_vars.mk
    cp %{_includedir}/apr_memcache-0/apr_memcache.h modules/ssl/

    # finally doing the build stage
    %make
    popd
done

%if %{build_test}
# run the test suite, quite a hack, but works, sometimes...
TEST_DIR="`pwd`/TEST"
make -C build-prefork DESTDIR=${TEST_DIR} \
	manualdir=${TEST_DIR}/var/www/html/manual \
	install

perl -pi -e "s|%{_libdir}/apache/|${TEST_DIR}%{_libdir}/apache/|g" ${TEST_DIR}%{_sysconfdir}/httpd/conf/*
perl -pi -e "s|^#Include|Include|g" ${TEST_DIR}%{_sysconfdir}/httpd/conf/httpd.conf
perl -pi -e "s|/etc|${TEST_DIR}/etc|g" ${TEST_DIR}%{_sysconfdir}/httpd/conf/httpd.conf ${TEST_DIR}%{_sysconfdir}/httpd/conf/extra/*.conf
perl -pi -e  "s|%{_libdir}/apache/build|${TEST_DIR}%{_libdir}/apache/build|g" ${TEST_DIR}%{_sbindir}/apxs

# fool apxs
cat >> ${TEST_DIR}%{_libdir}/apache/build/config_vars.mk << EOF
bindir = ${TEST_DIR}/usr/bin
sbindir = ${TEST_DIR}/usr/sbin
exec_prefix = ${TEST_DIR}/usr
datadir = ${TEST_DIR}/var/www
localstatedir = ${TEST_DIR}/var
libdir = ${TEST_DIR}%{_libdir}
libexecdir = ${TEST_DIR}%{_libdir}/apache
includedir = ${TEST_DIR}/usr/include/apache
sysconfdir = ${TEST_DIR}/etc/httpd/conf
installbuilddir = ${TEST_DIR}%{_libdir}/apache/build
runtimedir = ${TEST_DIR}/var/run
proxycachedir = ${TEST_DIR}/var/cache/httpd/mod_proxy
prefix = ${TEST_DIR}/usr
EOF

pushd perl-framework
#svn checkout --ignore-externals http://svn.apache.org/repos/asf/httpd/test/trunk/perl-framework perl-framework
#svn checkout http://svn.apache.org/repos/asf/httpd/test/trunk/perl-framework perl-framework
#svn up

# disable test cases for bugs that has not been fixed yet,are too old, or
# it is unclear who to blaim, either the php or ASF folks...
rm -f t/php/arg.t
rm -f t/php/func5.t

# this test works with php-5.0 but not with php-5.1, yuck!
rm -f t/php/virtual.t

# if not using LC_ALL=C t/php/getlastmod.t can fail at
# testing : getlastmod()
# expected: november
# received: November
export LC_ALL=C

perl Makefile.PL -apxs ${TEST_DIR}%{_sbindir}/apxs \
    -httpd_conf ${TEST_DIR}%{_sysconfdir}/httpd/conf/httpd.conf \
    -httpd ${TEST_DIR}%{_sbindir}/httpd
make test
popd
%endif

# prevent some insane linkage
pushd build-prefork/support
    for i in htcacheclean logresolve rotatelogs; do
	rm -f ${i} ${i}.o
	%make AP_LIBS="`apr-1-config --apr-la-file`" $i
    done
popd    

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 
#########################################################################################
# install phase
install -d %{buildroot}%{_libdir}/apache
install -d %{buildroot}%{_libdir}/apache-extramodules
install -d %{buildroot}%{_sysconfdir}/httpd/modules.d
install -d %{buildroot}%{_localstatedir}/dav
install -d %{buildroot}/var/www
install -d %{buildroot}/var/cache/httpd/mod_proxy

#EXCLUDE_FROM_STRIP="%{buildroot}%{_sbindir}/httpd %{buildroot}%{_sbindir}/httpd-worker %{buildroot}%{_sbindir}/httpd-peruser"

# install source
tar c -C $RPM_BUILD_DIR/tmp-httpd-%{version} usr/src | tar x -C %{buildroot}

# don't fiddle with the initscript!
export DONT_GPRINTIFY=1

pushd build-prefork
make install \
	prefix=%{buildroot}%{_prefix} \
	bindir=%{buildroot}%{_bindir} \
	sbindir=%{buildroot}%{_sbindir} \
	libdir=%{buildroot}%{_libdir} \
	libexecdir=%{buildroot}%{_libdir}/apache \
	mandir=%{buildroot}%{_mandir} \
	sysconfdir=%{buildroot}%{_sysconfdir}/httpd/conf \
	includedir=%{buildroot}%{_includedir}/apache \
	localstatedir=%{buildroot}/var \
	runtimedir=%{buildroot}/var/run \
	installbuilddir=%{buildroot}%{_libdir}/apache/build  \
	datadir=%{buildroot}/var/www \
	errordir=%{buildroot}/var/www/error \
	iconsdir=%{buildroot}/var/www/icons \
	htdocsdir=%{buildroot}/var/www/html \
	manualdir=%{buildroot}/var/www/html/manual \
	cgidir=%{buildroot}/var/www/cgi-bin \
	runtimedir=%{buildroot}/var/run \
	logdir=%{buildroot}/var/log/httpd \
	logfiledir=%{buildroot}/var/log/httpd \
	proxycachedir=%{buildroot}/var/cache/httpd/mod_proxy
popd

# do some house cleaning 
for f in `find %{buildroot} -type f -name ".orig"` \
    `find %{buildroot} -type f -name ".deps"` \
    `find %{buildroot} -type f -name "NW*"` \
    `find %{buildroot} -type f -name "*.droplet"` \
    `find %{buildroot} -type f -name "*.zip"` \
    `find %{buildroot} -type f -name "*.dsp"`; do
    rm -f $f
done

# this is needed to generate the vanilla config
make -C build-prefork DESTDIR=`pwd` install-conf

#Fix config_vars.mk, and add some MDK flags so all other modules 
#can simply do "apxs -q VARIABLE" and know, for example, the exact
#release of apache-devel or the exact directory where the source is
#located. 
CVMK="%{buildroot}%{_libdir}/apache/build/config_vars.mk"
perl -pi -e "s|%{_builddir}/httpd-%{version}|%{_usrsrc}/apache-%{version}|g" $CVMK
perl -pi -e "s|%{buildroot}||g" $CVMK
perl -pi -e "s|^EXTRA_INCLUDES.*|EXTRA_INCLUDES = `apr-1-config --includes` -I%{_includedir}/apache -I%{_includedir}/openssl|g" $CVMK

# fix libtool invocation
perl -pi -e "s|^LIBTOOL.*|LIBTOOL = libtool|g" $CVMK
perl -pi -e "s|^SH_LIBTOOL.*|SH_LIBTOOL = libtool|g" $CVMK

# if the following 3 lines needs to be enabled again, use the ".*" wildcard as in
# "s|bla bla =.*|bla bla = replaced whatever text after the equal char...|g"
#perl -pi -e "s|installbuilddir =.*|installbuilddir = %{_libdir}/apache/build|g" $CVMK
#perl -pi -e "s|htdocsdir =.*|htdocsdir = /var/www/html|g" $CVMK
#perl -pi -e "s|logfiledir =.*|logfiledir = /var/log/httpd|g" $CVMK

echo "ap_version = %{version}" >> $CVMK
echo "ap_release = %{release}" >> $CVMK

#########################################################################################
# fix some bugs and other stuff
#
perl -pi -e "s|%{_builddir}/httpd-%{version}|%{_usrsrc}/apache-%{version}|g" %{buildroot}%{_libdir}/apache/build/apr_rules.mk

mv %{buildroot}%{_sbindir}/envvars %{buildroot}%{_libdir}/apache/build/

# named config.nice files are in the devel package
rm -f %{buildroot}%{_libdir}/apache/build/config.nice

##################################################################

# Link build dir
ln -s ../../..%{_libdir}/apache/build %{buildroot}%{_sysconfdir}/httpd/build

##################################################################
# install module conf files for the "modules.d" dir loading structure
install -m0644 30_mod_proxy.conf %{buildroot}%{_sysconfdir}/httpd/modules.d/
install -m0644 31_mod_proxy_ajp.conf %{buildroot}%{_sysconfdir}/httpd/modules.d/
install -m0644 40_mod_ssl.conf %{buildroot}%{_sysconfdir}/httpd/modules.d/
install -m0644 41_mod_ssl.default-vhost.conf %{buildroot}%{_sysconfdir}/httpd/modules.d/
install -m0644 45_mod_dav.conf %{buildroot}%{_sysconfdir}/httpd/modules.d/
install -m0644 46_mod_ldap.conf %{buildroot}%{_sysconfdir}/httpd/modules.d/
install -m0644 47_mod_authnz_ldap.conf %{buildroot}%{_sysconfdir}/httpd/modules.d/
install -m0644 55_mod_cache.conf %{buildroot}%{_sysconfdir}/httpd/modules.d/
install -m0644 56_mod_disk_cache.conf %{buildroot}%{_sysconfdir}/httpd/modules.d/
install -m0644 57_mod_mem_cache.conf %{buildroot}%{_sysconfdir}/httpd/modules.d/
install -m0644 58_mod_file_cache.conf %{buildroot}%{_sysconfdir}/httpd/modules.d/
install -m0644 59_mod_deflate.conf %{buildroot}%{_sysconfdir}/httpd/modules.d/
install -m0644 60_mod_dbd.conf %{buildroot}%{_sysconfdir}/httpd/modules.d/
install -m0644 61_mod_authn_dbd.conf %{buildroot}%{_sysconfdir}/httpd/modules.d/
install -m0644 67_mod_userdir.conf %{buildroot}%{_sysconfdir}/httpd/modules.d/

# install the mpm stuff
install -m0755 build-worker/httpd %{buildroot}%{_sbindir}/httpd-worker
install -m0755 build-event/httpd %{buildroot}%{_sbindir}/httpd-event
install -m0755 build-itk/httpd %{buildroot}%{_sbindir}/httpd-itk

# install missing files
install -m755 build-prefork/support/split-logfile %{buildroot}%{_sbindir}/split-logfile
install -m755 support/list_hooks.pl %{buildroot}%{_sbindir}/list_hooks.pl
install -m755 build-prefork/support/logresolve.pl %{buildroot}%{_sbindir}/logresolve.pl
install -m755 build-prefork/support/log_server_status %{buildroot}%{_sbindir}/log_server_status
install -m755 build-prefork/support/checkgid %{buildroot}%{_sbindir}/checkgid
install -m755 support/check_forensic %{buildroot}%{_sbindir}/check_forensic

# fix a msec safe cache for the ssl stuff
install -d %{buildroot}/var/cache/httpd/mod_ssl
touch %{buildroot}/var/cache/httpd/mod_ssl/scache.dir
touch %{buildroot}/var/cache/httpd/mod_ssl/scache.pag
touch %{buildroot}/var/cache/httpd/mod_ssl/scache.sem

# fix a msec safe cache for the mod_ldap LDAPSharedCacheFile
touch %{buildroot}/var/cache/httpd/mod_ldap_cache

# install htcacheclean files
install -d %{buildroot}%{_initrddir}
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -m0755 htcacheclean.init %{buildroot}%{_initrddir}/htcacheclean
install -m0644 htcacheclean.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/htcacheclean

%if %mdkversion >= 1020
%multiarch_includes %{buildroot}%{_includedir}/apache/ap_config_layout.h
%endif

# add two important documentation files in the plain ASCII format
cp docs/manual/upgrading.html.en upgrading.html
cp docs/manual/new_features_2_2.html.en new_features_2_2.html

lynx -dump -nolist upgrading.html > upgrading.txt
lynx -dump -nolist new_features_2_2.html > new_features_2_2.txt

# cleanup
rm -f %{buildroot}%{_sbindir}/suexec
rm -f  %{buildroot}%{_mandir}/man8/suexec.8*
rm -rf %{buildroot}/var/www/html/index*
rm -rf %{buildroot}/var/www/html/apach*
rm -rf %{buildroot}/var/www/cgi-bin/printenv
rm -rf %{buildroot}/var/www/cgi-bin/test-cgi
rm -rf %{buildroot}/var/www/html/manual
rm -rf %{buildroot}%{_sysconfdir}/httpd/conf/{extra,original,httpd.conf,magic,mime.types}

#########################################################################################
# install phase done
#

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 

# Clean up "install source" and other generated dirs
[ "$RPM_BUILD_DIR/tmp-httpd-%{version}%{_usrsrc}/apache-%{version}" != "/" ] && rm -rf $RPM_BUILD_DIR/tmp-httpd-%{version}%{_usrsrc}/apache-%{version}
[ "$RPM_BUILD_DIR/usr/src" != "/" ] && rm -rf $RPM_BUILD_DIR/usr/src
[ "$RPM_BUILD_DIR/tmp-httpd-%{version}" != "/" ] && rm -rf $RPM_BUILD_DIR/tmp-httpd-%{version}

%pre base
%_pre_useradd apache /var/www /bin/sh

%postun base
%_postun_userdel apache

%post mpm-prefork
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi

%postun mpm-prefork
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart 1>&2
    fi
fi

%post mpm-worker
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi

%postun mpm-worker
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart 1>&2
    fi
fi

%post mpm-event
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi

%postun mpm-event
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart 1>&2
    fi
fi

%post mpm-itk
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi

%postun mpm-itk
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart 1>&2
    fi
fi

%post modules
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi

%post mod_proxy
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi

%postun mod_proxy
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart 1>&2
    fi
fi

%post mod_proxy_ajp
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi

%postun mod_proxy_ajp
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart 1>&2
    fi
fi

%post mod_dav
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi

%postun mod_dav
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart 1>&2
    fi
fi

%post mod_ldap
%create_ghostfile /var/cache/httpd/mod_ldap_cache apache root 0600
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi

%postun mod_ldap
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart 1>&2
    fi
fi

%post mod_cache
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi

%postun mod_cache
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart 1>&2
    fi
fi

%post mod_disk_cache
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi

%postun mod_disk_cache
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart 1>&2
    fi
fi

%post mod_mem_cache
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi

%postun mod_mem_cache
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart 1>&2
    fi
fi

%post mod_file_cache
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi

%postun mod_file_cache
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart 1>&2
    fi
fi

%post mod_deflate
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi

%postun mod_deflate
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart 1>&2
    fi
fi

%post mod_userdir
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi

%postun mod_userdir
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart 1>&2
    fi
fi

%post mod_ssl
if [ "$1" = "1" ]; then 

mkdir -p %{_sysconfdir}/pki/tls/{private,certs} 2>/dev/null
umask 077

if [ ! -f %{_sysconfdir}/pki/tls/private/localhost.key ]; then
    %{_bindir}/openssl genrsa -rand /proc/apm:/proc/cpuinfo:/proc/dma:/proc/filesystems:/proc/interrupts:/proc/ioports:/proc/pci:/proc/rtc:/proc/uptime 1024 > %{_sysconfdir}/pki/tls/private/localhost.key 2> /dev/null
fi

FQDN=`hostname`
if [ "x${FQDN}" = "x" ]; then
    FQDN=localhost.localdomain
fi

if [ ! -f %{_sysconfdir}/pki/tls/certs/localhost.crt ] ; then
cat << EOF | %{_bindir}/openssl req -new -key %{_sysconfdir}/pki/tls/private/localhost.key -x509 -days 365 -set_serial $RANDOM -out %{_sysconfdir}/pki/tls/certs/localhost.crt 2>/dev/null
--
SomeState
SomeCity
SomeOrganization
SomeOrganizationalUnit
${FQDN}
root@${FQDN}
EOF
fi
fi

if [ "$1" -gt "1" ]; then
    mkdir -p %{_sysconfdir}/pki/tls/{private,certs} 2>/dev/null
    if [ -d /etc/ssl/apache ];then
	if [ -f /etc/ssl/apache/server.crt.rpmsave -a ! -f /etc/pki/tls/certs/localhost.crt ]; then
	    cp -p /etc/ssl/apache/server.crt.rpmsave /etc/pki/tls/certs/localhost.crt
	fi
	if [ -f /etc/ssl/apache/server.key.rpmsave -a ! -f /etc/pki/tls/private/localhost.key ]; then
	    cp -p /etc/ssl/apache/server.key.rpmsave /etc/pki/tls/private/localhost.key
	fi

    fi
fi

# create some ghost files
%create_ghostfile /var/cache/httpd/mod_ssl/scache.dir apache root 0600
%create_ghostfile /var/cache/httpd/mod_ssl/scache.pag apache root 0600
%create_ghostfile /var/cache/httpd/mod_ssl/scache.sem apache root 0600

if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi

%postun mod_ssl
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart 1>&2
    fi
fi

%post mod_dbd
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi

%postun mod_dbd
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart 1>&2
    fi
fi

%post mod_authn_dbd
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi

%postun mod_authn_dbd
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart 1>&2
    fi
fi

%post htcacheclean
%_post_service htcacheclean
if [ -f %{_var}/lock/subsys/htcacheclean ]; then
    %{_initrddir}/htcacheclean restart 1>&2;
fi

%preun htcacheclean
%_preun_service htcacheclean

%postun htcacheclean
if [ "$1" = "0" ]; then
    if [ -f %{_var}/lock/subsys/htcacheclean ]; then
        %{_initrddir}/htcacheclean restart 1>&2
    fi
fi

%files mpm-prefork
%defattr(-,root,root)
%doc etc/httpd/conf/httpd.conf etc/httpd/conf/extra/*.conf
%attr(0755,root,root) %{_sbindir}/httpd

%files mpm-worker
%defattr(-,root,root)
%doc etc/httpd/conf/httpd.conf etc/httpd/conf/extra/*.conf
%attr(0755,root,root) %{_sbindir}/httpd-worker

%files mpm-event
%defattr(-,root,root)
%doc etc/httpd/conf/httpd.conf etc/httpd/conf/extra/*.conf
%attr(0755,root,root) %{_sbindir}/httpd-event

%files mpm-itk
%defattr(-,root,root)
%doc etc/httpd/conf/httpd.conf etc/httpd/conf/extra/*.conf README.itk
%attr(0755,root,root) %{_sbindir}/httpd-itk

%files modules
%defattr(-,root,root)
%doc modules/README*
%attr(0755,root,root) %{_libdir}/apache/mod_actions.so
%attr(0755,root,root) %{_libdir}/apache/mod_alias.so
%attr(0755,root,root) %{_libdir}/apache/mod_asis.so
%attr(0755,root,root) %{_libdir}/apache/mod_auth_basic.so
%attr(0755,root,root) %{_libdir}/apache/mod_auth_digest.so
%attr(0755,root,root) %{_libdir}/apache/mod_authn_alias.so
%attr(0755,root,root) %{_libdir}/apache/mod_authn_anon.so
%attr(0755,root,root) %{_libdir}/apache/mod_authn_dbm.so
%attr(0755,root,root) %{_libdir}/apache/mod_authn_default.so
%attr(0755,root,root) %{_libdir}/apache/mod_authn_file.so
%attr(0755,root,root) %{_libdir}/apache/mod_authz_dbm.so
%attr(0755,root,root) %{_libdir}/apache/mod_authz_default.so
%attr(0755,root,root) %{_libdir}/apache/mod_authz_groupfile.so
%attr(0755,root,root) %{_libdir}/apache/mod_authz_host.so
%attr(0755,root,root) %{_libdir}/apache/mod_authz_owner.so
%attr(0755,root,root) %{_libdir}/apache/mod_authz_user.so
%attr(0755,root,root) %{_libdir}/apache/mod_autoindex.so
%attr(0755,root,root) %{_libdir}/apache/mod_bucketeer.so
%attr(0755,root,root) %{_libdir}/apache/mod_case_filter.so
%attr(0755,root,root) %{_libdir}/apache/mod_case_filter_in.so
%attr(0755,root,root) %{_libdir}/apache/mod_cern_meta.so
%attr(0755,root,root) %{_libdir}/apache/mod_cgi.so
%attr(0755,root,root) %{_libdir}/apache/mod_cgid.so
%attr(0755,root,root) %{_libdir}/apache/mod_charset_lite.so
%attr(0755,root,root) %{_libdir}/apache/mod_dir.so
%attr(0755,root,root) %{_libdir}/apache/mod_dumpio.so
%attr(0755,root,root) %{_libdir}/apache/mod_echo.so
%attr(0755,root,root) %{_libdir}/apache/mod_env.so
%attr(0755,root,root) %{_libdir}/apache/mod_example.so
%attr(0755,root,root) %{_libdir}/apache/mod_expires.so
%attr(0755,root,root) %{_libdir}/apache/mod_ext_filter.so
%attr(0755,root,root) %{_libdir}/apache/mod_filter.so
%attr(0755,root,root) %{_libdir}/apache/mod_headers.so
%attr(0755,root,root) %{_libdir}/apache/mod_ident.so
%attr(0755,root,root) %{_libdir}/apache/mod_imagemap.so
%attr(0755,root,root) %{_libdir}/apache/mod_include.so
%attr(0755,root,root) %{_libdir}/apache/mod_info.so
%attr(0755,root,root) %{_libdir}/apache/mod_log_config.so
%attr(0755,root,root) %{_libdir}/apache/mod_log_forensic.so
%attr(0755,root,root) %{_libdir}/apache/mod_logio.so
%attr(0755,root,root) %{_libdir}/apache/mod_mime_magic.so
%attr(0755,root,root) %{_libdir}/apache/mod_mime.so
%attr(0755,root,root) %{_libdir}/apache/mod_negotiation.so
%attr(0755,root,root) %{_libdir}/apache/mod_optional_fn_export.so
%attr(0755,root,root) %{_libdir}/apache/mod_optional_fn_import.so
%attr(0755,root,root) %{_libdir}/apache/mod_optional_hook_export.so
%attr(0755,root,root) %{_libdir}/apache/mod_optional_hook_import.so
%attr(0755,root,root) %{_libdir}/apache/mod_rewrite.so
%attr(0755,root,root) %{_libdir}/apache/mod_setenvif.so
%attr(0755,root,root) %{_libdir}/apache/mod_speling.so
%attr(0755,root,root) %{_libdir}/apache/mod_status.so
%attr(0755,root,root) %{_libdir}/apache/mod_unique_id.so
%attr(0755,root,root) %{_libdir}/apache/mod_usertrack.so
%attr(0755,root,root) %{_libdir}/apache/mod_version.so
%attr(0755,root,root) %{_libdir}/apache/mod_vhost_alias.so
%attr(0755,root,root) %{_libdir}/apache/httpd.exp

%files mod_proxy
%defattr(-,root,root)
%doc modules/proxy/CHANGES
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/*_mod_proxy.conf
%attr(0755,root,root) %{_libdir}/apache/mod_proxy_connect.so
%attr(0755,root,root) %{_libdir}/apache/mod_proxy_ftp.so
%attr(0755,root,root) %{_libdir}/apache/mod_proxy_http.so
%attr(0755,root,root) %{_libdir}/apache/mod_proxy.so
%attr(0755,root,root) %{_libdir}/apache/mod_proxy_balancer.so
%attr(0770,root,apache) %dir /var/cache/httpd/mod_proxy

%files mod_proxy_ajp
%defattr(-,root,root)
%doc modules/proxy/CHANGES
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/*_mod_proxy_ajp.conf
%attr(0755,root,root) %{_libdir}/apache/mod_proxy_ajp.so

%files mod_dav
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/*_mod_dav.conf
%attr(0755,root,root) %{_libdir}/apache/mod_dav_fs.so
%attr(0755,root,root) %{_libdir}/apache/mod_dav_lock.so
%attr(0755,root,root) %{_libdir}/apache/mod_dav.so
%attr(-,apache,apache) %dir %{_localstatedir}/dav
 
%files mod_ldap
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/*_mod_ldap.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/*_mod_authnz_ldap.conf
%attr(0755,root,root) %{_libdir}/apache/mod_ldap.so
%attr(0755,root,root) %{_libdir}/apache/mod_authnz_ldap.so
%attr(0600,apache,root) %ghost /var/cache/httpd/mod_ldap_cache

%files mod_cache
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/*_mod_cache.conf
%attr(0755,root,root) %{_libdir}/apache/mod_cache.so

%files mod_disk_cache
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/*_mod_disk_cache.conf
%attr(0755,root,root) %{_libdir}/apache/mod_disk_cache.so

%files mod_mem_cache
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/*_mod_mem_cache.conf
%attr(0755,root,root) %{_libdir}/apache/mod_mem_cache.so

%files mod_file_cache
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/*_mod_file_cache.conf
%attr(0755,root,root) %{_libdir}/apache/mod_file_cache.so

%files mod_deflate
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/*_mod_deflate.conf
%attr(0755,root,root) %{_libdir}/apache/mod_deflate.so

%files mod_userdir
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/*_mod_userdir.conf
%attr(0755,root,root) %{_libdir}/apache/mod_userdir.so

%files mod_ssl
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/*_mod_ssl.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/*_mod_ssl.default-vhost.conf
%attr(0755,root,root) %{_libdir}/apache/mod_ssl.so
%attr(0700,apache,root) %dir /var/cache/httpd/mod_ssl
%attr(0600,apache,root) %ghost /var/cache/httpd/mod_ssl/scache.dir
%attr(0600,apache,root) %ghost /var/cache/httpd/mod_ssl/scache.pag
%attr(0600,apache,root) %ghost /var/cache/httpd/mod_ssl/scache.sem

%files mod_dbd
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/*_mod_dbd.conf
%attr(0755,root,root) %{_libdir}/apache/mod_dbd.so

%files mod_authn_dbd
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/*_mod_authn_dbd.conf
%attr(0755,root,root) %{_libdir}/apache/mod_authn_dbd.so

%files base
%defattr(-,root,root)
%doc README.urpmi upgrading.txt new_features_2_2.txt
%dir /var/www/error
%dir /var/www/error/include
%config(noreplace,missingok) /var/www/error/README
%config(noreplace,missingok) /var/www/error/*.var
%config(noreplace,missingok) /var/www/error/include/*.html
%dir /var/www/icons
%dir /var/www/icons/small
%attr(0644,root,root) /var/www/icons/README*
%attr(0644,root,root) /var/www/icons/*.png
%attr(0644,root,root) /var/www/icons/*.gif
%attr(0644,root,root) /var/www/icons/small/README*
%attr(0644,root,root) /var/www/icons/small/*.png
%attr(0644,root,root) /var/www/icons/small/*.gif
%attr(0755,root,root) %{_sbindir}/ab
%attr(0755,root,root) %{_sbindir}/apachectl
%attr(0755,root,root) %{_sbindir}/check_forensic
%attr(0755,root,root) %{_sbindir}/checkgid
%attr(0755,root,root) %{_sbindir}/dbmmanage
%attr(0755,root,root) %{_sbindir}/htdbm
%attr(0755,root,root) %{_sbindir}/htdigest
%attr(0755,root,root) %{_sbindir}/htpasswd
%attr(0755,root,root) %{_sbindir}/httxt2dbm
%attr(0755,root,root) %{_sbindir}/list_hooks.pl
%attr(0755,root,root) %{_sbindir}/logresolve
%attr(0755,root,root) %{_sbindir}/logresolve.pl
%attr(0755,root,root) %{_sbindir}/log_server_status
%attr(0755,root,root) %{_sbindir}/rotatelogs
%attr(0755,root,root) %{_sbindir}/split-logfile
%attr(0755,root,root) %dir %{_libdir}/apache
%attr(0755,root,root) %dir %{_libdir}/apache-extramodules
%attr(0700,apache,root) %dir /var/cache/httpd
%exclude %{_mandir}/man8/htcacheclean.8*
%{_mandir}/*/*

%files htcacheclean
%defattr(-,root,root)
%attr(0755,root,root) %{_initrddir}/htcacheclean
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/htcacheclean
%attr(0755,root,root) %{_sbindir}/htcacheclean
%{_mandir}/man8/htcacheclean.8*

%files devel
%defattr(-,root,root)
%if %mdkversion >= 1020
%multiarch %{multiarch_includedir}/apache/ap_config_layout.h
%endif
%{_includedir}/apache
%attr(0755,root,root) %dir %{_libdir}/apache/build
%attr(0755,root,root) %dir %{_sysconfdir}/httpd/build
%attr(0644,root,root) %{_libdir}/apache/build/*.mk
%attr(0755,root,root) %{_libdir}/apache/build/*.sh
%attr(0755,root,root) %{_libdir}/apache/build/envvars
%attr(0755,root,root) %{_sbindir}/envvars-std
%attr(0755,root,root) %{_sbindir}/apxs

%files source
%defattr(-,root,root)
%{_usrsrc}/apache-%{version}
