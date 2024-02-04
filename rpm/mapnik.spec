Summary: Mapnik is an open source toolkit for developing mapping applications
Name: mapnik
Version: 3.1.0
Release: 1%{?dist}
License: LGPL
Group: Libraries/Geosciences
URL: mapnik.org

Source: %{name}-%{version}.tar.gz
Patch0:     mapnik.issue3384.patch
Patch1:     mapnik.twkb.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++ pkgconfig(harfbuzz) pkgconfig(sqlite3)
BuildRequires: pkgconfig(icu-uc)
BuildRequires: boost-devel freetype-devel
BuildRequires: libxml2-devel libjpeg-turbo-devel libpng-devel libtiff-devel cairo-devel
BuildRequires: proj-devel
BuildRequires: python(abi) >= 2.7, python(abi) < 3.0
BuildRequires: boost-devel
Requires: proj

%description
Mapnik is basically a collection of geographic objects
like maps, layers, datasources, features, and geometries. The library
does not rely on any OS specific "windowing systems" and it can be
deployed to any server environment. It is intended to play fair in a
multi-threaded environment and is aimed primarily, but not
exclusively, at web-based development.

Custom:
  Repo: https://github.com/mapnik/mapnik
Categories:
  - Library
  - Maps

%package devel
Summary: Mapnik development headers
Group: Development/Libraries
Requires: %{name} = %{version}
Requires: pkgconfig(icu-uc)
Requires: pkgconfig(harfbuzz) pkgconfig(sqlite3)
Requires: boost-devel pkgconfig(freetype2)
Requires: pkgconfig(libxml-2.0) pkgconfig(libjpeg) pkgconfig(libpng) pkgconfig(libtiff-4)
Requires: cairo-devel
Requires: proj-devel

%description devel
This package provides headers for development

Custom:
  Repo: https://github.com/mapnik/mapnik
Categories:
  - Library
  - Maps

%package tools
Summary: Mapnik tools
Group: Libraries/Geosciences
Requires: %{name} = %{version}

%description tools
The package provides command line tools to test basic operations of mapnik

Type: console-application
Custom:
  Repo: https://github.com/mapnik/mapnik
Categories:
  - Utility
  - Maps

%prep
%setup -q -n %{name}-%{version}/mapnik
%patch0 -p1
%patch1 -p1

%build
%{__make} clean || true
%{__make} reset

%configure INPUT_PLUGINS="sqlite,shape" \
           DESTDIR=%{buildroot} \
           PREFIX=%{_prefix} \
           LIBDIR_SCHEMA=%{_lib} \
           CUSTOM_CXXFLAGS="$CXXFLAGS -fPIC -g0" \
           CUSTOM_CFLAGS="$CFLAGS -fPIC -g0" \
           CUSTOM_LDFLAGS="$LDFLAGS" \
           LINKING=shared \
           OPTIMIZATION=2 \
           CPP_TESTS=no \
           CAIRO=no \
           PLUGIN_LINKING=shared \
           MEMORY_MAPPED_FILE=no \
           DEMO=no \ MAPNIK_INDEX=no \
           MAPNIK_RENDER=no \
           CUSTOM_DEFINES="-DBOOST_PHOENIX_STL_TUPLE_H_"
           # ^ Workaround
           # https://github.com/mapnik/mapnik/issues/4375#issuecomment-1386786829
           #ENABLE_STATS=True ENABLE_LOG=True


%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
cp -r deps/mapbox/variant/include/mapbox %{buildroot}/usr/include

%clean
%{__rm} -rf %{buildroot}

%pre

%post -n mapnik -p /sbin/ldconfig

%postun -n mapnik -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%{_libdir}/libmapnik.so*
%{_libdir}/mapnik/fonts
%{_libdir}/mapnik/input

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/mapnik-config
%{_includedir}/mapnik
%{_includedir}/mapbox
%{_libdir}/libmapnik-json.a
%{_libdir}/libmapnik-wkt.a

%files tools
%defattr(-, root, root, 0755)
%{_bindir}/shapeindex
%{_bindir}/mapnik-index

%changelog
* Mon Apr 3 2017 rinigus <rinigus.git@gmail.com> - 3.0.13-1
- initial packaging release for SFOS
