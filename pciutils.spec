#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v13
# autospec commit: 2659038
#
Name     : pciutils
Version  : 3.13.0
Release  : 48
URL      : https://mirrors.kernel.org/pub/software/utils/pciutils/pciutils-3.13.0.tar.gz
Source0  : https://mirrors.kernel.org/pub/software/utils/pciutils/pciutils-3.13.0.tar.gz
Summary  : The PCI Utilities
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: pciutils-bin = %{version}-%{release}
Requires: pciutils-data = %{version}-%{release}
Requires: pciutils-lib = %{version}-%{release}
Requires: pciutils-license = %{version}-%{release}
Requires: pciutils-man = %{version}-%{release}
BuildRequires : pkgconfig(libkmod)
BuildRequires : pkgconfig(zlib)
BuildRequires : systemd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Makefile-build-fixes.patch

%description
This package contains various utilities for inspecting and
setting of devices connected to the PCI bus.

%package bin
Summary: bin components for the pciutils package.
Group: Binaries
Requires: pciutils-data = %{version}-%{release}
Requires: pciutils-license = %{version}-%{release}

%description bin
bin components for the pciutils package.


%package data
Summary: data components for the pciutils package.
Group: Data

%description data
data components for the pciutils package.


%package dev
Summary: dev components for the pciutils package.
Group: Development
Requires: pciutils-lib = %{version}-%{release}
Requires: pciutils-bin = %{version}-%{release}
Requires: pciutils-data = %{version}-%{release}
Provides: pciutils-devel = %{version}-%{release}
Requires: pciutils = %{version}-%{release}

%description dev
dev components for the pciutils package.


%package lib
Summary: lib components for the pciutils package.
Group: Libraries
Requires: pciutils-data = %{version}-%{release}
Requires: pciutils-license = %{version}-%{release}

%description lib
lib components for the pciutils package.


%package license
Summary: license components for the pciutils package.
Group: Default

%description license
license components for the pciutils package.


%package man
Summary: man components for the pciutils package.
Group: Default

%description man
man components for the pciutils package.


%prep
%setup -q -n pciutils-3.13.0
cd %{_builddir}/pciutils-3.13.0
%patch -P 1 -p1
pushd ..
cp -a pciutils-3.13.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1720102241
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make  %{?_smp_mflags}

pushd ../buildavx2
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1720102241
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pciutils
cp %{_builddir}/pciutils-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pciutils/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
## install_append content
%make_install install-lib
chmod a+x %{buildroot}*/usr/lib64/*
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/lspci
/V3/usr/bin/pcilmr
/V3/usr/bin/setpci
/usr/bin/lspci
/usr/bin/pcilmr
/usr/bin/setpci
/usr/bin/update-pciids

%files data
%defattr(-,root,root,-)
/usr/share/pci.ids.gz

%files dev
%defattr(-,root,root,-)
/usr/include/pci/config.h
/usr/include/pci/header.h
/usr/include/pci/pci.h
/usr/include/pci/types.h
/usr/lib64/libpci.so
/usr/lib64/pkgconfig/libpci.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libpci.so.3.13.0
/usr/lib64/libpci.so.3
/usr/lib64/libpci.so.3.13.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pciutils/06877624ea5c77efe3b7e39b0f909eda6e25a4ec

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/pci.ids.5
/usr/share/man/man7/pcilib.7
/usr/share/man/man8/lspci.8
/usr/share/man/man8/pcilmr.8
/usr/share/man/man8/setpci.8
/usr/share/man/man8/update-pciids.8
