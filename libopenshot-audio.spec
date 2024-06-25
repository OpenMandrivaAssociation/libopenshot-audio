%define major	9
%define libname	%mklibname openshot-audio %{major}
%define devname	%mklibname openshot-audio -d

Name:		libopenshot-audio
Version:	0.3.3
Release:	1
Summary:	OpenShot Audio Library
License:	GPLv3+
Group:		System/Libraries
Url:		http://www.openshot.org/
Source0:	https://github.com/OpenShot/libopenshot-audio/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake ninja
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
Obsoletes:	%{mklibname openshot-audio 6} < %{EVRD}

%description -n	%{libname}
OpenShot Audio Library.
This package contains library files for %{name}.

#----------------------------------------------------

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	openshot-audio-devel = %{EVRD}

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
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_docdir}/OpenShotAudio/

%files -n %{libname}
%license AUTHORS COPYING
%{_libdir}/libopenshot-audio.so.%{major}
%{_libdir}/libopenshot-audio.so.%{version}

%files -n %{devname}
%{_includedir}/%{name}/
%{_libdir}/libopenshot-audio.so
%{_libdir}/cmake/OpenShotAudio/FindASIO.cmake
%{_libdir}/cmake/OpenShotAudio/OpenShotAudioConfig*
%{_libdir}/cmake/OpenShotAudio/OpenShotAudioTargets*

%files tools
%{_bindir}/openshot-audio-demo
%{_mandir}/man1/openshot-audio-demo.1.*
