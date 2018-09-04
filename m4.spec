#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xA7A16B4A2527436A (eblake@redhat.com)
#
Name     : m4
Version  : 1.4.18
Release  : 73
URL      : http://mirrors.kernel.org/gnu/m4/m4-1.4.18.tar.xz
Source0  : http://mirrors.kernel.org/gnu/m4/m4-1.4.18.tar.xz
Source99 : http://mirrors.kernel.org/gnu/m4/m4-1.4.18.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : FSFULLR GPL-3.0 GPL-3.0+
Requires: m4-bin
Requires: m4-license
Requires: m4-man
BuildRequires : glibc-locale
Patch1: 0001-disable-update-copyright-if-perl-is-too-new.patch
Patch2: 0002-Fix-build-with-glibc-2.18.patch

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
Requires: m4-license
Requires: m4-man

%description bin
bin components for the m4 package.


%package doc
Summary: doc components for the m4 package.
Group: Documentation
Requires: m4-man

%description doc
doc components for the m4 package.


%package license
Summary: license components for the m4 package.
Group: Default

%description license
license components for the m4 package.


%package man
Summary: man components for the m4 package.
Group: Default

%description man
man components for the m4 package.


%prep
%setup -q -n m4-1.4.18
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534206225
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1534206225
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/m4
cp COPYING %{buildroot}/usr/share/doc/m4/COPYING
cp examples/COPYING %{buildroot}/usr/share/doc/m4/examples_COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/m4

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/info/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/m4/COPYING
/usr/share/doc/m4/examples_COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/m4.1
