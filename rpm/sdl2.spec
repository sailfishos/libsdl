%undefine __cmake_in_source_build

# cmake of SDL requires static libs to exist
%define keepstatic 1

Summary: Simple DirectMedia Layer 2
Name: SDL2
Version: 2.30.0
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
Patch1: 0002-Revert-Fixed-a-memory-leak-at-window-creation.patch

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
%cmake \
  -DLIB_SUFFIX="" \
  -DPULSEAUDIO=ON \
  -DSDL_RPATH=OFF \
  -DSDL_STATIC=ON \
  -DVIDEO_WAYLAND=ON \
  -DVIDEO_X11=OFF \
  -DWAYLAND_LIBDECOR=OFF
%cmake_build

%install
%cmake_install
rm -f %{buildroot}%{_datadir}/licenses/%{name}/LICENSE.txt

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license LICENSE.txt
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_bindir}/*-config
%{_libdir}/lib*.a
%{_libdir}/lib*.so
%{_libdir}/cmake/%{name}/*.cmake
%{_includedir}/*/*.h
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*
