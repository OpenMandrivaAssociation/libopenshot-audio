%define major	6
%define libname	%mklibname openshot-audio %{major}
%define devname	%mklibname openshot-audio -d

Name:		libopenshot-audio
Version:	0.1.7
Release:	2
Summary:	OpenShot Audio Library
License:	GPLv3+
Group:		System/Libraries
Url:		http://www.openshot.org/
Source0:	https://github.com/OpenShot/libopenshot-audio/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xrandr)

%description
OpenShot Audio Library.

#----------------------------------------------------

%package -n	%{libname}
Summary:	OpenShot Audio Library
Group:		System/Libraries

%description -n	%{libname}
OpenShot Audio Library.
This package contains library files for %{name}.

#----------------------------------------------------

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	openshot-audio-devel = %{version}-%{release}

%description -n	%{devname}
The %{devname} package contains libraries and header files for
developing applications that use %{name}.

#----------------------------------------------------

%package tools
Summary:	Tools and test binaries for %{name}
Group:		System/Libraries

%description tools
This package provides tools and test binaries for %{name}.

#----------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files

%files -n %{libname}
%license AUTHORS COPYING
%{_libdir}/libopenshot-audio.so.%{major}
%{_libdir}/libopenshot-audio.so.%{version}

%files -n %{devname}
%{_includedir}/%{name}/
%{_libdir}/libopenshot-audio.so

%files tools
%{_bindir}/openshot-audio-test-sound
%{_mandir}/man1/openshot-audio-test-sound.1*
