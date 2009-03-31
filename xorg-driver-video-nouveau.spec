%define	snap	20090331
Summary:	X.org video driver for NVIDIA video adapters
Summary(pl.UTF-8):	Sterownik obrazu X.org dla kart graficznych NVIDIA
Name:		xorg-driver-video-nouveau
Version:	0.0.10
Release:	0.%{snap}.1
License:	MIT
Group:		X11/Applications
# git://git.freedesktop.org/git/nouveau/xf86-video-nouveau
Source0:	xf86-video-nouveau-%{snap}.tar.bz2
# Source0-md5:	165e3ef74dab176145b73bb9c35ec719
URL:		http://nouveau.freedesktop.org
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.4.5-2
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-util-util-macros >= 1.1.3
BuildRequires:	xorg-xserver-server-devel >= 1.2
%requires_xorg_xserver_videodrv
Requires:	libdrm >= 2.4.5-2
Requires:	xorg-xserver-server >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for NVIDIA video adapters.

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

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/nouveau_drv.so
%{_mandir}/man4/nouveau.4*
