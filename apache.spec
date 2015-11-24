%define _build_pkgcheck_set %{nil}
%define _build_pkgcheck_srpm %{nil}

%define defaultmaxmodules 256
%define defaultserverlimit 2048

%define TAG OpenMandriva Lx
%define BASEPRODUCT Apache
%define all_services httpd.service httpd-worker.service httpd-event.service

Summary:	The most widely used Web server on the Internet
Name:		apache
Version:	2.4.17
Release:	0.1
Group:		System/Servers
License:	Apache License
URL:		http://www.apache.org
Source0:	http://archive.apache.org/dist/httpd/httpd-%{version}.tar.gz
Source1:	http://archive.apache.org/dist/httpd/httpd-%{version}.tar.gz.asc
Source2:	webapp.script
Source3:	apache2_transparent_png_icons.tar.bz2
Source9: 	htcacheclean.service
Source10: 	htcacheclean.sysconfig
Source11:	OpenMandriva.tar.xz
Source15:	httpd.service
Source100:	buildconf
Patch0:		httpd-2.0.45-deplibs.patch
Patch8:		httpd-2.1.10-apxs.patch
# speedups by Allen Pulsifer
Patch16:	httpd-2.2.4-fix_extra_htaccess_check.diff
Patch18:	httpd-2.2.10-ldap_auth_now_modular_in-apr-util-dbd-ldap_fix.diff
Patch19:	httpd-2.2.21-linux3.diff
Patch105:	httpd-2.2.17-filter.patch
Patch106:	httpd-2.4.1-mdv_config.diff
Patch107:	httpd-2.4.1-linkage_fix.diff
Patch108:	httpd-2.4.1-buildfix.diff
BuildRequires:	autoconf automake libtool
BuildRequires:	pkgconfig(apr-1) >= 1.5.0
BuildRequires:	pkgconfig(apr-util-1) >= 1.5.3
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(libnghttp2)
BuildRequires:	sasl-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(lua) >= 5.1
BuildRequires:	lynx
BuildRequires:	openldap-devel
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	perl
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(zlib)
# So people who "urpmi httpd" get what they expect
Provides:	httpd = %EVRD

%description
This package contains the main binary of apache, a powerful, full-featured,
efficient and freely-available Web server. Apache is also the most popular Web
server on the Internet.

This version of apache is fully modular, and many modules are available in
pre-compiled formats, like PHP and mod_auth_external.

This package defaults to a maximum of %{defaultmaxmodules} dynamically loadable modules.
This package defaults to a ServerLimit of %{defaultserverlimit}.

You can change these values at RPM build time by using for example:

--define 'maxmodules 512' --define 'serverlimit 2048' 

The package was built to support a maximum of %{?!maxmodules:%{defaultmaxmodules}}%{?maxmodules:%{maxmodules}} dynamically loadable modules.
The package was built with a ServerLimit of %{?!serverlimit:%{defaultserverlimit}}%{?serverlimit:%{serverlimit}}.

%package	mpm-prefork
Summary:	Implements a non-threaded, pre-forking web server (stable)
Group:		System/Servers
Requires(preun): systemd-units
Requires(postun): systemd-units
Requires(post): systemd-units
Requires:	apache-base = %{version}-%{release}
Requires:	apache-modules = %{version}-%{release}
Provides:	webserver
Provides:	apache = %{version}-%{release}
Provides:	apache-mpm = %{version}-%{release}

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

This package defaults to a maximum of %{defaultmaxmodules} dynamically loadable modules.
This package defaults to a ServerLimit of %{defaultserverlimit}.

You can change these values at RPM build time by using for example:

--define 'maxmodules 512' --define 'serverlimit 2048' 

The package was built to support a maximum of %{?!maxmodules:%{defaultmaxmodules}}%{?maxmodules:%{maxmodules}} dynamically loadable modules.
The package was built with a ServerLimit of %{?!serverlimit:%{defaultserverlimit}}%{?serverlimit:%{serverlimit}}.

%package	mpm-worker
Summary:	Implements a hybrid multi-threaded multi-process web server (experimental)
Group:		System/Servers
Requires(preun): systemd-units
Requires(postun): systemd-units
Requires(post): systemd-units
Requires:	apache-base = %{version}-%{release}
Requires:	apache-modules = %{version}-%{release}
Provides:	webserver
Provides:	apache = %{version}-%{release}
Conflicts:	apache-mod_php apache-mod_perl apache-mod_python

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

This package defaults to a maximum of %{defaultmaxmodules} dynamically loadable modules.

You can change these values at RPM build time by using for example:

--define 'maxmodules 512'

The package was built to support a maximum of %{?!maxmodules:%{defaultmaxmodules}}%{?maxmodules:%{maxmodules}} dynamically loadable modules.

%package	mpm-event
Summary:	Implements a hybrid multi-threaded multi-process web server
Group:		System/Servers
Requires(preun): systemd-units
Requires(postun): systemd-units
Requires(post): systemd-units
Requires:	apache-base = %{version}-%{release}
Requires:	apache-modules = %{version}-%{release}
Provides:	webserver
Provides:	apache = %{version}-%{release}
Conflicts:	apache-mod_php apache-mod_perl apache-mod_python

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

This package defaults to a maximum of %{defaultmaxmodules} dynamically loadable modules.

You can change these values at RPM build time by using for example:

--define 'maxmodules 512'

The package was built to support a maximum of %{?!maxmodules:%{defaultmaxmodules}}%{?maxmodules:%{maxmodules}} dynamically loadable modules.

%package	base
Summary:	Common files and utilities for apache
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires:	apache = %{version}-%{release}
Provides:	apache-conf = %{version}-%{release}
Obsoletes:	apache-conf

%description	base
This package contains the apache utilities such as Apache Bench (ab) for stress
testing your apache installation and several tools for managing user databases,
access control, the apache logs and more.

%package	modules
Summary:	Meta package
Group:		System/Servers
Requires:	apache-mpm = %{version}-%{release}
Requires:	apache-mod_actions = %{version}-%{release}
Requires:	apache-mod_alias = %{version}-%{release}
Requires:	apache-mod_auth_basic = %{version}-%{release}
Requires:	apache-mod_auth_digest = %{version}-%{release}
Requires:	apache-mod_authn_anon = %{version}-%{release}
Requires:	apache-mod_authn_file = %{version}-%{release}
Requires:	apache-mod_authz_dbm = %{version}-%{release}
Requires:	apache-mod_authz_groupfile = %{version}-%{release}
Requires:	apache-mod_authz_host = %{version}-%{release}
Requires:	apache-mod_authz_owner = %{version}-%{release}
Requires:	apache-mod_authz_user = %{version}-%{release}
Requires:	apache-mod_autoindex = %{version}-%{release}
Requires:	apache-mod_cgi = %{version}-%{release}
Requires:	apache-mod_dir = %{version}-%{release}
Requires:	apache-mod_env = %{version}-%{release}
Requires:	apache-mod_expires = %{version}-%{release}
Requires:	apache-mod_filter = %{version}-%{release}
Requires:	apache-mod_headers = %{version}-%{release}
Requires:	apache-mod_http2 = %{version}-%{release}
Requires:	apache-mod_imagemap = %{version}-%{release}
Requires:	apache-mod_include = %{version}-%{release}
Requires:	apache-mod_info = %{version}-%{release}
Requires:	apache-mod_log_config = %{version}-%{release}
Requires:	apache-mod_mime = %{version}-%{release}
Requires:	apache-mod_mime_magic = %{version}-%{release}
Requires:	apache-mod_negotiation = %{version}-%{release}
Requires:	apache-mod_rewrite = %{version}-%{release}
Requires:	apache-mod_setenvif = %{version}-%{release}
Requires:	apache-mod_status = %{version}-%{release}
Requires:	apache-mod_substitute = %{version}-%{release}
Requires:	apache-mod_unique_id = %{version}-%{release}
Requires:	apache-mod_usertrack = %{version}-%{release}
Requires:	apache-mod_version = %{version}-%{release}
Requires:	apache-mod_vhost_alias = %{version}-%{release}
# new 2.3+ modules
Requires:	apache-mod_authz_core = %{version}-%{release}
Requires:	apache-mod_authz_host = %{version}-%{release}
Requires:	apache-mod_unixd = %{version}-%{release}
# obsolete 2.2 modules
Obsoletes:	apache-mod_authz_default
Obsoletes:	apache-mod_authn_alias
Obsoletes:	apache-mod_authn_default

%description	modules
This is a meta package that pulls in the apache modules used as default in the
apache-2.2 series in OpenMandriva.

%package	mod_authn_file
Summary:	User authentication using text files
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_authn_file
This module provides authentication front-ends such as mod_auth_digest
and mod_auth_basic to authenticate users by looking up users in plain text
password files. Similar functionality is provided by mod_authn_dbm.

When using mod_auth_basic or mod_auth_digest, this module is invoked via
the AuthBasicProvider or AuthDigestProvider with the file value.

%package	mod_authn_dbm
Summary:	User authentication using DBM files
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_authn_dbm
This module provides authentication front-ends such as mod_auth_digest and
mod_auth_basic to authenticate users by looking up users in dbm password
files. Similar functionality is provided by mod_authn_file.

When using mod_auth_basic or mod_auth_digest, this module is invoked via
the AuthBasicProvider or AuthDigestProvider with the dbm value.

%package	mod_authn_anon
Summary:	Allows "anonymous" user access to authenticated areas
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_authn_anon
This module provides authentication front-ends such as mod_auth_basic to
authenticate users similar to anonymous-ftp sites, i.e. have a 'magic' user
id 'anonymous' and the email address as a password. These email addresses
can be logged.

Combined with other (database) access control methods, this allows for
effective user tracking and customization according to a user profile
while still keeping the site open for 'unregistered' users. One advantage
of using Auth-based user tracking is that, unlike magic-cookies and funny
URL pre/postfixes, it is completely browser independent and it allows users
to share URLs.

When using mod_auth_basic, this module is invoked via the AuthBasicProvider
directive with the anon value.

%package	mod_authn_dbd
Summary:	User authentication using an SQL database
Group:		System/Servers
Requires:	apache-mod_dbd

%description	mod_authn_dbd
This module provides authentication front-ends such as mod_auth_digest
and mod_auth_basic to authenticate users by looking up users in SQL
tables. Similar functionality is provided by, for example, mod_authn_file.

This module relies on mod_dbd to specify the backend database driver and
connection parameters, and manage the database connections.

When using mod_auth_basic or mod_auth_digest, this module is invoked via
the AuthBasicProvider or AuthDigestProvider with the dbd value.

%package	mod_authn_socache
Summary:	Manages a cache of authentication credentials to relieve the load on backends
Group:		System/Servers

%description	mod_authn_socache
Maintains a cache of authentication credentials, so that a new backend
lookup is not required for every authenticated request.

%package	mod_authn_core
Summary:	Core Authentication
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_authn_core
This module provides core authentication capabilities to allow or deny
access to portions of the web site. mod_authn_core provides directives that
are common to all authentication providers.

%package	mod_authz_host
Summary:	Group authorizations based on host (name or IP address)
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_authz_host
The authorization providers implemented by mod_authz_host are registered using
the Require directive. The directive can be referenced within a <Directory>,
<Files>, or <Location> section as well as .htaccess files to control access
to particular parts of the server.  Access can be controlled based on the
client hostname or IP address.

In general, access restriction directives apply to all access methods (GET,
PUT, POST, etc). This is the desired behavior in most cases.  However, it is
possible to restrict some methods, while leaving other methods unrestricted,
by enclosing the directives in a <Limit> section.

%package	mod_authz_groupfile
Summary:	Group authorization using plaintext files
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_authz_groupfile
This module provides authorization capabilities so that authenticated
users can be allowed or denied access to portions of the web site by group
membership. Similar functionality is provided by mod_authz_dbm.

%package	mod_authz_user
Summary:	User Authorization
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_authz_user
This module provides authorization capabilities so that authenticated
users can be allowed or denied access to portions of the web site.
mod_authz_user grants access if the authenticated user is listed in a
Require user directive. Alternatively Require valid-user can be used to
grant access to all successfully authenticated users.

%package	mod_authz_dbm
Summary:	Group authorization using DBM files
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_authz_dbm
This module provides authorization capabilities so that authenticated
users can be allowed or denied access to portions of the web site by group
membership. Similar functionality is provided by mod_authz_groupfile.

%package	mod_authz_owner
Summary:	Authorization based on file ownership
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_authz_owner
This module authorizes access to files by comparing the userid used for
HTTP authentication (the web userid) with the file-system owner or group
of the requested file. The supplied username and password must be already
properly verified by an authentication module, such as mod_auth_basic or
mod_auth_digest. mod_authz_owner recognizes two arguments for the Require
directive, file-owner and file-group, as follows:

file-owner
 The supplied web-username must match the system's name for the owner of the
 file being requested. That is, if the operating system says the requested
 file is owned by jones, then the username used to access it through the
 web must be jones as well.

file-group
 The name of the system group that owns the file must be present in a
 group database, which is provided, for example, by mod_authz_groupfile
 or mod_authz_dbm, and the web-username must be a member of that group. For
 example, if the operating system says the requested file is owned by (system)
 group accounts, the group accounts must appear in the group database and
 the web-username used in the request must be a member of that group.

%package	mod_authz_dbd
Summary:	Group Authorization and Login using SQL
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_authz_dbd
This module provides authorization capabilities so that authenticated
users can be allowed or denied access to portions of the web site by group
membership. Similar functionality is provided by mod_authz_groupfile and
mod_authz_dbm, with the exception that this module queries a SQL database
to determine whether a user is a member of a group.

This module can also provide database-backed user login/logout
capabilities. These are likely to be of most value when used in conjunction
with mod_authn_dbd.

This module relies on mod_dbd to specify the backend database driver and
connection parameters, and manage the database connections.

%package	mod_authz_core
Summary:	Core Authorization
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_authz_core
This module provides core authorization capabilities so that
authenticated users can be allowed or denied access to portions of the
web site. mod_authz_core provides the functionality to register various
authorization providers. It is usually used in conjunction with an
authentication provider module such as mod_authn_file and an authorization
module such as mod_authz_user. It also allows for advanced logic to be
applied to the authorization processing.

%package	mod_authnz_ldap
Summary:	LDAP HTTP Basic authentication
Group:		System/Servers
Conflicts:	apache-mod_proxy < 2.4.0

%description	mod_authnz_ldap
This module provides authentication front-ends such as mod_auth_basic to
authenticate users through an ldap directory.

mod_authnz_ldap supports the following features:

* Known to support the OpenLDAP SDK (both 1.x and 2.x), Novell LDAP SDK and
  the iPlanet (Netscape) SDK.

* Complex authorization policies can be implemented by representing the policy
  with LDAP filters.

* Uses extensive caching of LDAP operations via mod_ldap.

* Support for LDAP over SSL (requires the Netscape SDK) or TLS (requires the
  OpenLDAP 2.x SDK or Novell LDAP SDK).

When using mod_auth_basic, this module is invoked via the AuthBasicProvider
directive with the ldap value.

%package	mod_access_compat
Summary:	Group authorizations based on host (name or IP address)
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_access_compat
The directives provided by mod_access_compat are used in <Directory>,
<Files>, and <Location> sections as well as .htaccess files to control access
to particular parts of the server. Access can be controlled based on the
client hostname, IP address, or other characteristics of the client request,
as captured in environment variables. The Allow and Deny directives are
used to specify which clients are or are not allowed access to the server,
while the Order directive sets the default access state, and configures
how the Allow and Deny directives interact with each other.

Both host-based access restrictions and password-based authentication may
be implemented simultaneously. In that case, the Satisfy directive is used
to determine how the two sets of restrictions interact.

%package	mod_auth_basic
Summary:	Basic authentication
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_auth_basic
This module allows the use of HTTP Basic Authentication to restrict access
by looking up users in the given providers. HTTP Digest Authentication is
provided by mod_auth_digest. This module should usually be combined with at
least one authentication module such as mod_authn_file and one authorization
module such as mod_authz_user.

%package	mod_auth_form
Summary:	Form authentication
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_auth_form
Form authentication depends on the mod_session modules, and these modules
make use of HTTP cookies, and as such can fall victim to Cross Site Scripting
attacks, or expose potentially private information to clients. Please ensure
that the relevant risks have been taken into account before enabling the
session functionality on your server.

This module allows the use of an HTML login form to restrict access by
looking up users in the given providers. HTML forms require significantly
more configuration than the alternatives, however an HTML login form can
provide a much friendlier experience for end users.

HTTP basic authentication is provided by mod_auth_basic, and HTTP digest
authentication is provided by mod_auth_digest. This module should be
combined with at least one authentication module such as mod_authn_file
and one authorization module such as mod_authz_user.

Once the user has been successfully authenticated, the user's login details
will be stored in a session provided by mod_session.

%package	mod_auth_digest
Summary:	User authentication using MD5 Digest Authentication
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_auth_digest
This module implements HTTP Digest Authentication (RFC2617), and provides
a more secure alternative to mod_auth_basic.

%package	mod_allowmethods
Summary:	Easily restrict what HTTP methods can be used on the server
Group:		System/Servers

%description	mod_allowmethods
This module makes it easy to restrict what HTTP methods can used on an
server. The most common configuration would be:

%package	mod_file_cache
Summary:	Caches a static list of files in memory
Group:		System/Servers

%description	mod_file_cache
This module should be used with care. You can easily create a broken site
using mod_file_cache, so read this document carefully.

Caching frequently requested files that change very infrequently is a
technique for reducing server load. mod_file_cache provides two techniques for
caching frequently requested static files. Through configuration directives,
you can direct mod_file_cache to either open then mmap() a file, or to
pre-open a file and save the file's open file handle. Both techniques reduce
server load when processing requests for these files by doing part of the
work (specifically, the file I/O) for serving the file when the server is
started rather than during each request.

Notice: You cannot use this for speeding up CGI programs or other files
which are served by special content handlers. It can only be used for
regular files which are usually served by the Apache core content handler.

This module is an extension of and borrows heavily from the mod_mmap_static
module in Apache 1.3.

%package	mod_cache
Summary:	RFC 2616 compliant HTTP caching filter
Group:		System/Servers
Suggests:	apache-mod_cache_disk

%description	mod_cache
This module should be used with care, as when the CacheQuickHandler
directive is in its default value of on, the Allow and Deny directives
will be circumvented. You should not enable quick handler caching for any
content to which you wish to limit access by client host name, address or
environment variable.

mod_cache implements an RFC 2616 compliant HTTP content caching filter,
with support for the caching of content negotiated responses containing
the Vary header.

RFC 2616 compliant caching provides a mechanism to verify whether stale or
expired content is still fresh, and can represent a significant performance
boost when the origin server supports conditional requests by honouring
the If-None-Match HTTP request header. Content is only regenerated from
scratch when the content has changed, and not when the cached entry expires.

As a filter, mod_cache can be placed in front of content originating from
any handler, including flat files (served from a slow disk cached on a fast
disk), the output of a CGI script or dynamic content generator, or content
proxied from another server.

In the default configuration, mod_cache inserts the caching filter as far
forward as possible within the filter stack, utilising the quick handler to
bypass all per request processing when returning content to the client. In
this mode of operation, mod_cache may be thought of as a caching proxy
server bolted to the front of the webserver, while running within the
webserver itself.

When the quick handler is switched off using the CacheQuickHandler directive,
it becomes possible to insert the CACHE filter at a point in the filter
stack chosen by the administrator. This provides the opportunity to cache
content before that content is personalised by the mod_include filter,
or optionally compressed by the mod_deflate filter.

Under normal operation, mod_cache will respond to and can be controlled by
the Cache-Control and Pragma headers sent from a client in a request, or from
a server within a response. Under exceptional circumstances, mod_cache can
be configured to override these headers and force site specific behaviour,
however such behaviour will be limited to this cache only, and will not
affect the operation of other caches that may exist between the client and
server, and as a result is not recommended unless strictly necessary.

RFC 2616 allows for the cache to return stale data while the existing
stale entry is refreshed from the origin server, and this is supported
by mod_cache when the CacheLock directive is suitably configured. Such
responses will contain a Warning HTTP header with a 110 response code.
RFC 2616 also allows a cache to return stale data when the attempt made to
refresh the stale data returns an error 500 or above, and this behaviour
is supported by default by mod_cache. Such responses will contain a Warning
HTTP header with a 111 response code.

mod_cache requires the services of one or more storage management modules. One
storage management module is included in the base Apache distribution:

mod_cache_disk
 Implements a disk based storage manager. Headers and bodies are stored
 separately on disk, in a directory structure derived from the md5 hash of the
 cached URL. Multiple content negotiated responses can be stored concurrently,
 however the caching of partial content is not supported by this module. The
 htcacheclean tool is provided to list cached URLs, remove cached URLs,
 or to maintain the size of the disk cache within size and inode limits.

Further details, discussion, and examples, are provided in the Caching Guide.

%package	mod_cache_disk
Summary:	Disk based storage module for the HTTP caching filter
Group:		System/Servers
Obsoletes:	apache-mod_disk_cache
Suggests:	apache-htcacheclean = %{version}-%{release}

%description	mod_cache_disk
mod_cache_disk implements a disk based storage manager for mod_cache.

The headers and bodies of cached responses are stored separately on disk,
in a directory structure derived from the md5 hash of the cached URL.

Multiple content negotiated responses can be stored concurrently, however
the caching of partial content is not yet supported by this module.

Atomic cache updates to both header and body files are achieved without
the need for locking by storing the device and inode numbers of the body
file within the header file. This has the side effect that cache entries
manually moved into the cache will be ignored.

The htcacheclean tool is provided to list cached URLs, remove cached URLs,
or to maintain the size of the disk cache within size and/or inode limits. The
tool can be run on demand, or can be daemonized to offer continuous monitoring
of directory sizes.

%package	mod_cache_socache
Summary:	Shared Object cache module for HTTPD
Group:		System/Servers

%description	mod_cache_socache
mod_cache_socache implements a shared object cache (socache) based storage
manager for mod_cache.

The headers and bodies of cached responses are combined, and stored underneath
a single key in the shared object cache. A number of implementations of shared
object caches are available to choose from.

Multiple content negotiated responses can be stored concurrently, however the
caching of partial content is not yet supported by this module.

%package	mod_socache_shmcb
Summary:	shmcb based shared object cache provider
Group:		System/Servers

%description	mod_socache_shmcb
mod_socache_shmcb is a shared object cache provider which provides for
creation and access to a cache backed by a high-performance cyclic buffer
inside a shared memory segment.

shmcb:/path/to/datafile(512000)

Details of other shared object cache providers can be found here.

%package	mod_socache_dbm
Summary:	DBM based shared object cache provider
Group:		System/Servers

%description	mod_socache_dbm
mod_socache_dbm is a shared object cache provider which provides for creation
and access to a cache backed by a DBM database.

dbm:/path/to/datafile

Details of other shared object cache providers can be found here.

%package	mod_socache_memcache
Summary:	Memcache based shared object cache provider
Group:		System/Servers

%description	mod_socache_memcache
mod_socache_memcache is a shared object cache provider which provides for
creation and access to a cache backed by the memcached high-performance,
distributed memory object caching system.

Details of other shared object cache providers can be found here.

%package	mod_watchdog
Summary:	provides infrastructure for other modules to periodically run tasks
Group:		System/Servers

%description	mod_watchdog
mod_watchdog defines programmatic hooks for other modules to periodically run
tasks. These modules can register handlers for mod_watchdog hooks. Currently,
the following modules in the Apache distribution use this functionality:

 * mod_heartbeat

 * mod_heartmonitor

To allow a module to use mod_watchdog functionality, mod_watchdog itself
must be statically linked to the server core or, if a dynamic module,
be loaded before the calling module.

%package	mod_dbd
Summary:	Manages SQL database connections
Group:		System/Servers
Requires:	apr-util-dbd-ldap
Suggests:	apr-util-dbd-freetds
Suggests:	apr-util-dbd-mysql
Suggests:	apr-util-dbd-odbc
Suggests:	apr-util-dbd-pgsql
Suggests:	apr-util-dbd-sqlite3

%description	mod_dbd
mod_dbd manages SQL database connections using APR. It provides database
connections on request to modules requiring SQL database functions, and
takes care of managing databases with optimal efficiency and scalability
for both threaded and non-threaded MPMs. For details, see the APR website
and this overview of the Apache DBD Framework by its original developer.

%package	mod_bucketeer
Summary:	Buckets manipulation filter
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_bucketeer
Buckets manipulation filter

%package	mod_dumpio
Summary:	Dumps all I/O to error log as desired
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_dumpio
mod_dumpio allows for the logging of all input received by Apache and/or
all output sent by Apache to be logged (dumped) to the error.log file.

The data logging is done right after SSL decoding (for input) and right
before SSL encoding (for output). As can be expected, this can produce
extreme volumes of data, and should only be used when debugging problems.

%package	mod_echo
Summary:	A simple echo server to illustrate protocol modules
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_echo
This module provides an example protocol module to illustrate the concept. It
provides a simple echo server. Telnet to it and type stuff, and it will
echo it.

%package	mod_case_filter
Summary:	CaseFilter module
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_case_filter
CaseFilter module

%package	mod_case_filter_in
Summary:	CaseFilterInFilter module
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_case_filter_in
CaseFilterInFilter module

%package	mod_buffer
Summary:	Support for request buffering
Group:		System/Servers

%description	mod_buffer
This module provides the ability to buffer the input and output filter stacks.

Under certain circumstances, content generators might create content in small
chunks. In order to promote memory reuse, in memory chunks are always 8k in
size, regardless of the size of the chunk itself. When many small chunks are
generated by a request, this can create a large memory footprint while the
request is being processed, and an unnecessarily large amount of data on
the wire. The addition of a buffer collapses the response into the fewest
chunks possible.

When httpd is used in front of an expensive content generator, buffering the
response may allow the backend to complete processing and release resources
sooner, depending on how the backend is designed.

The buffer filter may be added to either the input or the output filter
stacks, as appropriate, using the SetInputFilter, SetOutputFilter,
AddOutputFilter or AddOutputFilterByType directives.

Using buffer with mod_include

AddOutputFilterByType INCLUDES;BUFFER text/html The buffer filters read the
request/response into RAM and then repack the request/response into the fewest
memory buckets possible, at the cost of CPU time. When the request/response
is already efficiently packed, buffering the request/response could cause
the request/response to be slower than not using a buffer at all. These
filters should be used with care, and only where necessary.

%package	mod_data
Summary:	Convert response body into an RFC2397 data URL
Group:		System/Servers

%description	mod_data
This module provides the ability to convert a response into an RFC2397
data URL.

Data URLs can be embedded inline within web pages using something like
the mod_include module, to remove the need for clients to make separate
connections to fetch what may potentially be many small images. Data URLs
may also be included into pages generated by scripting languages such as PHP.

An example of a data URL

data:image/gif;base64,R0lGODdhMAAwAPAAAAAAAP///ywAAAAAMAAw
AAAC8IyPqcvt3wCcDkiLc7C0qwyGHhSWpjQu5yqmCYsapyuvUUlvONmOZtfzgFz
ByTB10QgxOR0TqBQejhRNzOfkVJ+5YiUqrXF5Y5lKh/DeuNcP5yLWGsEbtLiOSp
a/TPg7JpJHxyendzWTBfX0cxOnKPjgBzi4diinWGdkF8kjdfnycQZXZeYGejmJl
ZeGl9i2icVqaNVailT6F5iJ90m6mvuTS4OK05M0vDk0Q4XUtwvKOzrcd3iq9uis
F81M1OIcR7lEewwcLp7tuNNkM3uNna3F2JQFo97Vriy/Xl4/f1cf5VWzXyym7PH
hhx4dbgYKAAA7

The filter takes no parameters, and can be added to the filter stack using
the SetOutputFilter directive, or any of the directives supported by the
mod_filter module.

Configuring the filter

<Location /data/images>
SetOutputFilter DATA </Location>

%package	mod_ratelimit
Summary:	Bandwidth Rate Limiting for Clients
Group:		System/Servers

%description	mod_ratelimit
Provides a filter named RATE_LIMIT to limit client bandwidth. The connection
speed to be simulated is specified, in KiB/s, using the environment variable
rate-limit.

%package	mod_reqtimeout
Summary:	Set timeout and minimum data rate for receiving requests
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_reqtimeout
This module allows to set timeouts for the reading request and reading body
phases. It is implemented as an input connection filter that sets the socket
timeout so that the total request time does not exceed the timeout value.

mod_reqtimeout can be used to mitigate slowloris type attacks.

%package	mod_ext_filter
Summary:	Pass the response body through an external program before delivery
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_ext_filter
mod_ext_filter presents a simple and familiar programming model for
filters. With this module, a program which reads from stdin and writes to
stdout (i.e., a Unix-style filter command) can be a filter for Apache. This
filtering mechanism is much slower than using a filter which is specially
written for the Apache API and runs inside of the Apache server process,
but it does have the following benefits: * the programming model is much
simpler * any programming/scripting language can be used, provided that it
 allows the program to read from standard input and write to standard output
* existing programs can be used unmodified as Apache filters

Even when the performance characteristics are not suitable for production
use, mod_ext_filter can be used as a prototype environment for filters.

%package	mod_request
Summary:	Filters to handle and make available HTTP request bodies
Group:		System/Servers

%description	mod_request
Under normal circumstances, request handlers such as the default handler
for static files will discard the request body when it is not needed by
the request handler. As a result, filters such as mod_include are limited
to making GET requests only when including other URLs as subrequests, even
if the original request was a POST request, as the discarded request body
is no longer available once filter processing is taking place.

When this directive has a value greater than zero, request handlers that
would otherwise discard request bodies will instead set the request body
aside for use by filters up to the maximum size specified. In the case of the
mod_include filter, an attempt to POST a request to the static shtml file will
cause any subrequests to be POST requests, instead of GET requests as before.

This feature makes it possible to break up complex web pages and web
applications into small individual components, and combine the components
and the surrounding web page structure together using mod_include. The
components can take the form of CGI programs, scripted languages, or URLs
reverse proxied into the URL space from another server using mod_proxy.

Note: Each request set aside has to be set aside in temporary RAM until the
request is complete. As a result, care should be taken to ensure sufficient
RAM is available on the server to support the intended load. Use of this
directive should be limited to where needed on targeted parts of your URL
space, and with the lowest possible value that is still big enough to hold
a request body.

If the request size sent by the client exceeds the maximum size allocated
by this directive, the server will return 413 Request Entity Too Large.

%package	mod_include
Summary:	Server-parsed html documents (Server Side Includes)
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_include
This module provides a filter which will process files before they are
sent to the client. The processing is controlled by specially formatted
SGML comments, referred to as elements. These elements allow conditional
text, the inclusion of other files or programs, as well as the setting and
printing of environment variables.

%package	mod_filter
Summary:	Context-sensitive smart filter configuration module
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_filter
This module enables smart, context-sensitive configuration of output
content filters. For example, apache can be configured to process different
content-types through different filters, even when the content-type is not
known in advance (e.g. in a proxy).

mod_filter works by introducing indirection into the filter chain.  Instead of
inserting filters in the chain, we insert a filter harness which in turn
dispatches conditionally to a filter provider. Any content filter may be
used as a provider to mod_filter; no change to existing filter modules is
required (although it may be possible to simplify them).

%package	mod_reflector
Summary:	Reflect a request body as a response via the output filter stack
Group:		System/Servers

%description	mod_reflector
This module allows request bodies to be reflected back to the client,
in the process passing the request through the output filter stack. A
suitably configured chain of filters can be used to transform the request
into a response. This module can be used to turn an output filter into an
HTTP service.

%package	mod_substitute
Summary:	Perform search and replace operations on response bodies
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_substitute
mod_substitute provides a mechanism to perform both regular expression and
fixed string substitutions on response bodies.

%package	mod_sed
Summary:	Filter Input (request) and Output (response) content using sed syntax
Group:		System/Servers

%description	mod_sed
mod_sed is an in-process content filter. The mod_sed filter implements the
sed editing commands implemented by the Solaris 10 sed program as described
in the manual page. However, unlike sed, mod_sed doesn't take data from
standard input. Instead, the filter acts on the entity data sent between
client and server. mod_sed can be used as an input or output filter. mod_sed
is a content filter, which means that it cannot be used to modify client
or server http headers.

The mod_sed output filter accepts a chunk of data, executes the sed scripts
on the data, and generates the output which is passed to the next filter
in the chain.

The mod_sed input filter reads the data from the next filter in the chain,
executes the sed scripts, and returns the generated data to the caller
filter in the filter chain.

Both the input and output filters only process the data if newline characters
are seen in the content. At the end of the data, the rest of the data is
treated as the last line.

A tutorial article on mod_sed, and why it is more powerful than simple string
or regular expression search and replace, is available on the author's blog.

%package	mod_charset_lite
Summary:	Specify character set translation or recoding
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_charset_lite
mod_charset_lite allows the server to change the character set of responses
before sending them to the client. In an EBCDIC environment, Apache always
translates HTTP protocol content (e.g. response headers) from the code page of
the Apache process locale to ISO-8859-1, but not the body of responses. In
any environment, mod_charset_lite can be used to specify that response
bodies should be translated. For example, if files are stored in EBCDIC,
then mod_charset_lite can translate them to ISO-8859-1 before sending them
to the client.

This module provides a small subset of configuration mechanisms implemented
by Russian Apache and its associated mod_charset.

%package	mod_deflate
Summary:	Compress content before it is delivered to the client
Group:		System/Servers

%description	mod_deflate
The mod_deflate module provides the DEFLATE output filter that allows
output from your server to be compressed before being sent to the client
over the network.

%package	mod_macro
Summary:	Macro support inside Apache httpd runtime configuration files
Group:		System/Servers

%description	mod_macro
This modules provides macros within apache httpd runtime configuration files.
These macros may have parameters. They are expanded when used (parameters
are substituted by their values given as an argument), and the result is
processed normally.

%package	mod_xml2enc
Summary:	Enhanced charset/internationalisation support for libxml2-based filter modules
Group:		System/Servers

%description	mod_xml2enc
This module provides enhanced internationalisation support for markup-aware
filter modules such as mod_proxy_html. It can automatically detect the
encoding of input data and ensure they are correctly processed by the
libxml2 parser, including converting to Unicode (UTF-8) where necessary. It
can also convert data to an encoding of choice after markup processing, and
will ensure the correct charset value is set in the HTTP Content-Type header.

%package	mod_proxy_html
Summary:	Rewrite HTML links in to ensure they are addressable in a proxy context
Group:		System/Servers

%description	mod_proxy_html
This module provides an output filter to rewrite HTML links in a proxy
situation, to ensure that links work for users outside the proxy. It serves
the same purpose as Apache's ProxyPassReverse directive does for HTTP headers,
and is an essential component of a reverse proxy.

For example, if a company has an application server at appserver.example.com
that is only visible from within the company's internal network, and a
public webserver www.example.com, they may wish to provide a gateway to
the application server at http://www.example.com/appserver/. When the
application server links to itself, those links need to be rewritten
to work through the gateway.  mod_proxy_html serves to rewrite <a
href="http://appserver.example.com/foo/bar.html">foobar</a> to <a
href="http://www.example.com/appserver/foo/bar.html">foobar</a> making it
accessible from outside.

mod_proxy_html was originally developed at WebÞing, whose extensive
documentation may be useful to users.

%package	mod_proxy_wstunnel
Summary:	WebSockets support for mod_proxy
Group:		System/Servers

%description	mod_proxy_wstunnel
This module requires the service of mod_proxy. It provides support
for the tunnelling of web socket connections to a backend websockets
server. The connection is automagically upgraded to a websocket
connection.

%package	mod_mime
Summary:	Associates the requested filename's extensions with the
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_mime
This module is used to assign content metadata to the content selected
for an HTTP response by mapping patterns in the URI or filenames to the
metadata values. For example, the filename extensions of content files
often define the content's Internet media type, language, character set,
and content-encoding. This information is sent in HTTP messages containing
that content and used in content negotiation when selecting alternatives,
such that the user's preferences are respected when choosing one of several
possible contents to serve. See mod_negotiation for more information about
content negotiation.

The directives AddCharset, AddEncoding, AddLanguage and AddType are all used
to map file extensions onto the metadata for that file.  Respectively they
set the character set, content-encoding, content-language, and media-type
(content-type) of documents. The directive TypesConfig is used to specify
a file which also maps extensions onto media types.

In addition, mod_mime may define the handler and filters that originate
and process content. The directives AddHandler, AddOutputFilter, and
AddInputFilter control the modules or scripts that serve the document.
The MultiviewsMatch directive allows mod_negotiation to consider these file
extensions to be included when testing Multiviews matches.

While mod_mime associates metadata with filename extensions, the core
server provides directives that are used to associate all the files in a
given container (e.g., <Location>, <Directory>, or <Files>) with particular
metadata. These directives include ForceType, SetHandler, SetInputFilter,
and SetOutputFilter. The core directives override any filename extension
mappings defined in mod_mime.

Note that changing the metadata for a file does not change the value of the
Last-Modified header. Thus, previously cached copies may still be used by
a client or proxy, with the previous headers. If you change the metadata
(language, content type, character set or encoding) you may need to 'touch'
affected files (updating their last modified date) to ensure that all
visitors are receive the corrected content headers.

%package	mod_ldap
Summary:	LDAP connection pooling and result caching services
Group:		System/Servers
Requires:	apr-util-dbd-ldap
Requires:	apache-mod_authnz_ldap

%description	mod_ldap
This module was created to improve the performance of websites relying on
backend connections to LDAP servers. In addition to the functions provided
by the standard LDAP libraries, this module adds an LDAP connection pool
and an LDAP shared memory cache.

To enable this module, LDAP support must be compiled into apr-util.
This is achieved by adding the --with-ldap flag to the configure script
when building Apache.

SSL/TLS support is dependant on which LDAP toolkit has been linked to
APR. As of this writing, APR-util supports: OpenLDAP SDK (2.x or later),
Novell LDAP SDK, Mozilla LDAP SDK, native Solaris LDAP SDK (Mozilla based),
native Microsoft LDAP SDK, or the iPlanet (Netscape) SDK. See the APR
website for details.

%package	mod_log_config
Summary:	Logging of the requests made to the server
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_log_config
This module provides for flexible logging of client requests. Logs are
written in a customizable format, and may be written directly to a file, or
to an external program. Conditional logging is provided so that individual
requests may be included or excluded from the logs based on characteristics
of the request.

Three directives are provided by this module: TransferLog to create a log
file, LogFormat to set a custom format, and CustomLog to define a log file
and format in one step. The TransferLog and CustomLog directives can be
used multiple times in each server to cause each request to be logged to
multiple files.

%package	mod_log_debug
Summary:	Additional configurable debug logging
Group:		System/Servers

%description	mod_log_debug
Additional configurable debug logging.

%package	mod_log_forensic
Summary:	Forensic Logging of the requests made to the server
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_log_forensic
This module provides for forensic logging of client requests. Logging is
done before and after processing a request, so the forensic log contains
two log lines for each request. The forensic logger is very strict, which
means: * The format is fixed. You cannot modify the logging format at
 runtime.
* If it cannot write its data, the child process exits immediately
 and may dump core (depending on your CoreDumpDirectory configuration).

The check_forensic script, which can be found in the distribution's support
directory, may be helpful in evaluating the forensic log output.

%package	mod_logio
Summary:	Logging of input and output bytes per request
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_logio
This module provides the logging of input and output number of bytes
received/sent per request. The numbers reflect the actual bytes as received
on the network, which then takes into account the headers and bodies of
requests and responses. The counting is done before SSL/TLS on input and
after SSL/TLS on output, so the numbers will correctly reflect any changes
made by encryption.

This module requires mod_log_config.  When KeepAlive connections are used with
SSL, the overhead of the SSL handshake is reflected in the byte count of the
first request on the connection. When per-directory SSL renegotiation occurs,
the bytes are associated with the request that triggered the renegotiation.

%package	mod_lua
Summary:	Provides Lua hooks into various portions of the httpd request processing
Group:		System/Servers

%description	mod_lua
This module allows the server to be extended with scripts written in the Lua
programming language. The extension points (hooks) available with mod_lua
include many of the hooks available to natively compiled Apache HTTP Server
modules, such as mapping requests to files, generating dynamic responses,
access control, authentication, and authorization

More information on the Lua programming language can be found at the the Lua
website.  mod_lua is still in experimental state. Until it is declared stable,
usage and behavior may change at any time, even between stable releases of
the 2.4.x series. Be sure to check the CHANGES file before upgrading.

%package	mod_env
Summary:	Modifies the environment which is passed to CGI scripts and SSI pages
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_env
This module allows for control of internal environment variables that are
used by various Apache HTTP Server modules. These variables are also provided
to CGI scripts as native system environment variables, and available for
use in SSI pages. Environment variables may be passed from the shell which
invoked the httpd process. Alternatively, environment variables may be set
or unset within the configuration process.

%package	mod_mime_magic
Summary:	Determines the MIME type of a file by looking at a few bytes of its contents
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_mime_magic
This module determines the MIME type of files in the same way the Unix
file(1) command works: it looks at the first few bytes of the file. It is
intended as a "second line of defense" for cases that mod_mime can't resolve.

This module is derived from a free version of the file(1) command for Unix,
which uses "magic numbers" and other hints from a file's contents to figure
out what the contents are. This module is active only if the magic file is
specified by the MimeMagicFile directive.

%package	mod_cern_meta
Summary:	CERN httpd metafile semantics
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_cern_meta
Emulate the CERN HTTPD Meta file semantics. Meta files are HTTP headers
that can be output in addition to the normal range of headers for each
file accessed. They appear rather like the Apache .asis files, and are
able to provide a crude way of influencing the Expires: header, as well as
providing other curiosities. There are many ways to manage meta information,
this one was chosen because there is already a large number of CERN users
who can exploit this module.

More information on the CERN metafile semantics is available.

%package	mod_expires
Summary:	Generation of Expires and Cache-Control HTTP headers
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_expires
This module controls the setting of the Expires HTTP header and the
max-age directive of the Cache-Control HTTP header in server responses.
The expiration date can set to be relative to either the time the source
file was last modified, or to the time of the client access.

These HTTP headers are an instruction to the client about the document's
validity and persistence. If cached, the document may be fetched from the
cache rather than from the source until this time has passed. After that,
the cache copy is considered "expired" and invalid, and a new copy must be
obtained from the source.

To modify Cache-Control directives other than max-age (see RFC 2616 section
14.9), you can use the Header directive.

When the Expires header is already part of the response generated by the
server, for example when generated by a CGI script or proxied from an origin
server, this module does not change or add an Expires or Cache-Control header.

%package	mod_headers
Summary:	Customization of HTTP request and response headers
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_headers
This module provides directives to control and modify HTTP request and
response headers. Headers can be merged, replaced or removed.

%package	mod_ident
Summary:	RFC 1413 ident lookups
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_ident
This module queries an RFC 1413 compatible daemon on a remote host to look
up the owner of a connection.

%package	mod_usertrack
Summary:	Clickstream logging of user activity on a site
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_usertrack
Provides tracking of a user through your website via browser cookies.

%package	mod_unique_id
Summary:	Provides an environment variable with a unique identifier for each request
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_unique_id
This module provides a magic token for each request which is guaranteed
to be unique across "all" requests under very specific conditions. The
unique identifier is even unique across multiple machines in a properly
configured cluster of machines. The environment variable UNIQUE_ID is set to
the identifier for each request. Unique identifiers are useful for various
reasons which are beyond the scope of this document.

%package	mod_setenvif
Summary:	Set the environment variables based on characteristics of the request
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_setenvif
The mod_setenvif module allows you to set internal environment variables
according to whether different aspects of the request match regular
expressions you specify. These environment variables can be used by other
parts of the server to make decisions about actions to be taken, as well
as becoming available to CGI scripts and SSI pages.

The directives are considered in the order they appear in the configuration
files. So more complex sequences can be used, such as this example, which
sets netscape if the browser is mozilla but not MSIE.

BrowserMatch ^Mozilla netscape BrowserMatch MSIE !netscape

%package	mod_version
Summary:	Version dependent configuration
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_version
This module is designed for the use in test suites and large networks which
have to deal with different httpd versions and different configurations. It
provides a new container -- <IfVersion>, which allows a flexible version
checking including numeric comparisons and regular expressions.

%package	mod_remoteip
Summary:	Replaces the original client IP address with the useragent IP address
Group:		System/Servers

%description	mod_remoteip
This module is used to treat the useragent which initiated the request
as the originating useragent as identified by httpd for the purposes of
authorization and logging, even where that useragent is behind a load
balancer, front end server, or proxy server.

The module overrides the client IP address for the connection with the
useragent IP address reported in the request header configured with the
RemoteIPHeader directive.

Once replaced as instructed, this overridden useragent IP address is then used
for the mod_authz_host <Require ip> feature, is reported by mod_status, and
is recorded by mod_log_config \%a and core \%a format strings. The underlying
client IP of the connection is available in the \%{c}a format string.  It is
critical to only enable this behavior from intermediate hosts (proxies,
etc) which are trusted by this server, since it is trivial for the remote
useragent to impersonate another useragent.

%package	mod_proxy
Summary:	Multi-protocol proxy/gateway server
Group:		System/Servers
Suggests:	apache-mod_proxy_connect
Suggests:	apache-mod_proxy_ftp
Suggests:	apache-mod_proxy_http
Suggests:	apache-mod_proxy_balancer

%description	mod_proxy
Do not enable proxying with ProxyRequests until you have secured your
server. Open proxy servers are dangerous both to your network and to the
Internet at large.

mod_proxy and related modules implement a proxy/gateway for Apache HTTP
Server, supporting a number of popular protocols as well as several different
load balancing algorithms. Third-party modules can add support for additional
protocols and load balancing algorithms.

A set of modules must be loaded into the server to provide the necessary
features. These modules can be included statically at build time
or dynamically via the LoadModule directive). The set must include: *
mod_proxy, which provides basic proxy capabilities * mod_proxy_balancer
and one or more balancer modules, if load
 balancing is required. (See mod_proxy_balancer for more information.)
* one or more proxy scheme, or protocol, modules:

 Protocol Module AJP13 (Apache JServe Protocol version 1.3) mod_proxy_ajp
 CONNECT (for SSL) mod_proxy_connect FastCGI mod_proxy_fcgi ftp mod_proxy_ftp
 HTTP/0.9, HTTP/1.0, and HTTP/1.1 mod_proxy_http SCGI mod_proxy_scgi

In addition, extended features are provided by other modules. Caching is
provided by mod_cache and related modules. The ability to contact remote
servers using the SSL/TLS protocol is provided by the SSLProxy* directives
of mod_ssl. These additional modules will need to be loaded and configured
to take advantage of these features.

%package	mod_proxy_connect
Summary:	mod_proxy extension for CONNECT request handling
Group:		System/Servers
Conflicts:	apache-proxy < 2.4.0

%description	mod_proxy_connect
This module requires the service of mod_proxy. It provides support for
the CONNECT HTTP method. This method is mainly used to tunnel SSL requests
through proxy servers.

Thus, in order to get the ability of handling CONNECT requests, mod_proxy
and mod_proxy_connect have to be present in the server.

CONNECT is also used, when the server needs to send an HTTPS request through
a forward proxy. In this case the server acts as a CONNECT client. This
functionality is part of mod_proxy and mod_proxy_connect is not needed in
this case.

Do not enable proxying until you have secured your server. Open proxy
servers are dangerous both to your network and to the Internet at large.

%package	mod_proxy_ftp
Summary:	FTP support module for mod_proxy
Group:		System/Servers
Conflicts:	apache-proxy < 2.4.0

%description	mod_proxy_ftp
This module requires the service of mod_proxy. It provides support for
the proxying FTP sites. Note that FTP support is currently limited to the
GET method.

Thus, in order to get the ability of handling FTP proxy requests, mod_proxy
and mod_proxy_ftp have to be present in the server.

Do not enable proxying until you have secured your server. Open proxy
servers are dangerous both to your network and to the Internet at large.

%package	mod_proxy_http
Summary:	HTTP support module for mod_proxy
Group:		System/Servers
Conflicts:	apache-proxy < 2.4.0

%description	mod_proxy_http
This module requires the service of mod_proxy. It provides the features used
for proxying HTTP and HTTPS requests. mod_proxy_http supports HTTP/0.9,
HTTP/1.0 and HTTP/1.1. It does not provide any caching abilities. If you
want to set up a caching proxy, you might want to use the additional service
of the mod_cache module.

Thus, in order to get the ability of handling HTTP proxy requests, mod_proxy
and mod_proxy_http have to be present in the server.

Do not enable proxying until you have secured your server. Open proxy
servers are dangerous both to your network and to the Internet at large.

%package	mod_proxy_fcgi
Summary:	FastCGI support module for mod_proxy
Group:		System/Servers

%description	mod_proxy_fcgi
This module requires the service of mod_proxy. It provides support for the
FastCGI protocol.

Thus, in order to get the ability of handling the FastCGI protocol, mod_proxy
and mod_proxy_fcgi have to be present in the server.

Unlike mod_fcgid and mod_fastcgi, mod_proxy_fcgi has no provision for
starting the application process; fcgistarter is provided for that purpose.

Do not enable proxying until you have secured your server. Open proxy
servers are dangerous both to your network and to the Internet at large.

%package	mod_proxy_scgi
Summary:	SCGI gateway module for mod_proxy
Group:		System/Servers
Conflicts:	apache-proxy < 2.4.0

%description	mod_proxy_scgi
This module requires the service of mod_proxy. It provides support for the
SCGI protocol, version 1.

Thus, in order to get the ability of handling the SCGI protocol, mod_proxy
and mod_proxy_scgi have to be present in the server.

Do not enable proxying until you have secured your server. Open proxy
servers are dangerous both to your network and to the Internet at large.

%package	mod_proxy_fdpass
Summary:	fdpass external process support module for mod_proxy
Group:		System/Servers

%description	mod_proxy_fdpass
This module requires the service of mod_proxy. It provides support for the
passing the socket of the client to another process.

mod_proxy_fdpass uses the ability of AF_UNIX domain sockets to pass an open
file descriptor to allow another process to finish handling a request.

The module has a proxy_fdpass_flusher provider interface, which allows
another module to optionally send the response headers, or even the start of
the response body. The default flush provider disables keep-alive, and sends
the response headers, letting the external process just send a response body.

At this time the only data passed to the external process is the client
socket. To receive a client socket, call recvfrom with an allocated struct
cmsghdr. Future versions of this module may include more data after the
client socket, but this is not implemented at this time.

%package	mod_proxy_ajp
Summary:	AJP support module for mod_proxy
Group:		System/Servers

%description	mod_proxy_ajp
This module requires the service of mod_proxy. It provides support for the
Apache JServ Protocol version 1.3 (hereafter AJP13).

Thus, in order to get the ability of handling AJP13 protocol, mod_proxy
and mod_proxy_ajp have to be present in the server.

Do not enable proxying until you have secured your server. Open proxy
servers are dangerous both to your network and to the Internet at large.

%package	mod_proxy_balancer
Summary:	mod_proxy extension for load balancing
Group:		System/Servers
Conflicts:	apache-proxy < 2.4.0

%description	mod_proxy_balancer
This module requires the service of mod_proxy. It provides load balancing
support for HTTP, FTP and AJP13 protocols

Load balancing scheduler algorithm is provided by not this module but
other modules such as: mod_lbmethod_byrequests, mod_lbmethod_bytraffic,
mod_lbmethod_bybusyness and mod_lbmethod_heartbeat.

Thus, in order to get the ability of load balancing, mod_proxy,
mod_proxy_balancer and at least one of load balancing scheduler algorithm
modules have to be present in the server.

Do not enable proxying until you have secured your server. Open proxy
servers are dangerous both to your network and to the Internet at large.

%package	mod_proxy_express
Summary:	Dynamic mass reverse proxy extension for mod_proxy
Group:		System/Servers

%description	mod_proxy_express
This module creates dynamically configured mass reverse proxies, by mapping
the Host: header of the HTTP request to a server name and backend URL
stored in a DBM file. This allows for easy use of a huge number of reverse
proxies with no configuration changes. It is much less feature-full than
mod_proxy_balancer, which also provides dynamic growth, but is intended
to handle much, much larger numbers of backends. It is ideally suited as
a front-end HTTP switch.

This module requires the service of mod_proxy.

Do not enable proxying until you have secured your server. Open proxy
servers are dangerous both to your network and to the Internet at large.

Limitations

* This module is not intended to replace the dynamic capability of
 mod_proxy_balancer. Instead, it is intended to be mostly a lightweight
 and fast alternative to using mod_rewrite with RewriteMap and the [P]
 flag for mapped reverse proxying.
* It does not support regex or pattern matching at all.  * It emulates:
 ProxyPass / backend.server:port ProxyPassReverse / backend.server:port
 That is, the entire URL is appended to the mapped backend URL. This is in
 keeping with the intent of being a simple but fast reverse proxy switch.

%package	mod_session
Summary:	Session support
Group:		System/Servers

%description	mod_session
The session modules make use of HTTP cookies, and as such can fall victim to
Cross Site Scripting attacks, or expose potentially private information to
clients. Please ensure that the relevant risks have been taken into account
before enabling the session functionality on your server.

This module provides support for a server wide per user session
interface. Sessions can be used for keeping track of whether a user has been
logged in, or for other per user information that should be kept available
across requests.

Sessions may be stored on the server, or may be stored on the browser.
Sessions may also be optionally encrypted for added security. These
features are divided into several modules in addition to mod_session;
mod_session_crypto, mod_session_cookie and mod_session_dbd. Depending on the
server requirements, load the appropriate modules into the server (either
statically at compile time or dynamically via the LoadModule directive).

Sessions may be manipulated from other modules that depend on the session,
or the session may be read from and written to using environment variables
and HTTP headers, as appropriate.

%package	mod_session_cookie
Summary:	Cookie based session support
Group:		System/Servers

%description	mod_session_cookie
The session modules make use of HTTP cookies, and as such can fall victim to
Cross Site Scripting attacks, or expose potentially private information to
clients. Please ensure that the relevant risks have been taken into account
before enabling the session functionality on your server.

This submodule of mod_session provides support for the storage of user
sessions on the remote browser within HTTP cookies.

Using cookies to store a session removes the need for the server or a group
of servers to store the session locally, or collaborate to share a session,
and can be useful for high traffic environments where a server based session
might be too resource intensive.

If session privacy is required, the mod_session_crypto module can be used to
encrypt the contents of the session before writing the session to the client.

For more details on the session interface, see the documentation for the
mod_session module.

%package	mod_session_crypto
Summary:	Session encryption support
Group:		System/Servers

%description	mod_session_crypto
The session modules make use of HTTP cookies, and as such can fall victim to
Cross Site Scripting attacks, or expose potentially private information to
clients. Please ensure that the relevant risks have been taken into account
before enabling the session functionality on your server.

This submodule of mod_session provides support for the encryption of user
sessions before being written to a local database, or written to a remote
browser via an HTTP cookie.

This can help provide privacy to user sessions where the contents of the
session should be kept private from the user, or where protection is needed
against the effects of cross site scripting attacks.

For more details on the session interface, see the documentation for the
mod_session module.

%package	mod_session_dbd
Summary:	DBD/SQL based session support
Group:		System/Servers

%description	mod_session_dbd
The session modules make use of HTTP cookies, and as such can fall victim to
Cross Site Scripting attacks, or expose potentially private information to
clients. Please ensure that the relevant risks have been taken into account
before enabling the session functionality on your server.

This submodule of mod_session provides support for the storage of user
sessions within a SQL database using the mod_dbd module.

Sessions can either be anonymous, where the session is keyed by a unique
UUID string stored on the browser in a cookie, or per user, where the
session is keyed against the userid of the logged in user.

SQL based sessions are hidden from the browser, and so offer a measure of
privacy without the need for encryption.

Different webservers within a server farm may choose to share a database,
and so share sessions with one another.

For more details on the session interface, see the documentation for the
mod_session module.

%package	mod_slotmem_shm
Summary:	Slot-based shared memory provider
Group:		System/Servers

%description	mod_slotmem_shm
mod_slotmem_shm is a memory provider which provides for creation and access
to a shared memory segment in which the datasets are organized in "slots."

All shared memory is cleared and cleaned with each restart, whether graceful
or not. The data itself is stored and restored within a file noted by the
name parameter in the create and attach calls.

%package	mod_slotmem_plain
Summary:	Slot-based shared memory provider
Group:		System/Servers

%description	mod_slotmem_plain
mod_slotmem_plain is a memory provider which provides for creation and access
to a plain memory segment in which the datasets are organized in "slots."

If the memory needs to be shared between threads and processes, a better
provider would be mod_slotmem_shm.

%package	mod_ssl
Summary:	Strong cryptography using the SSL and TLS protocols
Group:		System/Servers
Requires:	apache-mod_socache_shmcb
Requires(post):	openssl

%description	mod_ssl
This module provides SSL v2/v3 and TLS v1 support for the Apache HTTP
Server. It was contributed by Ralf S. Engelschall based on his mod_ssl
project and originally derived from work by Ben Laurie.

This module relies on OpenSSL to provide the cryptography engine.

Further details, discussion, and examples are provided in the SSL
documentation.

%package	mod_optional_hook_export
Summary:	ExportLogTransaction module
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_optional_hook_export
ExportLogTransaction module

%package	mod_optional_hook_import
Summary:	ImportOptionalHookTestHook module
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_optional_hook_import
ImportOptionalHookTestHook module

%package	mod_optional_fn_import
Summary:	ImportLogTransaction module
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_optional_fn_import
ImportLogTransaction module

%package	mod_optional_fn_export
Summary:	optional hook import module
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_optional_fn_export
Description:optional hook import module

%package	mod_dialup
Summary:	Send static content at a bandwidth rate limit, defined by old modem standards
Group:		System/Servers

%description	mod_dialup
It is a module that sends static content at a bandwidth rate limit, defined
by the various old modem standards. So, you can browse your site with a
56k V.92 modem, by adding something like this:

<Location /mysite> ModemStandard V.92 </Location>

Previously to do bandwidth rate limiting modules would have to block an entire
thread, for each client, and insert sleeps to slow the bandwidth down. Using
the new suspend feature, a handler can get callback N milliseconds in the
future, and it will be invoked by the Event MPM on a different thread,
once the timer hits. From there the handler can continue to send data to
the client.

%package	mod_lbmethod_byrequests
Summary:	Request Counting load balancer scheduler algorithm for mod_proxy_balancer
Group:		System/Servers

%description	mod_lbmethod_byrequests
This module does not provide any configuration directives of its own.
It requires the services of mod_proxy_balancer, and provides the byrequests
load balancing method..

%package	mod_lbmethod_bytraffic
Summary:	Weighted Traffic Counting load balancer scheduler for mod_proxy_balancer
Group:		System/Servers

%description	mod_lbmethod_bytraffic
This module does not provide any configuration directives of its own.
It requires the services of mod_proxy_balancer, and provides the bytraffic
load balancing method..

%package	mod_lbmethod_bybusyness
Summary:	Pending Request Counting load balancer scheduler for mod_proxy_balancer
Group:		System/Servers

%description	mod_lbmethod_bybusyness
This module does not provide any configuration directives of its own.
It requires the services of mod_proxy_balancer, and provides the bybusyness
load balancing method.

%package	mod_lbmethod_heartbeat
Summary:	Heartbeat Traffic Counting load balancer scheduler for mod_proxy_balancer
Group:		System/Servers

%description	mod_lbmethod_heartbeat
lbmethod=heartbeat uses the services of mod_heartmonitor to balance between
origin servers that are providing heartbeat info via the mod_heartbeat module.

This modules load balancing algorithm favors servers with more ready (idle)
capacity over time, but does not select the server with the most ready
capacity every time. Servers that have 0 active clients are penalized,
with the assumption that they are not fully initialized.

%package	mod_unixd
Summary:	Basic (required) security for Unix-family platforms
Group:		System/Servers

%description	mod_unixd
Basic (required) security for Unix-family platforms.

%package	mod_heartbeat
Summary:	sends messages with server status to frontend proxy
Group:		System/Servers

%description	mod_heartbeat
mod_heartbeat sends multicast messages to a mod_heartmonitor listener that
advertises the servers current connection count. Usually, mod_heartmonitor
will be running on a proxy server with mod_lbmethod_heartbeat loaded,
which allows ProxyPass to use the "heartbeat" lbmethod inside of ProxyPass.

mod_heartbeat itself is loaded on the origin server(s) that serve
requests through the proxy server(s).  To use mod_heartbeat, mod_status
and mod_watchdog must be either a static modules or, if a dynamic module,
must be loaded before mod_heartbeat.

%package	mod_heartmonitor
Summary:	centralized monitor for mod_heartbeat origin servers
Group:		System/Servers

%description	mod_heartmonitor
mod_heartmonitor listens for server status messages generated by
mod_heartbeat enabled origin servers and makes their status available
to mod_lbmethod_heartbeat. This allows ProxyPass to use the "heartbeat"
lbmethod inside of ProxyPass.

This module uses the services of mod_slotmem_shm when available instead
of flat-file storage. No configuration is required to use mod_slotmem_shm.
To use mod_heartmonitor, mod_status and mod_watchdog must be either a static
modules or, if a dynamic module, it must be loaded before mod_heartmonitor.

%package	mod_dav
Summary:	Distributed Authoring and Versioning (WebDAV) functionality
Group:		System/Servers

%description	mod_dav
This module provides class 1 and class 2 WebDAV ('Web-based Distributed
Authoring and Versioning') functionality for Apache. This extension to the
HTTP protocol allows creating, moving, copying, and deleting resources and
collections on a remote web server.

%package	mod_status
Summary:	Provides information on server activity and performance
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_status
The Status module allows a server administrator to find out how well their
server is performing. A HTML page is presented that gives the current server
statistics in an easily readable form. If required this page can be made
to automatically refresh (given a compatible browser).  Another page gives
a simple machine-readable list of the current server state.

The details given are: * The number of worker serving requests * The number
of idle worker * The status of each worker, the number of requests that
worker has
 performed and the total number of bytes served by the worker (*)
* A total number of accesses and byte count served (*) * The time the server
was started/restarted and the time it has been
 running for
* Averages giving the number of requests per second, the number of
 bytes served per second and the average number of bytes per request (*)
* The current percentage CPU used by each worker and in total by all
 workers combined (*)
* The current hosts and requests being processed (*)

The lines marked "(*)" are only available if ExtendedStatus is On. In
version 2.3.6, loading mod_status will toggle ExtendedStatus On by default.

%package	mod_autoindex
Summary:	Generates directory indexes automatically
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_autoindex
The index of a directory can come from one of two sources:

* A file written by the user, typically called index.html. The DirectoryIndex
  directive sets the name of this file. This is controlled by mod_dir.

* Otherwise, a listing generated by the server. The other directives control
  the format of this listing. The AddIcon, AddIconByEncoding and AddIconByType
  are used to set a list of icons to display for various file types; for each
  file listed, the first icon listed that matches the file is displayed. These
  are controlled by mod_autoindex.

The two functions are separated so that you can completely remove (or replace)
automatic index generation should you want to.

Automatic index generation is enabled with using Options +Indexes. See the
Options directive for more details.

If the FancyIndexing option is given with the IndexOptions directive,
the column headers are links that control the order of the display. If
you select a header link, the listing will be regenerated, sorted by the
values in that column. Selecting the same header repeatedly toggles between
ascending and descending order. These column header links are suppressed
with the IndexOptions directive's SuppressColumnSorting option.

Note that when the display is sorted by "Size", it's the actual size of
the files that's used, not the displayed value - so a 1010-byte file will
always be displayed before a 1011-byte file (if in ascending order) even
though they both are shown as "1K".

%package	mod_asis
Summary:	Sends files that contain their own HTTP headers
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_asis
This module provides the handler send-as-is which causes Apache HTTP Server
to send the document without adding most of the usual HTTP headers.

This can be used to send any kind of data from the server, including
redirects and other special HTTP responses, without requiring a cgi-script
or an nph script.

For historical reasons, this module will also process any file with the
mime type httpd/send-as-is.

%package	mod_info
Summary:	Provides a comprehensive overview of the server configuration
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_info
To configure mod_info, add the following to your httpd.conf file.

<Location /server-info> SetHandler server-info </Location>

You may wish to use mod_access inside the <Location> directive to limit
access to your server configuration information:

<Location /server-info> SetHandler server-info Require host example.com
</Location>

Once configured, the server information is obtained by accessing
http://your.host.example.com/server-info

%package	mod_suexec
Summary:	Allows CGI scripts to run as a specified user and Group
Group:		System/Servers

%description	mod_suexec
This module, in combination with the suexec support program allows CGI scripts
to run as a specified user and Group.

Normally, when a CGI or SSI program executes, it runs as the same user who is
running the web server.

%package	mod_cgi
Summary:	Execution of CGI scripts
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_cgi
Any file that has the handler cgi-script will be treated as a CGI script,
and run by the server, with its output being returned to the client. Files
acquire this handler either by having a name containing an extension defined
by the AddHandler directive, or by being in a ScriptAlias directory.

For an introduction to using CGI scripts with Apache, see our tutorial on
Dynamic Content With CGI.

When using a multi-threaded MPM under unix, the module mod_cgid should
be used in place of this module. At the user level, the two modules are
essentially identical.

For backward-compatibility, the cgi-script handler will also be activated
for any file with the mime-type application/x-httpd-cgi. The use of the
magic mime-type is deprecated.

%package	mod_cgid
Summary:	Execution of CGI scripts using an external CGI daemon
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_cgid
Except for the optimizations and the additional ScriptSock directive noted
below, mod_cgid behaves similarly to mod_cgi. See the mod_cgi summary for
additional details about Apache and CGI.

On certain unix operating systems, forking a process from a multi-threaded
server is a very expensive operation because the new process will replicate
all the threads of the parent process. In order to avoid incurring this
expense on each CGI invocation, mod_cgid creates an external daemon that
is responsible for forking child processes to run CGI scripts. The main
server communicates with this daemon using a unix domain socket.

This module is used by default instead of mod_cgi whenever a multi-threaded
MPM is selected during the compilation process. At the user level, this
module is identical in configuration and operation to mod_cgi. The only
exception is the additional directive ScriptSock which gives the name of
the socket to use for communication with the cgi daemon.

%package	mod_dav_fs
Summary:	filesystem provider for mod_dav
Group:		System/Servers
Conflicts:	apache-mod_dav < 2.4.0

%description	mod_dav_fs
This module requires the service of mod_dav. It acts as a support module
for mod_dav and provides access to resources located in the server's file
system. The formal name of this provider is filesystem.  mod_dav backend
providers will be invoked by using the Dav directive:

%package	mod_dav_lock
Summary:	generic locking module for mod_dav
Group:		System/Servers
Conflicts:	apache-mod_dav < 2.4.0

%description	mod_dav_lock
This module implements a generic locking API which can be used by any backend
provider of mod_dav. It requires at least the service of mod_dav. But without
a backend provider which makes use of it, it's useless and should not be
loaded into the server. A sample backend module which actually utilizes
mod_dav_lock is mod_dav_svn, the subversion provider module.

Note that mod_dav_fs does not need this generic locking module, because it
uses its own more specialized version.

In order to make mod_dav_lock functional, you just have to specify the
location of the lock database using the DavGenericLockDB directive described
below.

Developer's Note

In order to retrieve the pointer to the locking provider function, you have
to use the ap_lookup_provider API with the arguments dav-lock, generic, and 0.

%package	mod_vhost_alias
Summary:	Provides for dynamically configured mass virtual hosting
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_vhost_alias
This module creates dynamically configured virtual hosts, by allowing the
IP address and/or the Host: header of the HTTP request to be used as part
of the pathname to determine what files to serve. This allows for easy use
of a huge number of virtual hosts with similar configurations.

%package	mod_negotiation
Summary:	Provides for content negotiation
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_negotiation
Content negotiation, or more accurately content selection, is the selection
of the document that best matches the clients capabilities, from one of
several available documents. There are two implementations of this.  *
A type map (a file with the handler type-map) which explicitly
 lists the files containing the variants.
* A Multiviews search (enabled by the Multiviews Options), where the
 server does an implicit filename pattern match, and choose from amongst
 the results.

%package	mod_dir
Summary:	Provides for "trailing slash" redirects and serving directory index files
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_dir
The index of a directory can come from one of two sources: * A file written
by the user, typically called index.html. The
 DirectoryIndex directive sets the name of this file. This is controlled
 by mod_dir.
* Otherwise, a listing generated by the server. This is provided by
 mod_autoindex.

The two functions are separated so that you can completely remove (or replace)
automatic index generation should you want to.

A "trailing slash" redirect is issued when the server receives a
request for a URL http://servername/foo/dirname where dirname is
a directory. Directories require a trailing slash, so mod_dir issues a
redirect to http://servername/foo/dirname/.

%package	mod_imagemap
Summary:	Server-side imagemap processing
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_imagemap
This module processes .map files, thereby replacing the functionality of
the imagemap CGI program. Any directory or document type configured to
use the handler imap-file (using either AddHandler or SetHandler) will be
processed by this module.

The following directive will activate files ending with .map as imagemap
files:

AddHandler imap-file map

Note that the following is still supported:

AddType application/x-httpd-imap map

However, we are trying to phase out "magic MIME types" so we are deprecating
this method.

%package	mod_actions
Summary:	Provides for executing CGI scripts based on media type or request method
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_actions
This module has two directives. The Action directive lets you run CGI scripts
whenever a file of a certain MIME content type is requested.  The Script
directive lets you run CGI scripts whenever a particular method is used in
a request. This makes it much easier to execute scripts that process files.

%package	mod_speling
Summary:	Attempts to correct various minor misspellings
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_speling
Requests to documents sometimes cannot be served by the core apache server
because the request was misspelled or miscapitalized. This module addresses
this problem by trying to find a matching document, even after all other
modules gave up. It does its work by comparing each document name in the
requested directory against the requested document name without regard to
case, and allowing up to one misspelling (character insertion / omission /
transposition or wrong character). A list is built with all document names
which were matched using this strategy.

If, after scanning the directory, * no matching document was found, Apache
will proceed as usual and
 return a "document not found" error.
* only one document is found that "almost" matches the request, then
 it is returned in the form of a redirection response.
* more than one document with a close match was found, then the list
 of the matches is returned to the client, and the client can select the
 correct candidate.

%package	mod_userdir
Summary:	User-specific directories
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_userdir
This module allows user-specific directories to be accessed using the
http://example.com/~user/ syntax.

%package	mod_alias
Summary:	Provides for mapping and for URL redirection
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_alias
The directives contained in this module allow for manipulation and control of
URLs as requests arrive at the server. The Alias and ScriptAlias directives
are used to map between URLs and filesystem paths. This allows for content
which is not directly under the DocumentRoot served as part of the web
document tree. The ScriptAlias directive has the additional effect of
marking the target directory as containing only CGI scripts.

The Redirect directives are used to instruct clients to make a new request
with a different URL. They are often used when a resource has moved to a
new location.

mod_alias is designed to handle simple URL manipulation tasks. For more
complicated tasks such as manipulating the query string, use the tools
provided by mod_rewrite.

%package	mod_rewrite
Summary:	Provides a rule-based rewriting engine to rewrite requested URLs on the fly
Group:		System/Servers
Conflicts:	apache-modules < 2.4.0

%description	mod_rewrite
The mod_rewrite module uses a rule-based rewriting engine, based on a
regular-expression parser, to rewrite requested URLs on the fly. By default,
mod_rewrite maps a URL to a filesystem path. However, it can also be used
to redirect one URL to another URL, or to invoke an internal proxy fetch.

mod_rewrite provides a flexible and powerful way to manipulate URLs using
an unlimited number of rules. Each rule can have an unlimited number of
attached rule conditions, to allow you to rewrite URL based on server
variables, environment variables, HTTP headers, or time stamps.

mod_rewrite operates on the full URL path, including the path-info section. A
rewrite rule can be invoked in httpd.conf or in .htaccess.  The path generated
by a rewrite rule can include a query string, or can lead to internal
sub-processing, external request redirection, or internal proxy throughput.

Further details, discussion, and examples, are provided in the detailed
mod_rewrite documentation.

%package        mod_http2
Summary:        Provides HTTP2 Support
Group:          System/Servers
Conflicts:      apache-modules < 2.4.0

%description    mod_http2
This module provides HTTP/2 (RFC 7540) support for the Apache HTTP Server.

%package	htcacheclean
Summary:	Clean up the disk cache (for apache-mod_cache_disk)
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Suggests:	apache-mod_cache_disk = %{version}-%{release}
Suggests:	apache-mod_proxy = %{version}-%{release}

%description	htcacheclean
htcacheclean is used to keep the size of mod_cache_disk's storage within a
certain limit. This tool can run either manually or in daemon mode. When
running in daemon mode, it sleeps in the background and checks the cache
directories at regular intervals for cached content to be removed.

%package	devel
Summary:	Module development tools for the apache web server
Group:		Development/C
Requires:	apr-devel >= 1:1.4.6
Requires:	apr-util-devel >= 1.4.1
Requires:	autoconf automake libtool
Requires:	expat-devel
Requires:	sasl-devel
Requires:	openssl-devel
Requires:	pcre-devel
Requires:	perl >= 0:5.600
Requires:	pkgconfig
Requires:	zlib-devel

%description	devel
The apache-devel package contains the source code for the apache Web server and
the APXS binary you'll need to build Dynamic Shared Objects (DSOs) for apache.

If you are installing the apache Web server and you want to be able to compile
or develop additional modules for apache, you'll need to install this package.

%package	source
Summary:	The apache source code, including OpenMandriva patches
Group:		System/Servers

%description	source
The apache source code, including OpenMandriva patches. Use this package to build
your own customized apache if needed.

%package	doc
Summary:	The apache Manual
Group:		System/Servers
BuildArch:	noarch

%description	doc
This package contains the apache server documentation in HTML format.

Please view the documentaion by starting the apache server and your favourite
web browser and point to this URL: http://localhost/manual

%prep

%setup -q -n httpd-%{version} -a11
%patch0 -p0 -b .deplibs.droplet
%patch8 -p1 -b .apxs.droplet
%patch16 -p0 -b .fix_extra_htaccess_check.droplet
%patch18 -p0 -b .PR45994.droplet
%patch19 -p1 -b .linux3.droplet
%patch105 -p1 -b .filter.droplet
%patch106 -p1 -b .mdvConfig~
%patch107 -p1 -b .linkage~
%patch108 -p0 -b .buildfix~

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
    datadir:       /srv/www
    installbuilddir: %{_libdir}/apache/build
    errordir:      /srv/www/error
    iconsdir:      /srv/www/icons
    htdocsdir:     /srv/www/html
    manualdir:     %{_datadir}/doc/apache-doc
    cgidir:        /srv/www/cgi-bin
    localstatedir: /var
    runtimedir:    /var/run/httpd
    logfiledir:    /var/log/httpd
    proxycachedir: /var/cache/httpd/mod_proxy
</Layout>
EOF

#Fix DYNAMIC_MODULE_LIMIT
perl -pi -e "s/DYNAMIC_MODULE_LIMIT 256/DYNAMIC_MODULE_LIMIT %{?!maxmodules:%{defaultmaxmodules}}%{?maxmodules:%{maxmodules}}/;" include/httpd.h

# don't try to touch srclib
perl -pi -e "s|^SUBDIRS = .*|SUBDIRS = os server modules support|g" Makefile.in

# bump server limit
perl -pi -e "s|DEFAULT_SERVER_LIMIT 256|DEFAULT_SERVER_LIMIT %{?!serverlimit:%{defaultserverlimit}}%{?serverlimit:%{serverlimit}}|g" server/mpm/prefork/prefork.c

# tag it with the "legacy" name so that we can track this at netcraft...
perl -pi -e "s|^#define AP_SERVER_BASEPRODUCT .*|#define AP_SERVER_BASEPRODUCT \"%{BASEPRODUCT}\"|g" include/ap_release.h

# avoid regenerating code with yacc
pushd server
    touch util_expr_scan.c util_expr_parse.c util_expr_parse.h util_expr_scan.l util_expr_parse.y
popd

# use my nice converted transparent png icons
tar -jxf %{SOURCE3}
mv icons/*.png docs/icons/

# prepare the apache-source package
rm -rf %{_builddir}/tmp-httpd-%{version}; mkdir -p %{_builddir}/tmp-httpd-%{version}/usr/src
cp -dpR %{_builddir}/httpd-%{version} %{_builddir}/tmp-httpd-%{version}/usr/src/apache-%{version}
rm -rf %{_builddir}/tmp-httpd-%{version}/usr/src/apache-%{version}/tmp-httpd-%{version}/usr/src
rm -f %{_builddir}/tmp-httpd-%{version}%{_usrsrc}/apache-%{version}/*.spec
rm -rf %{_builddir}/tmp-httpd-%{version}/usr/src/apache-%{version}/Mandriva

# add the htcacheclean stuff
cp %{SOURCE9} htcacheclean.service
cp %{SOURCE10} htcacheclean.sysconfig

# this will only work if configured correctly in the config (FullOs)...
cp server/core.c server/core.c.untagged

# some adjustments here
perl -pi -e "s|_MODULE_DIR_|%{_libdir}/apache|g" OpenMandriva/*_mod_*.conf

# Build the systemd file
cp %{SOURCE15} httpd.service
for mpm in worker event; do
    sed "s,@NAME@,${mpm},g;s,@EXEC@,%{_sbindir}/httpd-${mpm},g" httpd.service > httpd-${mpm}.service
done
touch -r httpd.service httpd-${mpm}.service

%build
%serverbuild

#########################################################################################
# configure and build phase
#

# use a minimal buildconf instead
cp %{SOURCE100} buildconf
sh ./buildconf

CFLAGS="`echo $RPM_OPT_FLAGS |sed -e 's/-fomit-frame-pointer//'`"
CPPFLAGS="-DSSL_EXPERIMENTAL_ENGINE -DLDAP_DEPRECATED"
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

export SH_LDFLAGS="%{ldflags}"

APVARS="--enable-layout=NUX \
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
    --datadir=/srv/www \
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

for mpm in worker event prefork; do
    mkdir build-${mpm}; pushd build-${mpm}
    ln -s ../configure .

    if [ ${mpm} = prefork ]; then
        %configure2_5x $APVARS \
    	    --with-mpm=prefork \
    	    --enable-modules=all \
	    --enable-mods-shared=all \
    	    --with-ldap --enable-ldap=shared --enable-authnz-ldap=shared \
	    --enable-cache=shared --enable-disk-cache=shared --enable-file-cache=shared --enable-mem-cache=shared \
    	    --enable-ssl --with-ssl=%{_prefix} --disable-distcache \
    	    --enable-deflate=shared \
    	    --enable-cgid=shared \
    	    --enable-proxy=shared --enable-proxy-connect=shared --enable-proxy-ftp=shared \
    	    --enable-proxy-http=shared --enable-proxy-ajp=shared --enable-proxy-balancer=shared \
    	    --enable-dav=shared --enable-dav-fs=shared --enable-dav-lock=shared \
    	    --enable-version=shared \
    	    --enable-bucketeer=shared --enable-case-filter=shared --enable-case-filter-in=shared --enable-echo=shared \
    	    --enable-example=shared --enable-optional-fn-export=shared --enable-optional-fn-import=shared \
    	    --enable-optional-hook-export=shared --enable-optional-hook-import=shared \
	    --enable-charset_lite=shared --enable-authn_alias=shared \
	    --enable-cern-meta=shared \
	    --enable-ident=shared \
	    --enable-imagemap=shared \
	    --enable-suexec=shared

    # nuke excessive use of ldflags
    perl -pi -e "s|^LDFLAGS.*|LDFLAGS = %{ldflags}|g" build/config_vars.mk
    perl -pi -e "s|^SH_LDFLAGS.*|SH_LDFLAGS = %{ldflags}|g" build/config_vars.mk

    fi

    if [ ${mpm} = worker ]; then
	%configure2_5x $APVARS \
    	    --with-mpm=worker \
	    --enable-modules=none
    # don't build support tools
    perl -pi -e "s|^SUBDIRS = .*|SUBDIRS = os server modules|g" Makefile
    # nuke excessive use of ldflags
    perl -pi -e "s|^LDFLAGS.*|LDFLAGS = %{ldflags}|g" build/config_vars.mk
    perl -pi -e "s|^SH_LDFLAGS.*|SH_LDFLAGS = %{ldflags}|g" build/config_vars.mk
    fi

    if [ ${mpm} = event ]; then
	%configure2_5x $APVARS \
    	    --with-mpm=event \
	    --enable-modules=none
    # don't build support tools
    perl -pi -e "s|^SUBDIRS = .*|SUBDIRS = os server modules|g" Makefile
    # nuke excessive use of ldflags
    perl -pi -e "s|^LDFLAGS.*|LDFLAGS = %{ldflags}|g" build/config_vars.mk
    perl -pi -e "s|^SH_LDFLAGS.*|SH_LDFLAGS = %{ldflags}|g" build/config_vars.mk
    fi

    #Copy configure flags to a file in the apache-source rpm.
    cp config.nice %{_builddir}/tmp-httpd-%{version}%{_usrsrc}/apache-%{version}/config.nice.${mpm}

    # tag it with the mpm name too so that we can track this somehow at for example netcraft...
    MPM_NAME=`echo ${mpm}|tr "[a-z]" "[A-Z]"`
    cp ../server/core.c.untagged ../server/core.c
    perl -pi -e "s|\" PLATFORM \"|%{TAG}/${MPM_NAME}-%{release}|g" ../server/core.c

    # if libexpat0-devel is installed on x86_64 somehow the EXTRA_LDLAGS is set 
    # to -L/usr/lib, fix that with a conditional hack...
    %ifarch x86_64
	find -type f | xargs perl -pi -e "s|/usr/lib\b|%{_libdir}|g"
    %endif

    # finally doing the build stage
    %make
    popd
done

# Create default/prefork service file for systemd
sed "s,@NAME@,prefork,g;s,@EXEC@,%{_sbindir}/httpd,g" httpd.service > httpd.service.def
touch -r httpd.service httpd.service.def

%install
rm -rf %{buildroot}
#########################################################################################
# install phase

install -d %{buildroot}%{_libdir}/apache
install -d %{buildroot}%{_sysconfdir}/httpd/conf.d
install -d %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d
install -d %{buildroot}%{_sysconfdir}/httpd/conf/vhosts.d
install -d %{buildroot}%{_sysconfdir}/httpd/modules.d
install -d %{buildroot}%{_sysconfdir}/logrotate.d
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -d %{buildroot}/var/cache/httpd/mod_proxy
install -d %{buildroot}/var/lib/dav
install -d %{buildroot}/var/lib/dav/uploads
install -d %{buildroot}/var/log/httpd
install -d %{buildroot}/var/run/httpd
install -d %{buildroot}/srv/www/perl

#EXCLUDE_FROM_STRIP="%{buildroot}%{_sbindir}/httpd %{buildroot}%{_sbindir}/httpd-worker %{buildroot}%{_sbindir}/httpd-peruser"

# install source
tar -cf - -C %{_builddir}/tmp-httpd-%{version} usr/src | tar x -C %{buildroot} -f -

pushd build-prefork
make install \
	prefix=%{_sysconfdir}/httpd \
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
	datadir=%{buildroot}/srv/www \
	errordir=%{buildroot}/srv/www/error \
	iconsdir=%{buildroot}/srv/www/icons \
	htdocsdir=%{buildroot}/srv/www/html \
	manualdir=%{buildroot}%{_datadir}/doc/apache-doc \
	cgidir=%{buildroot}/srv/www/cgi-bin \
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
#perl -pi -e "s|htdocsdir =.*|htdocsdir = /srv/www/html|g" $CVMK
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
# install module conf files for the "modules.d" dir loading structure
install -m0644 OpenMandriva/*mod_*.conf %{buildroot}%{_sysconfdir}/httpd/modules.d/

install -d %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d

# install the mpm stuff
install -m0755 build-worker/httpd %{buildroot}%{_sbindir}/httpd-worker
install -m0755 build-event/httpd %{buildroot}%{_sbindir}/httpd-event

# install alternative MPMs; executables, man pages, and systemd service files
install -d %{buildroot}/lib/systemd/system
for mpm in worker event; do
    install -p -m 644 httpd-${mpm}.service %{buildroot}/lib/systemd/system/httpd-${mpm}.service
done

# Default httpd (prefork) service file
install -p -m 644 httpd.service.def %{buildroot}/lib/systemd/system/httpd.service

# install htcacheclean files
install -m0644 htcacheclean.service %{buildroot}/lib/systemd/system/htcacheclean.service
install -m0644 htcacheclean.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/htcacheclean

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

install -m0644 OpenMandriva/fileprotector.conf %{buildroot}%{_sysconfdir}/httpd/conf/fileprotector.conf
install -m0644 OpenMandriva/httpd.sysconf %{buildroot}%{_sysconfdir}/sysconfig/httpd
install -m0644 OpenMandriva/favicon.ico %{buildroot}/srv/www/html/
install -m0644 OpenMandriva/robots.txt %{buildroot}/srv/www/html/
install -m0644 OpenMandriva/rpm.png  %{buildroot}/srv/www/icons/
install -m0644 OpenMandriva/httpd.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/httpd

%multiarch_includes %{buildroot}%{_includedir}/apache/ap_config_layout.h

# rpm filetriggers
install -d %{buildroot}%{_localstatedir}/lib/rpm/filetriggers
cat > %{buildroot}%{_localstatedir}/lib/rpm/filetriggers/webapp.filter << EOF
^./etc/httpd/conf/webapps.d/.*\.conf$
EOF
install -m0755 %{SOURCE2} %{buildroot}%{_localstatedir}/lib/rpm/filetriggers/webapp.script

# add two important documentation files in the plain ASCII format
cp docs/manual/upgrading.html.en upgrading.html
cp docs/manual/new_features_2_4.html.en new_features_2_4.html

lynx -dump -nolist upgrading.html > upgrading.txt
lynx -dump -nolist new_features_2_4.html > new_features_2_4.txt

# fix the manual
find %{buildroot}%{_datadir}/doc/apache-doc -type d -exec chmod 755 {} \;
find %{buildroot}%{_datadir}/doc/apache-doc -type f -exec chmod 644 {} \;

# let's not ship those, they might reveal some information to unwanted eyes
rm -rf %{buildroot}/srv/www/cgi-bin/printenv*
rm -rf %{buildroot}/srv/www/cgi-bin/test-cgi

#########################################################################################
# install phase done
#

%clean
rm -rf %{buildroot}

# Clean up "install source" and other generated dirs
[ "%{_builddir}/tmp-httpd-%{version}%{_usrsrc}/apache-%{version}" != "/" ] && rm -rf %{_builddir}/tmp-httpd-%{version}%{_usrsrc}/apache-%{version}
[ "%{_builddir}/usr/src" != "/" ] && rm -rf %{_builddir}/usr/src
[ "%{_builddir}/tmp-httpd-%{version}" != "/" ] && rm -rf %{_builddir}/tmp-httpd-%{version}

%pre base
%_pre_useradd apache /srv/www /bin/sh

%postun base
%_postun_userdel apache

%triggerun -- %name < 2.4.3-1
# Deal with the /var/www -> /srv/www move
if [ -d /var/www -a ! -d /srv/www ]; then
	mv /var/www /srv/
fi

%post mpm-prefork
# Register the httpd service
if [ "$1" -eq "1" ] ; then 
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun mpm-prefork
if [ "$1" -eq "0" ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable %{all_services} > /dev/null 2>&1 || :
    /bin/systemctl stop %{all_services} > /dev/null 2>&1 || :
fi

%postun mpm-prefork
/bin/systemctl daemon-reload >/dev/null 2>&1 || :


%post mpm-worker
# Register the httpd service
if [ "$1" -eq "1" ] ; then 
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun mpm-worker
if [ "$1" -eq "0" ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable %{all_services} > /dev/null 2>&1 || :
    /bin/systemctl stop %{all_services} > /dev/null 2>&1 || :
fi

%postun mpm-worker
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%post mpm-event
# Register the httpd service
if [ "$1" -eq "1" ] ; then 
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun mpm-event
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable %{all_services} > /dev/null 2>&1 || :
    /bin/systemctl stop %{all_services} > /dev/null 2>&1 || :
fi

%postun mpm-event
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%post mod_authn_file
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_authn_file
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_authn_dbm
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_authn_dbm
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_authn_anon
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_authn_anon
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_authn_dbd
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_authn_dbd
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_authn_socache
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_authn_socache
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_authn_core
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_authn_core
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_authz_host
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_authz_host
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_authz_groupfile
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_authz_groupfile
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_authz_user
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_authz_user
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_authz_dbm
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_authz_dbm
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_authz_owner
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_authz_owner
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_authz_dbd
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_authz_dbd
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_authz_core
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_authz_core
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_authnz_ldap
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_authnz_ldap
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_access_compat
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_access_compat
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_auth_basic
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_auth_basic
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_auth_form
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_auth_form
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_auth_digest
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_auth_digest
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_allowmethods
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_allowmethods
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_file_cache
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_file_cache
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_cache
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_cache
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_cache_disk
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_cache_disk
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_socache_shmcb
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_socache_shmcb
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_socache_dbm
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_socache_dbm
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_socache_memcache
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_socache_memcache
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_watchdog
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_watchdog
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_dbd
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_dbd
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_bucketeer
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_bucketeer
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_dumpio
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_dumpio
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_echo
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_echo
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_case_filter
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_case_filter
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_case_filter_in
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_case_filter_in
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_buffer
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_buffer
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_data
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_data
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_ratelimit
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_ratelimit
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_reqtimeout
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_reqtimeout
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_ext_filter
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_ext_filter
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_request
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_request
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_include
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_include
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_filter
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_filter
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_reflector
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_reflector
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_substitute
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_substitute
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_sed
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_sed
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_charset_lite
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_charset_lite
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_deflate
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_deflate
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_xml2enc
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_xml2enc
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_proxy_html
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_proxy_html
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_mime
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_mime
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_ldap
%create_ghostfile /var/cache/httpd/mod_ldap_cache apache root 0600
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_ldap
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_log_config
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_log_config
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_log_debug
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_log_debug
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_log_forensic
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_log_forensic
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_logio
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_logio
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_lua
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_lua
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_env
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_env
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_mime_magic
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_mime_magic
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_cern_meta
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_cern_meta
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_expires
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_expires
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_headers
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_headers
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_ident
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_ident
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_usertrack
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_usertrack
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_unique_id
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_unique_id
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_setenvif
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_setenvif
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_version
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_version
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_remoteip
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_remoteip
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_proxy
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_proxy
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_proxy_connect
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_proxy_connect
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_proxy_ftp
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_proxy_ftp
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_proxy_http
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_proxy_http
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_proxy_fcgi
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_proxy_fcgi
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_proxy_scgi
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_proxy_scgi
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_proxy_fdpass
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_proxy_fdpass
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_proxy_ajp
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_proxy_ajp
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_proxy_balancer
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_proxy_balancer
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_proxy_express
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_proxy_express
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_session
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_session
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_session_cookie
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_session_cookie
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_session_crypto
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_session_crypto
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_session_dbd
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_session_dbd
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_slotmem_shm
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_slotmem_shm
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_slotmem_plain
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_slotmem_plain
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%pre mod_ssl
# http://qa.mandriva.com/show_bug.cgi?id=32773
# http://qa.mandriva.com/show_bug.cgi?id=33198
# If there was default mod_ssl vhost misplaced move it as rpmsave
if [ -f %{_sysconfdir}/httpd/modules.d/41_mod_ssl.default-vhost.conf -a ! -f  %{_sysconfdir}/httpd/conf/vhosts.d/01_default_ssl_vhost.conf ]; then
    mv -vf %{_sysconfdir}/httpd/modules.d/41_mod_ssl.default-vhost.conf %{_sysconfdir}/httpd/conf/vhosts.d/01_default_ssl_vhost.conf
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

# http://qa.mandriva.com/show_bug.cgi?id=33429
if [ -f /etc/pki/tls/certs/localhost.crt ]; then
    chmod 644 /etc/pki/tls/certs/localhost.crt
fi

/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_ssl
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_optional_hook_export
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_optional_hook_export
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_optional_hook_import
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_optional_hook_import
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_optional_fn_import
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_optional_fn_import
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_optional_fn_export
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_optional_fn_export
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_dialup
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_dialup
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_lbmethod_byrequests
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_lbmethod_byrequests
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_lbmethod_bytraffic
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_lbmethod_bytraffic
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_lbmethod_bybusyness
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_lbmethod_bybusyness
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_lbmethod_heartbeat
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_lbmethod_heartbeat
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_unixd
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_unixd
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_heartbeat
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_heartbeat
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_heartmonitor
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_heartmonitor
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_dav
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_dav
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_status
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_status
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_autoindex
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_autoindex
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_asis
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_asis
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_info
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_info
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_suexec
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_suexec
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_cgi
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_cgi
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_cgid
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_cgid
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_dav_fs
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_dav_fs
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_dav_lock
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_dav_lock
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_vhost_alias
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_vhost_alias
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_negotiation
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_negotiation
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_dir
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_dir
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_imagemap
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_imagemap
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_actions
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_actions
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_speling
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_speling
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_userdir
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_userdir
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_alias
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_alias
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_rewrite
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_rewrite
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mod_http2
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mod_http2
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post htcacheclean
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun htcacheclean
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%files mpm-prefork
%attr(0755,root,root) %{_sbindir}/httpd
/lib/systemd/system/httpd.service

%files mpm-worker
%attr(0755,root,root) %{_sbindir}/httpd-worker
/lib/systemd/system/httpd-worker.service

%files mpm-event
%attr(0755,root,root) %{_sbindir}/httpd-event
/lib/systemd/system/httpd-event.service

%files modules

%files mod_authn_file
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/001_mod_authn_file.conf
%attr(0755,root,root) %{_libdir}/apache/mod_authn_file.so

%files mod_authn_dbm
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/002_mod_authn_dbm.conf
%attr(0755,root,root) %{_libdir}/apache/mod_authn_dbm.so

%files mod_authn_anon
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/003_mod_authn_anon.conf
%attr(0755,root,root) %{_libdir}/apache/mod_authn_anon.so

%files mod_authn_dbd
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/004_mod_authn_dbd.conf
%attr(0755,root,root) %{_libdir}/apache/mod_authn_dbd.so

%files mod_authn_socache
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/005_mod_authn_socache.conf
%attr(0755,root,root) %{_libdir}/apache/mod_authn_socache.so

%files mod_authn_core
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/006_mod_authn_core.conf
%attr(0755,root,root) %{_libdir}/apache/mod_authn_core.so

%files mod_authz_host
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/007_mod_authz_host.conf
%attr(0755,root,root) %{_libdir}/apache/mod_authz_host.so

%files mod_authz_groupfile
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/008_mod_authz_groupfile.conf
%attr(0755,root,root) %{_libdir}/apache/mod_authz_groupfile.so

%files mod_authz_user
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/009_mod_authz_user.conf
%attr(0755,root,root) %{_libdir}/apache/mod_authz_user.so

%files mod_authz_dbm
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/010_mod_authz_dbm.conf
%attr(0755,root,root) %{_libdir}/apache/mod_authz_dbm.so

%files mod_authz_owner
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/011_mod_authz_owner.conf
%attr(0755,root,root) %{_libdir}/apache/mod_authz_owner.so

%files mod_authz_dbd
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/012_mod_authz_dbd.conf
%attr(0755,root,root) %{_libdir}/apache/mod_authz_dbd.so

%files mod_authz_core
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/013_mod_authz_core.conf
%attr(0755,root,root) %{_libdir}/apache/mod_authz_core.so

%files mod_authnz_ldap
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/014_mod_authnz_ldap.conf
%attr(0755,root,root) %{_libdir}/apache/mod_authnz_ldap.so

%files mod_access_compat
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/015_mod_access_compat.conf
%attr(0755,root,root) %{_libdir}/apache/mod_access_compat.so

%files mod_auth_basic
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/016_mod_auth_basic.conf
%attr(0755,root,root) %{_libdir}/apache/mod_auth_basic.so

%files mod_auth_form
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/017_mod_auth_form.conf
%attr(0755,root,root) %{_libdir}/apache/mod_auth_form.so

%files mod_auth_digest
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/018_mod_auth_digest.conf
%attr(0755,root,root) %{_libdir}/apache/mod_auth_digest.so

%files mod_allowmethods
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/019_mod_allowmethods.conf
%attr(0755,root,root) %{_libdir}/apache/mod_allowmethods.so

%files mod_file_cache
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/020_mod_file_cache.conf
%attr(0755,root,root) %{_libdir}/apache/mod_file_cache.so

%files mod_cache
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/021_mod_cache.conf
%attr(0755,root,root) %{_libdir}/apache/mod_cache.so

%files mod_cache_disk
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/022_mod_cache_disk.conf
%attr(0755,root,root) %{_libdir}/apache/mod_cache_disk.so

%files mod_cache_socache
%attr(0755,root,root) %{_libdir}/apache/mod_cache_socache.so

%files mod_socache_shmcb
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/023_mod_socache_shmcb.conf
%attr(0755,root,root) %{_libdir}/apache/mod_socache_shmcb.so

%files mod_socache_dbm
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/024_mod_socache_dbm.conf
%attr(0755,root,root) %{_libdir}/apache/mod_socache_dbm.so

%files mod_socache_memcache
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/025_mod_socache_memcache.conf
%attr(0755,root,root) %{_libdir}/apache/mod_socache_memcache.so

%files mod_watchdog
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/026_mod_watchdog.conf
%attr(0755,root,root) %{_libdir}/apache/mod_watchdog.so

%files mod_dbd
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/027_mod_dbd.conf
%attr(0755,root,root) %{_libdir}/apache/mod_dbd.so

%files mod_bucketeer
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/028_mod_bucketeer.conf
%attr(0755,root,root) %{_libdir}/apache/mod_bucketeer.so

%files mod_dumpio
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/029_mod_dumpio.conf
%attr(0755,root,root) %{_libdir}/apache/mod_dumpio.so

%files mod_echo
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/030_mod_echo.conf
%attr(0755,root,root) %{_libdir}/apache/mod_echo.so

%files mod_case_filter
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/031_mod_case_filter.conf
%attr(0755,root,root) %{_libdir}/apache/mod_case_filter.so

%files mod_case_filter_in
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/032_mod_case_filter_in.conf
%attr(0755,root,root) %{_libdir}/apache/mod_case_filter_in.so

%files mod_buffer
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/033_mod_buffer.conf
%attr(0755,root,root) %{_libdir}/apache/mod_buffer.so

%files mod_data
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/034_mod_data.conf
%attr(0755,root,root) %{_libdir}/apache/mod_data.so

%files mod_ratelimit
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/035_mod_ratelimit.conf
%attr(0755,root,root) %{_libdir}/apache/mod_ratelimit.so

%files mod_reqtimeout
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/036_mod_reqtimeout.conf
%attr(0755,root,root) %{_libdir}/apache/mod_reqtimeout.so

%files mod_ext_filter
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/037_mod_ext_filter.conf
%attr(0755,root,root) %{_libdir}/apache/mod_ext_filter.so

%files mod_request
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/038_mod_request.conf
%attr(0755,root,root) %{_libdir}/apache/mod_request.so

%files mod_include
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/039_mod_include.conf
%attr(0755,root,root) %{_libdir}/apache/mod_include.so

%files mod_filter
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/040_mod_filter.conf
%attr(0755,root,root) %{_libdir}/apache/mod_filter.so

%files mod_reflector
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/041_mod_reflector.conf
%attr(0755,root,root) %{_libdir}/apache/mod_reflector.so

%files mod_substitute
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/042_mod_substitute.conf
%attr(0755,root,root) %{_libdir}/apache/mod_substitute.so

%files mod_sed
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/043_mod_sed.conf
%attr(0755,root,root) %{_libdir}/apache/mod_sed.so

%files mod_charset_lite
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/044_mod_charset_lite.conf
%attr(0755,root,root) %{_libdir}/apache/mod_charset_lite.so

%files mod_deflate
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/045_mod_deflate.conf
%attr(0755,root,root) %{_libdir}/apache/mod_deflate.so

%files mod_macro
%attr(0755,root,root) %{_libdir}/apache/mod_macro.so

%files mod_xml2enc
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/046_mod_xml2enc.conf
%attr(0755,root,root) %{_libdir}/apache/mod_xml2enc.so

%files mod_proxy_html
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/047_mod_proxy_html.conf
%attr(0755,root,root) %{_libdir}/apache/mod_proxy_html.so

%files mod_proxy_wstunnel
%attr(0755,root,root) %{_libdir}/apache/mod_proxy_wstunnel.so

%files mod_mime
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/048_mod_mime.conf
%attr(0755,root,root) %{_libdir}/apache/mod_mime.so

%files mod_ldap
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/049_mod_ldap.conf
%attr(0755,root,root) %{_libdir}/apache/mod_ldap.so
%attr(0600,apache,root) %ghost /var/cache/httpd/mod_ldap_cache

%files mod_log_config
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/050_mod_log_config.conf
%attr(0755,root,root) %{_libdir}/apache/mod_log_config.so

%files mod_log_debug
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/051_mod_log_debug.conf
%attr(0755,root,root) %{_libdir}/apache/mod_log_debug.so

%files mod_log_forensic
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/052_mod_log_forensic.conf
%attr(0755,root,root) %{_libdir}/apache/mod_log_forensic.so

%files mod_logio
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/053_mod_logio.conf
%attr(0755,root,root) %{_libdir}/apache/mod_logio.so

%files mod_lua
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/054_mod_lua.conf
%attr(0755,root,root) %{_libdir}/apache/mod_lua.so

%files mod_env
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/055_mod_env.conf
%attr(0755,root,root) %{_libdir}/apache/mod_env.so

%files mod_mime_magic
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/056_mod_mime_magic.conf
%attr(0755,root,root) %{_libdir}/apache/mod_mime_magic.so

%files mod_cern_meta
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/057_mod_cern_meta.conf
%attr(0755,root,root) %{_libdir}/apache/mod_cern_meta.so

%files mod_expires
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/058_mod_expires.conf
%attr(0755,root,root) %{_libdir}/apache/mod_expires.so

%files mod_headers
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/059_mod_headers.conf
%attr(0755,root,root) %{_libdir}/apache/mod_headers.so

%files mod_ident
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/060_mod_ident.conf
%attr(0755,root,root) %{_libdir}/apache/mod_ident.so

%files mod_usertrack
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/061_mod_usertrack.conf
%attr(0755,root,root) %{_libdir}/apache/mod_usertrack.so

%files mod_unique_id
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/062_mod_unique_id.conf
%attr(0755,root,root) %{_libdir}/apache/mod_unique_id.so

%files mod_setenvif
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/063_mod_setenvif.conf
%attr(0755,root,root) %{_libdir}/apache/mod_setenvif.so

%files mod_version
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/064_mod_version.conf
%attr(0755,root,root) %{_libdir}/apache/mod_version.so

%files mod_remoteip
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/065_mod_remoteip.conf
%attr(0755,root,root) %{_libdir}/apache/mod_remoteip.so

%files mod_proxy
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/066_mod_proxy.conf
%attr(0755,root,root) %{_libdir}/apache/mod_proxy.so

%files mod_proxy_connect
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/067_mod_proxy_connect.conf
%attr(0755,root,root) %{_libdir}/apache/mod_proxy_connect.so

%files mod_proxy_ftp
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/068_mod_proxy_ftp.conf
%attr(0755,root,root) %{_libdir}/apache/mod_proxy_ftp.so

%files mod_proxy_http
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/069_mod_proxy_http.conf
%attr(0755,root,root) %{_libdir}/apache/mod_proxy_http.so

%files mod_proxy_fcgi
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/070_mod_proxy_fcgi.conf
%attr(0755,root,root) %{_libdir}/apache/mod_proxy_fcgi.so

%files mod_proxy_scgi
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/071_mod_proxy_scgi.conf
%attr(0755,root,root) %{_libdir}/apache/mod_proxy_scgi.so

%files mod_proxy_fdpass
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/072_mod_proxy_fdpass.conf
%attr(0755,root,root) %{_libdir}/apache/mod_proxy_fdpass.so

%files mod_proxy_ajp
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/073_mod_proxy_ajp.conf
%attr(0755,root,root) %{_libdir}/apache/mod_proxy_ajp.so

%files mod_proxy_balancer
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/074_mod_proxy_balancer.conf
%attr(0755,root,root) %{_libdir}/apache/mod_proxy_balancer.so

%files mod_proxy_express
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/075_mod_proxy_express.conf
%attr(0755,root,root) %{_libdir}/apache/mod_proxy_express.so

%files mod_session
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/076_mod_session.conf
%attr(0755,root,root) %{_libdir}/apache/mod_session.so

%files mod_session_cookie
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/077_mod_session_cookie.conf
%attr(0755,root,root) %{_libdir}/apache/mod_session_cookie.so

%files mod_session_crypto
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/078_mod_session_crypto.conf
%attr(0755,root,root) %{_libdir}/apache/mod_session_crypto.so

%files mod_session_dbd
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/079_mod_session_dbd.conf
%attr(0755,root,root) %{_libdir}/apache/mod_session_dbd.so

%files mod_slotmem_shm
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/080_mod_slotmem_shm.conf
%attr(0755,root,root) %{_libdir}/apache/mod_slotmem_shm.so

%files mod_slotmem_plain
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/081_mod_slotmem_plain.conf
%attr(0755,root,root) %{_libdir}/apache/mod_slotmem_plain.so

%files mod_ssl
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/082_mod_ssl.conf
%attr(0755,root,root) %{_libdir}/apache/mod_ssl.so
%attr(0700,apache,root) %dir /var/cache/httpd/mod_ssl
%attr(0600,apache,root) %ghost /var/cache/httpd/mod_ssl/scache.dir
%attr(0600,apache,root) %ghost /var/cache/httpd/mod_ssl/scache.pag
%attr(0600,apache,root) %ghost /var/cache/httpd/mod_ssl/scache.sem

%files mod_optional_hook_export
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/083_mod_optional_hook_export.conf
%attr(0755,root,root) %{_libdir}/apache/mod_optional_hook_export.so

%files mod_optional_hook_import
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/084_mod_optional_hook_import.conf
%attr(0755,root,root) %{_libdir}/apache/mod_optional_hook_import.so

%files mod_optional_fn_import
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/085_mod_optional_fn_import.conf
%attr(0755,root,root) %{_libdir}/apache/mod_optional_fn_import.so

%files mod_optional_fn_export
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/086_mod_optional_fn_export.conf
%attr(0755,root,root) %{_libdir}/apache/mod_optional_fn_export.so

%files mod_dialup
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/087_mod_dialup.conf
%attr(0755,root,root) %{_libdir}/apache/mod_dialup.so

%files mod_lbmethod_byrequests
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/088_mod_lbmethod_byrequests.conf
%attr(0755,root,root) %{_libdir}/apache/mod_lbmethod_byrequests.so

%files mod_lbmethod_bytraffic
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/089_mod_lbmethod_bytraffic.conf
%attr(0755,root,root) %{_libdir}/apache/mod_lbmethod_bytraffic.so

%files mod_lbmethod_bybusyness
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/090_mod_lbmethod_bybusyness.conf
%attr(0755,root,root) %{_libdir}/apache/mod_lbmethod_bybusyness.so

%files mod_lbmethod_heartbeat
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/091_mod_lbmethod_heartbeat.conf
%attr(0755,root,root) %{_libdir}/apache/mod_lbmethod_heartbeat.so

%files mod_unixd
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/092_mod_unixd.conf
%attr(0755,root,root) %{_libdir}/apache/mod_unixd.so

%files mod_heartbeat
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/093_mod_heartbeat.conf
%attr(0755,root,root) %{_libdir}/apache/mod_heartbeat.so

%files mod_heartmonitor
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/094_mod_heartmonitor.conf
%attr(0755,root,root) %{_libdir}/apache/mod_heartmonitor.so

%files mod_dav
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/095_mod_dav.conf
%attr(0755,root,root) %{_libdir}/apache/mod_dav.so
%attr(-,apache,apache) %dir /var/lib/dav
%attr(-,apache,apache) %dir /var/lib/dav/uploads

%files mod_status
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/096_mod_status.conf
%attr(0755,root,root) %{_libdir}/apache/mod_status.so

%files mod_autoindex
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/097_mod_autoindex.conf
%attr(0755,root,root) %{_libdir}/apache/mod_autoindex.so

%files mod_asis
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/098_mod_asis.conf
%attr(0755,root,root) %{_libdir}/apache/mod_asis.so

%files mod_info
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/099_mod_info.conf
%attr(0755,root,root) %{_libdir}/apache/mod_info.so

%files mod_suexec
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/100_mod_suexec.conf
%attr(0755,root,root) %{_libdir}/apache/mod_suexec.so
%attr(0755,root,root) %{_sbindir}/suexec
%attr(0644,root,root) %{_mandir}/man8/suexec.8*

%files mod_cgi
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/101_mod_cgi.conf
%attr(0755,root,root) %{_libdir}/apache/mod_cgi.so

%files mod_cgid
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/102_mod_cgid.conf
%attr(0755,root,root) %{_libdir}/apache/mod_cgid.so

%files mod_dav_fs
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/103_mod_dav_fs.conf
%attr(0755,root,root) %{_libdir}/apache/mod_dav_fs.so

%files mod_dav_lock
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/104_mod_dav_lock.conf
%attr(0755,root,root) %{_libdir}/apache/mod_dav_lock.so

%files mod_vhost_alias
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/105_mod_vhost_alias.conf
%attr(0755,root,root) %{_libdir}/apache/mod_vhost_alias.so

%files mod_negotiation
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/106_mod_negotiation.conf
%attr(0755,root,root) %{_libdir}/apache/mod_negotiation.so

%files mod_dir
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/107_mod_dir.conf
%attr(0755,root,root) %{_libdir}/apache/mod_dir.so

%files mod_imagemap
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/108_mod_imagemap.conf
%attr(0755,root,root) %{_libdir}/apache/mod_imagemap.so

%files mod_actions
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/109_mod_actions.conf
%attr(0755,root,root) %{_libdir}/apache/mod_actions.so

%files mod_speling
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/110_mod_speling.conf
%attr(0755,root,root) %{_libdir}/apache/mod_speling.so

%files mod_userdir
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/111_mod_userdir.conf
%attr(0755,root,root) %{_libdir}/apache/mod_userdir.so

%files mod_alias
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/112_mod_alias.conf
%attr(0755,root,root) %{_libdir}/apache/mod_alias.so

%files mod_rewrite
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/113_mod_rewrite.conf
%attr(0755,root,root) %{_libdir}/apache/mod_rewrite.so

%files mod_http2
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/114_mod_http2.conf
%attr(0755,root,root) %{_libdir}/apache/mod_http2.so

%files base
%defattr(-,root,root)
%doc upgrading.txt new_features_2_4.txt
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/httpd
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/httpd
%dir %{_sysconfdir}/httpd
%dir %{_sysconfdir}/httpd/conf
%dir %{_sysconfdir}/httpd/conf/webapps.d
%dir %{_sysconfdir}/httpd/conf/vhosts.d
%dir %{_sysconfdir}/httpd/conf.d
%dir %{_sysconfdir}/httpd/modules.d
%dir %{_sysconfdir}/httpd/conf/extra
%dir %{_sysconfdir}/httpd/conf/original
%dir %{_sysconfdir}/httpd/conf/original/extra
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/extra/httpd-autoindex.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/extra/httpd-dav.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/extra/httpd-default.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/extra/httpd-info.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/extra/httpd-languages.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/extra/httpd-manual.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/extra/httpd-mpm.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/extra/httpd-multilang-errordoc.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/extra/httpd-ssl.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/extra/httpd-userdir.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/extra/httpd-vhosts.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/extra/proxy-html.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/httpd.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/magic
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/mime.types
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/original/extra/httpd-autoindex.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/original/extra/httpd-dav.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/original/extra/httpd-default.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/original/extra/httpd-info.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/original/extra/httpd-languages.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/original/extra/httpd-manual.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/original/extra/httpd-mpm.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/original/extra/httpd-multilang-errordoc.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/original/extra/httpd-ssl.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/original/extra/httpd-userdir.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/original/extra/httpd-vhosts.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/original/extra/proxy-html.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/original/httpd.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/fileprotector.conf
%attr(0755,apache,apache) %dir /srv/www
%attr(0755,apache,apache) %dir /var/run/httpd
%attr(0755,root,root) %dir /srv/www/html
%dir /srv/www/error
%dir /srv/www/error/include
%dir /srv/www/icons
/srv/www/icons/*.svg
%dir /srv/www/icons/small
%dir /var/log/httpd
%dir /srv/www/cgi-bin
%dir /srv/www/perl
%config(noreplace,missingok) /srv/www/error/README
%config(noreplace,missingok) /srv/www/error/*.var
%config(noreplace,missingok) /srv/www/error/include/*.html
%attr(0644,root,root) /srv/www/icons/README*
%attr(0644,root,root) /srv/www/icons/*.png
%attr(0644,root,root) /srv/www/icons/*.gif
%attr(0644,root,root) /srv/www/icons/small/*.png
%attr(0644,root,root) /srv/www/icons/small/*.gif
%attr(0644,root,root) %config(noreplace) /srv/www/html/index.html
%attr(0644,root,root) %config(noreplace) /srv/www/html/favicon.ico
%attr(0644,root,root) %config(noreplace) /srv/www/html/robots.txt
%attr(0755,root,root) %{_bindir}/ab
%attr(0755,root,root) %{_bindir}/dbmmanage
%attr(0755,root,root) %{_bindir}/htdbm
%attr(0755,root,root) %{_bindir}/htdigest
%attr(0755,root,root) %{_bindir}/htpasswd
%attr(0755,root,root) %{_bindir}/httxt2dbm
%attr(0755,root,root) %{_bindir}/logresolve
%attr(0755,root,root) %{_sbindir}/apachectl
%attr(0755,root,root) %{_sbindir}/check_forensic
%attr(0755,root,root) %{_sbindir}/checkgid
%attr(0755,root,root) %{_sbindir}/fcgistarter
%attr(0755,root,root) %{_sbindir}/list_hooks.pl
%attr(0755,root,root) %{_sbindir}/logresolve.pl
%attr(0755,root,root) %{_sbindir}/log_server_status
%attr(0755,root,root) %{_sbindir}/rotatelogs
%attr(0755,root,root) %{_sbindir}/split-logfile
%attr(0755,root,root) %dir %{_libdir}/apache
%attr(0700,apache,root) %dir /var/cache/httpd
%{_localstatedir}/lib/rpm/filetriggers/webapp.*
%exclude %{_mandir}/man8/htcacheclean.8*
%exclude %{_mandir}/man8/suexec.8*
%{_mandir}/*/*

%files htcacheclean
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/htcacheclean
%attr(0755,root,root) %{_sbindir}/htcacheclean
%{_mandir}/man8/htcacheclean.8*
/lib/systemd/system/htcacheclean.service

%files devel
%{multiarch_includedir}/apache/ap_config_layout.h
%{_includedir}/apache
%attr(0755,root,root) %dir %{_libdir}/apache/build
%attr(0644,root,root) %{_libdir}/apache/build/*.mk
%attr(0755,root,root) %{_libdir}/apache/build/*.sh
%attr(0755,root,root) %{_libdir}/apache/build/envvars
%attr(0755,root,root) %{_sbindir}/envvars-std
%attr(0755,root,root) %{_bindir}/apxs
%attr(0755,root,root) %{_libdir}/apache/httpd.exp

%files source
%{_usrsrc}/apache-%{version}

%files doc
%{_datadir}/doc/apache-doc
