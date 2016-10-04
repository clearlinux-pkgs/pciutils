Name:           pciutils
Version:        3.5.2
Release:        18
License:        GPL-2.0+
Summary:        PCI utilities
Url:            http://atrey.karlin.mff.cuni.cz/~mj/pciutils.shtml
Group:          console/utils
Source0:        https://www.kernel.org/pub/software/utils/pciutils/pciutils-3.5.2.tar.xz
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
	INCDIR=/usr/include \
	PREFIX=%{_prefix} \
	LIBDIR=/usr/lib \
	SBINDIR=/usr/sbin \
	STRIP="" \
	SHARED=yes \
	IDSDIR=/usr/share/hwdata

%install
make PREFIX=%{buildroot}/%{_prefix} \
	INCDIR=%{buildroot}/usr/include \
	SBINDIR=%{buildroot}/usr/bin \
	BINDIR=%{buildroot}/usr/bin \
	ROOT=%{buildroot}/ \
	MANDIR=%{buildroot}//usr/share/man \
	STRIP="" \
	SHARED=yes \
	LIBDIR=%{buildroot}/usr/lib64 \
	IDSDIR=%{buildroot}//usr/share/hwdata \
	install install-lib

install -d %{buildroot}//usr/bin

chmod 755 %{buildroot}/usr/lib64/libpci.so.3.*

%files
/usr/bin/setpci
/usr/bin/update-pciids
/usr/bin/lspci

%files data
%exclude /usr/share/hwdata/pci.ids.gz

%files lib
/usr/lib64/libpci.so.*

%files dev
/usr/include/pci/config.h
/usr/include/pci/header.h
/usr/include/pci/pci.h
/usr/include/pci/types.h
/usr/lib64/libpci.so
/usr/lib64/pkgconfig/libpci.pc

%files doc
/usr/share/man/man8/lspci.8
/usr/share/man/man8/update-pciids.8
/usr/share/man/man8/setpci.8
/usr/share/man/man7/pcilib.7

