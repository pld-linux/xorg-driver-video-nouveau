Summary:	X.org video driver for NVIDIA graphics chipsets
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów graficznych NVIDIA
Name:		xorg-driver-video-nouveau
Version:	1.0.16
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/archive/individual/driver/xf86-video-nouveau-%{version}.tar.bz2
# Source0-md5:	ecd9be89d853301167e3d564c49f7a8e
URL:		https://nouveau.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.4.60
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig >= 1:0.24
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	udev-devel
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.10
BuildRequires:	xorg-proto-dri2proto-devel >= 2.6
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-glproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.8
%{?requires_xorg_xserver_videodrv}
Requires:	libdrm >= 2.4.60
Requires:	xorg-lib-libpciaccess >= 0.10
Requires:	xorg-xserver-libdri >= 1.8
Requires:	xorg-xserver-libglx >= 1.8
Requires:	xorg-xserver-server >= 1.8
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
- GeForce 6xxx (NV40, NV41, NV43, NV44, NV45, C51, MCP61),
- GeForce 7xxx (G70, G71, G72, G73, NCP67, MCP68, MCP73),
- GeForce 8xxx, 9xxx, 2xx, 3xx (G80, G84, G86, G92, G94, G96, G98,
  G200, GT215, GT216, GT218, MCP77, MCP79, MCP89),
- GeForce 4xx, 5xx (GF100, GF104, GF106, GF108, GF110, GF114, GF116,
  GF117, GF119),
- GeForce 6xx, 7xx (GK104, GK106, GK107, GK110, GK208),
- GeForce GTX 750 (GM107, GM108),
- GeForce GTX 9xx (GM200, GM204, GM206),
- GeForce GTX 10xx (GP102, GP104, GP106, GP107, GP108).

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
- GeForce 6xxx (NV40, NV41, NV43, NV44, NV45, C51, MCP61),
- GeForce 7xxx (G70, G71, G72, G73, NCP67, MCP68, MCP73),
- GeForce 8xxx, 9xxx, 2xx, 3xx (G80, G84, G86, G92, G94, G96, G98,
  G200, GT215, GT216, GT218, MCP77, MCP79, MCP89),
- GeForce 4xx, 5xx (GF100, GF104, GF106, GF108, GF110, GF114, GF116,
  GF117, GF119),
- GeForce 6xx, 7xx (GK104, GK106, GK107, GK110, GK208),
- GeForce GTX 750 (GM107, GM108),
- GeForce GTX 9xx (GM200, GM204, GM206),
- GeForce GTX 10xx (GP102, GP104, GP106, GP107, GP108).

%prep
%setup -q -n xf86-video-nouveau-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/drivers/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/nouveau_drv.so
%{_mandir}/man4/nouveau.4*
