Summary: Mapnik is an open source toolkit for developing mapping applications
Name: mapnik
Version: 3.0.15
Release: 1%{?dist}
License: LGPL
Group: Libraries/Geosciences
URL: mapnik.org

Source: https://github.com/mapnik/mapnik/releases/download/v3.0.13/mapnik-v3.0.13.tar.bz2
Patch0:     mapnik.issue3384.patch
Patch1:     mapnik.twkb.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++ libicu52-devel harfbuzz-devel sqlite-devel
BuildRequires: boost-devel freetype-devel
BuildRequires: libxml2-devel libjpeg-turbo-devel libpng-devel libtiff-devel cairo-devel
BuildRequires: proj-devel
Requires: proj

%description
Mapnik is basically a collection of geographic objects
like maps, layers, datasources, features, and geometries. The library
does not rely on any OS specific "windowing systems" and it can be
deployed to any server environment. It is intended to play fair in a
multi-threaded environment and is aimed primarily, but not
exclusively, at web-based development.


%package devel
Summary: Mapnik development headers
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This package provides headers for development


%package tools
Summary: Mapnik tools
Group: Libraries/Geosciences
Requires: %{name} = %{version}

%description tools
The package provides command line tools to test basic operations of mapnik

%prep
%setup -q -n %{name}-%{version}/mapnik
%patch0 -p1
%patch1 -p1

%build
%{__make} clean || true
%{__make} reset

%configure INPUT_PLUGINS="sqlite,shape" DESTDIR=%{buildroot} PREFIX="/usr" CUSTOM_CXXFLAGS="$CXXFLAGS -fPIC -g0" CUSTOM_CFLAGS="$CFLAGS -fPIC -g0" CUSTOM_LDFLAGS="$LDFLAGS" LINKING=shared OPTIMIZATION=2 CPP_TESTS=no CAIRO=no PLUGIN_LINKING=static MEMORY_MAPPED_FILE=no DEMO=no MAPNIK_INDEX=no MAPNIK_RENDER=no #ENABLE_STATS=True ENABLE_LOG=True 

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
#%{_libdir}/libmapnik.a

%files tools
%defattr(-, root, root, 0755)
%{_bindir}/shapeindex

%changelog
* Mon Apr 3 2017 rinigus <rinigus.git@gmail.com> - 3.0.13-1
- initial packaging release for SFOS
