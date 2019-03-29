Summary: Simple DirectMedia Layer 2
Name: SDL2
Version: 2.0.9
Release: 1
Source: http://www.libsdl.org/release/%{name}-%{version}.tar.gz
URL: http://www.libsdl.org/
License: zlib
Group: System/GUI/Other
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(glesv1_cm)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libpulse-simple)

Patch0: sdl2-disable-clipboard.patch
Patch1: sdl2-add-support-for-orientation-in-wayland.patch

%description
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

%package devel
Summary: Simple DirectMedia Layer 2 - Development libraries
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

This is the libraries, include files and other resources you can use
to develop SDL applications.


%prep
%setup -q -n %{name}-%{version}/%{name}
%patch0 -p1
%patch1 -p1

%build
%configure CFLAGS='-std=c99' --disable-video-x11 --enable-video-wayland --enable-pulseaudio
make %{?_smp_mflags}

%install
%make_install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_bindir}/*-config
%{_libdir}/lib*.so
%{_libdir}/cmake/SDL2/*.cmake
%{_includedir}/*/*.h
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*
