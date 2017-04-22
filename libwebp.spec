#
# Conditional build:
%bcond_without	opengl	# OpenGL-based visualizer
#
Summary:	WebP image codec libraries
Summary(pl.UTF-8):	Biblioteki do kodeka obrazów WebP
Name:		libwebp
Version:	0.6.0
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: http://downloads.webmproject.org/releases/webp/index.html
Source0:	http://downloads.webmproject.org/releases/webp/%{name}-%{version}.tar.gz
# Source0-md5:	19a6e926ab1721268df03161b84bb4a0
URL:		https://developers.google.com/speed/webp/
%{?with_opengl:BuildRequires:	OpenGL-devel}
%{?with_opengl:BuildRequires:	OpenGL-glut-devel}
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	giflib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebP image codec libraries.

%description -l pl.UTF-8
Biblioteki do kodeka obrazów WebP.

%package devel
Summary:	Header files for WebP libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek WebP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for WebP libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek WebP.

%package static
Summary:	Static WebP libraries
Summary(pl.UTF-8):	Statyczne biblioteki WebP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static WebP libraries.

%description static -l pl.UTF-8
Statyczne biblioteki WebP.

%package progs
Summary:	WebP image codec tools
Summary(pl.UTF-8):	Narzędzia do kodeka obrazów WebP
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
WebP image codec tools.

%description progs -l pl.UTF-8
Narzędzia do kodeka obrazów WebP.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-libwebpdemux \
	--enable-libwebpextras \
	--enable-libwebpmux
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkgconfig
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libwebp*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS PATENTS README
%attr(755,root,root) %{_libdir}/libwebp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwebp.so.7
%attr(755,root,root) %{_libdir}/libwebpdemux.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwebpdemux.so.2
%attr(755,root,root) %{_libdir}/libwebpmux.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwebpmux.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwebp.so
%attr(755,root,root) %{_libdir}/libwebpdemux.so
%attr(755,root,root) %{_libdir}/libwebpmux.so
%{_includedir}/webp
%{_pkgconfigdir}/libwebp.pc
%{_pkgconfigdir}/libwebpdemux.pc
%{_pkgconfigdir}/libwebpmux.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libwebp.a
%{_libdir}/libwebpdemux.a
%{_libdir}/libwebpmux.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cwebp
%attr(755,root,root) %{_bindir}/dwebp
%attr(755,root,root) %{_bindir}/gif2webp
%attr(755,root,root) %{_bindir}/img2webp
%{?with_opengl:%attr(755,root,root) %{_bindir}/vwebp}
%attr(755,root,root) %{_bindir}/webpmux
%{_mandir}/man1/cwebp.1*
%{_mandir}/man1/dwebp.1*
%{_mandir}/man1/gif2webp.1*
%{?with_opengl:%{_mandir}/man1/vwebp.1*}
%{_mandir}/man1/webpmux.1*
