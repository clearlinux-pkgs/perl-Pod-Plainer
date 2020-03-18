#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Pod-Plainer
Version  : 1.04
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/R/RM/RMBARKER/Pod-Plainer-1.04.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RM/RMBARKER/Pod-Plainer-1.04.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpod-plainer-perl/libpod-plainer-perl_1.04-1.debian.tar.xz
Summary  : 'Perl extension for converting Pod to old-style Pod.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Pod-Plainer-license = %{version}-%{release}
Requires: perl-Pod-Plainer-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Pod-Plainer version 1.04
========================
This was a core module in the Perl distribution to aid adoption
of extended POD featues.  It is no longer needed in the Perl
distribution and is being migrated to CPAN.

%package dev
Summary: dev components for the perl-Pod-Plainer package.
Group: Development
Provides: perl-Pod-Plainer-devel = %{version}-%{release}
Requires: perl-Pod-Plainer = %{version}-%{release}

%description dev
dev components for the perl-Pod-Plainer package.


%package license
Summary: license components for the perl-Pod-Plainer package.
Group: Default

%description license
license components for the perl-Pod-Plainer package.


%package perl
Summary: perl components for the perl-Pod-Plainer package.
Group: Default
Requires: perl-Pod-Plainer = %{version}-%{release}

%description perl
perl components for the perl-Pod-Plainer package.


%prep
%setup -q -n Pod-Plainer-1.04
cd %{_builddir}
tar xf %{_sourcedir}/libpod-plainer-perl_1.04-1.debian.tar.xz
cd %{_builddir}/Pod-Plainer-1.04
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Pod-Plainer-1.04/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Pod-Plainer
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Pod-Plainer/af5d38e2865f764a3552963ff75354104cb4cda8
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Pod::Plainer.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Pod-Plainer/af5d38e2865f764a3552963ff75354104cb4cda8

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/Pod/Plainer.pm
