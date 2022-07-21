# -*- rpm-spec -*-

Summary: A library for managing OS information for virtualization
Name: libosinfo
Version: 1.10.0
Release: 3%{?dist}
License: LGPLv2+
Source: https://releases.pagure.io/%{name}/%{name}-%{version}.tar.xz
URL: https://libosinfo.org/

### Patches ###

BuildRequires: meson
BuildRequires: gcc
BuildRequires: gtk-doc
BuildRequires: gettext-devel
BuildRequires: glib2-devel
BuildRequires: libxml2-devel >= 2.6.0
BuildRequires: libxslt-devel >= 1.0.0
BuildRequires: libsoup3-devel
BuildRequires: vala
BuildRequires: /usr/bin/pod2man
BuildRequires: hwdata
BuildRequires: gobject-introspection-devel
BuildRequires: osinfo-db
BuildRequires: git
Requires: hwdata
Requires: osinfo-db
Requires: osinfo-db-tools

%description
libosinfo is a library that allows virtualization provisioning tools to
determine the optimal device settings for a hypervisor/operating system
combination.

%package devel
Summary: Libraries, includes, etc. to compile with the libosinfo library
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: glib2-devel
# -vala subpackage removed in F30
Obsoletes: libosinfo-vala < 1.3.0-3
Provides: libosinfo-vala = %{version}-%{release}

%description devel
libosinfo is a library that allows virtualization provisioning tools to
determine the optimal device settings for a hypervisor/operating system
combination.

Libraries, includes, etc. to compile with the libosinfo library

%prep
%autosetup -S git

%build
%meson \
    -Denable-gtk-doc=true \
    -Denable-tests=true \
    -Denable-introspection=enabled \
    -Denable-vala=enabled
%meson_build

%install
%meson_install

%find_lang %{name}

%check
%meson_test

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING.LIB NEWS README
%{_bindir}/osinfo-detect
%{_bindir}/osinfo-query
%{_bindir}/osinfo-install-script
%{_mandir}/man1/osinfo-detect.1*
%{_mandir}/man1/osinfo-query.1*
%{_mandir}/man1/osinfo-install-script.1*
%{_libdir}/%{name}-1.0.so.*
%{_libdir}/girepository-1.0/Libosinfo-1.0.typelib

%files devel
%{_libdir}/%{name}-1.0.so
%dir %{_includedir}/%{name}-1.0/
%dir %{_includedir}/%{name}-1.0/osinfo/
%{_includedir}/%{name}-1.0/osinfo/*.h
%{_libdir}/pkgconfig/%{name}-1.0.pc
%{_datadir}/gir-1.0/Libosinfo-1.0.gir
%{_datadir}/gtk-doc/html/Libosinfo

%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libosinfo-1.0.deps
%{_datadir}/vala/vapi/libosinfo-1.0.vapi

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Daniel P. Berrangé <berrange@redhat.com> - 1.10.0-2
- Switch from libsoup2 to libsoup3 (rhbz #2108589)

* Mon Feb 14 2022 Victor Toso <victortoso@redhat.com> - 1.10.0-1
- Update to 1.10.0 release

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Cole Robinson <crobinso@redhat.com> - 1.9.0-3
- Fix build with glib 2.70

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 Fabiano Fidêncio <fidencio@redhat.com> - 1.9.0-1
- Update to 1.9.0 release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Fabiano Fidêncio <fidencio@redhat.com> - 1.8.0-1
- Update to 1.8.0 release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Fabiano Fidêncio <fidencio@redhat.com> - 1.7.1-2
- Fix OsinfoList ABI breakage
