#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xA7A16B4A2527436A (eblake@redhat.com)
#
Name     : m4
Version  : 1.4.19
Release  : 109
URL      : https://mirrors.kernel.org/gnu/m4/m4-1.4.19.tar.xz
Source0  : https://mirrors.kernel.org/gnu/m4/m4-1.4.19.tar.xz
Source1  : https://mirrors.kernel.org/gnu/m4/m4-1.4.19.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : FSFULLR GPL-3.0 GPL-3.0+
Requires: m4-bin = %{version}-%{release}
Requires: m4-info = %{version}-%{release}
Requires: m4-license = %{version}-%{release}
Requires: m4-locales = %{version}-%{release}
Requires: m4-man = %{version}-%{release}
BuildRequires : glibc-locale
Patch1: 0001-disable-update-copyright-if-perl-is-too-new.patch

%description
GNU `m4' is an implementation of the traditional Unix macro
processor.  It is mostly SVR4 compatible, although it has some
extensions (for example, handling more than 9 positional parameters
to macros).  `m4' also has built-in functions for including files,
running shell commands, doing arithmetic, etc.  Autoconf needs GNU
`m4' for generating `configure' scripts, but not for running them.

%package bin
Summary: bin components for the m4 package.
Group: Binaries
Requires: m4-license = %{version}-%{release}

%description bin
bin components for the m4 package.


%package info
Summary: info components for the m4 package.
Group: Default

%description info
info components for the m4 package.


%package license
Summary: license components for the m4 package.
Group: Default

%description license
license components for the m4 package.


%package locales
Summary: locales components for the m4 package.
Group: Default

%description locales
locales components for the m4 package.


%package man
Summary: man components for the m4 package.
Group: Default

%description man
man components for the m4 package.


%prep
%setup -q -n m4-1.4.19
cd %{_builddir}/m4-1.4.19
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633198938
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1633198938
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/m4
cp %{_builddir}/m4-1.4.19/COPYING %{buildroot}/usr/share/package-licenses/m4/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/m4-1.4.19/examples/COPYING %{buildroot}/usr/share/package-licenses/m4/72e66772b1e088d9b230123a261cae1e86dcecc4
%make_install
%find_lang m4

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/m4

%files info
%defattr(0644,root,root,0755)
/usr/share/info/m4.info
/usr/share/info/m4.info-1
/usr/share/info/m4.info-2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/m4/31a3d460bb3c7d98845187c716a30db81c44b615
/usr/share/package-licenses/m4/72e66772b1e088d9b230123a261cae1e86dcecc4

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/m4.1

%files locales -f m4.lang
%defattr(-,root,root,-)

