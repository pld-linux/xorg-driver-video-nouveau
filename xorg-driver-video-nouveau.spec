%define	snap	20070503
Summary:	X.org video driver for Nvidia graphics chipsets
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów graficznych Nvidia
Name:		xorg-driver-video-nouveau
Version:	0.1
Release:	0.%{snap}.1
License:	MIT
Group:		X11/Applications
# http://gitweb.freedesktop.org/?p=nouveau/xf86-video-nouveau.git;a=summary
Source0:	xf86-video-nouveau-20070503.tar.bz2
# Source0-md5:	4ac829217c64e463fd920e73d1a3b830
URL:		http://nouveau.freedesktop.org/wiki/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.4
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXvMC-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.3.0.0
Requires:	xorg-xserver-server >= 1.3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Nvidia graphics chipsets.

%description -l pl.UTF-8
Sterownik obrazu X.org dla układów graficznych Nvidia

%prep
%setup -q -n xf86-video-nouveau

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/*.so
%{_mandir}/man4/nouveau.4*
