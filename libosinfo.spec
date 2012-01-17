# -*- rpm-spec -*-

Summary: A library for managing OS information for virtualization
Name: libosinfo
Version: 0.0.5
Release: 1%{?dist}%{?extra_release}
License: LGPLv2+
Group: Development/Libraries
Source: https://fedorahosted.org/releases/l/i/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL: https://fedorahosted.org/libosinfo/
BuildRequires: glib2-devel
BuildRequires: check-devel
BuildRequires: libxml2-devel >= 2.6.0
BuildRequires: vala
BuildRequires: vala-tools
BuildRequires: gobject-introspection-devel
Requires: udev

%description
libosinfo is a library that allows virtualization provisioning tools to
determine the optimal device settings for a hypervisor/operating system
combination.

%package devel
Summary: Libraries, includes, etc. to compile with the libosinfo library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: glib2-devel

%description devel
libosinfo is a library that allows virtualization provisioning tools to
determine the optimal device settings for a hypervisor/operating system
combination.

Libraries, includes, etc. to compile with the libosinfo library

%package vala
Summary: Vala bindings
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description vala
libosinfo is a library that allows virtualization provisioning tools to
determine the optimal device settings for a hypervisor/operating system
combination.

This package provides the Vala bindings for libosinfo library.

%prep
%setup -q

%build
%configure --enable-introspection=yes --enable-vala=yes --enable-udev=yes
%__make %{?_smp_mflags} V=1

chmod a-x examples/*.js examples/*.py

%install
rm -fr %{buildroot}
%__make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la

%check
make check

%clean
rm -fr %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING.LIB NEWS README
%{_bindir}/osinfo-pciids-convert
%{_bindir}/osinfo-usbids-convert
%{_bindir}/osinfo-detect
%dir %{_datadir}/libosinfo/
%dir %{_datadir}/libosinfo/data/
%{_datadir}/libosinfo/data/usb.ids
%{_datadir}/libosinfo/data/pci.ids
%{_datadir}/libosinfo/data/devices
%{_datadir}/libosinfo/data/oses
%{_datadir}/libosinfo/data/hypervisors
%{_libdir}/%{name}-1.0.so.*
/lib/udev/rules.d/95-osinfo.rules
%{_libdir}/girepository-1.0/Libosinfo-1.0.typelib

%files devel
%defattr(-, root, root)
%doc examples/demo.js
%doc examples/demo.py
%{_libdir}/%{name}-1.0.so
%dir %{_includedir}/%{name}-1.0/
%dir %{_includedir}/%{name}-1.0/osinfo/
%{_includedir}/%{name}-1.0/osinfo/*.h
%{_libdir}/pkgconfig/%{name}-1.0.pc
%{_datadir}/gir-1.0/Libosinfo-1.0.gir
%{_datadir}/gtk-doc/html/Libosinfo

%files vala
%defattr(-, root, root)
%{_datadir}/vala/vapi/libosinfo-1.0.vapi

%changelog
* Tue Jan  17 2012 Zeeshan Ali <zeenix@redhat.com> - 0.0.5-1
- Update to 0.0.5 release

* Tue Jan  3 2012 Daniel P. Berrange <berrange@redhat.com> - 0.0.4-2
- Remove pointless gir conditionals

* Wed Dec 21 2011 Daniel P. Berrange <berrange@redhat.com> - 0.0.4-1
- Update to 0.0.4 release

* Thu Nov 24 2011 Daniel P. Berrange <berrange@redhat.com> - 0.0.2-1
- Initial package

