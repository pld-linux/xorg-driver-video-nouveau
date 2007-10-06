%define	snap	20071006
Summary:	X.org video driver for NVIDIA graphics chipsets
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów graficznych NVIDIA
Name:		xorg-driver-video-nouveau
Version:	0.1
Release:	0.%{snap}.1
License:	MIT
Group:		X11/Applications
# http://gitweb.freedesktop.org/?p=nouveau/xf86-video-nouveau.git;a=summary
Source0:	xf86-video-nouveau-%{snap}.tar.gz
# Source0-md5:	04cb9a55dbdb938c6f6726acd2f6af61
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
BuildRequires:  rpmbuild(macros) >= 1.389
%requires_xorg_xserver_videodrv
Requires:	xorg-xserver-server >= 1.3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for NVIDIA video adapters. It supports PCI,
PCI-Express and AGP video cards based on the following chips:
RIVA 128 (NV3), RIVA TNT (NV4), RIVA TNT2 (NV5), GeForce 256, QUADRO
(NV10), GeForce2, QUADRO2 (NV11, NV15), GeForce3, QUADRO DCC (NV20),
nForce, nForce2 (NV1A, NV1F), GeForce4, QUADRO4 (NV17, NV18, NV25,
NV28), GeForce FX, QUADRO FX (NV30, NV31, NV34, NV35, NV36, NV37,
NV38), GeForce 6xxx (NV40, NV41, NV43, NV44, NV45, C51), GeForce 7xxx
(G70, G71, G72, G73).

%description -l pl.UTF-8
Sterownik obrazu X.org dla kart graficznych NVIDIA. Obsługuje karty
PCI, PCI-Express i AGP oparte na następujących układach: RIVA 128
(NV3), RIVA TNT (NV4), RIVA TNT2 (NV5), GeForce 256, QUADRO (NV10),
GeForce2, QUADRO2 (NV11, NV15), GeForce3, QUADRO DCC (NV20), nForce,
nForce2 (NV1A, NV1F), GeForce4, QUADRO4 (NV17, NV18, NV25, NV28),
GeForce FX, QUADRO FX (NV30, NV31, NV34, NV35, NV36, NV37, NV38),
GeForce 6xxx (NV40, NV41, NV43, NV44, NV45, C51), GeForce 7xxx (G70,
G71, G72, G73).

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

%files
%defattr(644,root,root,755)
%doc COPYING README.NV1
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/*.so
%{_mandir}/man4/nouveau.4*
