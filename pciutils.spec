Name:           pciutils
Version:        3.3.1
Release:        14
License:        GPL-2.0+
Summary:        PCI utilities
Url:            http://atrey.karlin.mff.cuni.cz/~mj/pciutils.shtml
Group:          console/utils
Source0:        https://www.kernel.org/pub/software/utils/pciutils/pciutils-3.3.1.tar.xz
BuildRequires:  pkgconfig(libkmod)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  systemd
BuildRequires:  systemd-dev

%description
PCI utilities.

%package data
Summary:        PCI utilities
Group:          console/utils

%description data
PCI utilities.

%package lib
Summary:        PCI utilities
Group:          console/utils

%description lib
PCI utilities.

%package dev
Summary:        PCI utilities
Group:          console/utils
Requires:       pciutils-lib

%description dev
PCI utilities.

%package doc
Summary:        PCI utilities
Group:          doc

%description doc
PCI utilities.

%prep
%setup -q

%build
make %{?_smp_mflags} \
	OPT="%{optflags} -Wall" \
	INCDIR=%{_includedir} \
	PREFIX=%{_prefix} \
	LIBDIR=/usr/lib \
	SBINDIR=%{_sbindir} \
	STRIP="" \
	SHARED=yes \
	IDSDIR=%{_datadir}/hwdata

%install
make PREFIX=%{buildroot}/%{_prefix} \
	INCDIR=%{buildroot}/%{_includedir} \
	SBINDIR=%{buildroot}/%{_sbindir} \
	ROOT=%{buildroot}/ \
	MANDIR=%{buildroot}/%{_mandir} \
	STRIP="" \
	SHARED=yes \
	LIBDIR=%{buildroot}%{_libdir} \
	IDSDIR=%{buildroot}/%{_datadir}/hwdata \
	install install-lib

install -d %{buildroot}/%{_bindir}

chmod 755 %{buildroot}%{_libdir}/libpci.so.3.*

%files
%{_sbindir}/setpci
%{_sbindir}/update-pciids
%{_bindir}/lspci

%files data
%exclude %{_datadir}/hwdata/pci.ids.gz

%files lib
%{_libdir}/libpci.so.*

%files dev
%{_includedir}/pci/config.h
%{_includedir}/pci/header.h
%{_includedir}/pci/pci.h
%{_includedir}/pci/types.h
%{_libdir}/libpci.so
%{_libdir}/pkgconfig/libpci.pc

%files doc
%{_mandir}/man8/lspci.8
%{_mandir}/man8/update-pciids.8
%{_mandir}/man8/setpci.8
%{_mandir}/man7/pcilib.7

