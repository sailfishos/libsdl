Summary: Simple DirectMedia Layer 2
Name: SDL2
Version: 2.0.18
Release: 1
Source: %{name}-%{version}.tar.gz
URL: http://www.libsdl.org/
License: zlib
BuildRequires: cmake
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

Patch0: 0001-wayland-Bring-back-wl_shell-support.patch

%description
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

%package devel
Summary: Simple DirectMedia Layer 2 - Development libraries
Requires: %{name} = %{version}

%description devel
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

This is the libraries, include files and other resources you can use
to develop SDL applications.


%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
mkdir -p build
pushd build
%cmake .. \
  -DLIB_SUFFIX="" \
  -DPULSEAUDIO=ON \
  -DVIDEO_WAYLAND=ON \
  -DVIDEO_X11=OFF \
  -DWAYLAND_LIBDECOR=OFF
popd

%install
pushd build
%make_install
popd

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%license LICENSE.txt
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_bindir}/*-config
%{_libdir}/lib*.so
%{_libdir}/cmake/SDL2/*.cmake
%{_includedir}/*/*.h
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*
