Summary:	Galago feed for Evolution Data Server
Summary(pl.UTF-8):	Połączenie z Galago dla Evolution Data Servera
Name:		eds-feed
Version:	0.5.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.galago-project.org/files/releases/source/eds-feed/%{name}-%{version}.tar.bz2
# Source0-md5:	c4e4dfa8a701577e8dba2db000f5c864
URL:		http://galago-project.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	evolution-data-server-devel
BuildRequires:	libgalago-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Galago feed for Evolution Data Server

%description -l pl.UTF-8
Połączenie z Galago dla Evolution Data Servera.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/galago/eds-feed
