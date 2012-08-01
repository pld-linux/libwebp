#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs

Summary:	WebP image codec library and tools
Summary(pl.UTF-8):	Biblioteka i narzędzia do kodeka obrazów WebP
Name:		libwebp
Version:	0.1.99
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: http://code.google.com/p/webp/downloads/list
Source0:	http://webp.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	aca4d43f3e8d1d9f87136d116acfb68d
URL:		https://developers.google.com/speed/webp/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebP image codec library and tools.

%description -l pl.UTF-8
Biblioteka i narzędzia do kodeka obrazów WebP.

%package devel
Summary:	Header files for WebP library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki WebP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for WebP library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki WebP.

%package static
Summary:	Static WebP library
Summary(pl.UTF-8):	Statyczna biblioteka WebP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static WebP library.

%description static -l pl.UTF-8
Statyczna biblioteka WebP.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkgconfig
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libwebp.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS PATENTS README
%attr(755,root,root) %{_bindir}/cwebp
%attr(755,root,root) %{_bindir}/dwebp
%attr(755,root,root) %{_libdir}/libwebp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwebp.so.3
%{_mandir}/man1/cwebp.1*
%{_mandir}/man1/dwebp.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwebp.so
%{_includedir}/webp
%{_pkgconfigdir}/libwebp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libwebp.a
