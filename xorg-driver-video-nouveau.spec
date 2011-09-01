%define	snap	20110901
%define	rel	1
Summary:	X.org video driver for NVIDIA graphics chipsets
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów graficznych NVIDIA
Name:		xorg-driver-video-nouveau
Version:	0.0.16
Release:	0.%{snap}.%{rel}
License:	MIT
Group:		X11/Applications
# git clone --depth 1 git://git.freedesktop.org/git/nouveau/xf86-video-nouveau
# cd xf86-video-nouveau
# git archive master --prefix xf86-video-nouveau/ | bzip2 > ../xf86-video-nouveau-$(date +%Y%m%d).tar.bz2
Source0:	xf86-video-nouveau-%{snap}.tar.bz2
# Source0-md5:	1dd6205c74736ebb28675d98c3185c83
URL:		http://nouveau.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.4.24
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	udev-devel
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.10
BuildRequires:	xorg-proto-dri2proto-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-glproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.7.0
%{?requires_xorg_xserver_videodrv}
Requires:	libdrm >= 2.4.24
Requires:	xorg-lib-libpciaccess >= 0.10
Requires:	xorg-xserver-libdri >= 1.7.0
Requires:	xorg-xserver-libglx >= 1.7.0
Requires:	xorg-xserver-server >= 1.7.0
Provides:	xorg-driver-video
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for NVIDIA video adapters. It supports PCI,
PCI-Express and AGP video cards based on the following chips:
- RIVA TNT (NV4),
- RIVA TNT2 (NV5),
- GeForce 256, QUADRO (NV10),
- GeForce2, QUADRO2 (NV11, NV15),
- GeForce3, QUADRO DCC (NV20),
- nForce, nForce2 (NV1A, NV1F),
- GeForce4, QUADRO4 (NV17, NV18, NV25, NV28),
- GeForce FX, QUADRO FX (NV30, NV31, NV34, NV35, NV36, NV37, NV38),
- GeForce 6xxx (NV40, NV41, NV43, NV44, NV45, C51),
- GeForce 7xxx (G70, G71, G72, G73).

%description -l pl.UTF-8
Sterownik obrazu X.org dla kart graficznych NVIDIA. Obsługuje karty
PCI, PCI-Express i AGP oparte na następujących układach:
- RIVA TNT (NV4),
- RIVA TNT2 (NV5),
- GeForce 256, QUADRO (NV10),
- GeForce2, QUADRO2 (NV11, NV15),
- GeForce3, QUADRO DCC (NV20),
- nForce, nForce2 (NV1A, NV1F),
- GeForce4, QUADRO4 (NV17, NV18, NV25, NV28),
- GeForce FX, QUADRO FX (NV30, NV31, NV34, NV35, NV36, NV37, NV38),
- GeForce 6xxx (NV40, NV41, NV43, NV44, NV45, C51),
- GeForce 7xxx (G70, G71, G72, G73).

%prep
%setup -q -n xf86-video-nouveau

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

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
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/*.so
%{_mandir}/man4/nouveau.4*
