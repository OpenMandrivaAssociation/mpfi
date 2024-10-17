%define version			1.5.1
%define release			2
%define major			0
%define old_libmpfi		%mklibname mpfi 0
%define old_libmpfi_devel	%mklibname mpfi} -d
%define libmpfi_static_devel	%mklibname mpfi -d -s

Name:           mpfi
Version:        1.5.1
Release:        1%{?dist}
Summary:        An interval arithmetic library based on MPFR
License:        LGPLv2+
URL:            https://perso.ens-lyon.fr/nathalie.revol/software.html
Source0:        http://gforge.inria.fr/frs/download.php/30129/%{name}-%{version}.tar.bz2
Source1:        %{name}.rpmlintrc
BuildRequires:  mpfr-devel
BuildRequires:  gmp-devel
%rename %{old_libmpfi}

%description
MPFI is intended to be a portable library written in C for arbitrary
precision interval arithmetic with intervals represented using MPFR
reliable floating-point numbers. It is based on the GNU MP library and
on the MPFR library and is part of the latter. The purpose of an
arbitrary precision interval arithmetic is on the one hand to get
"guaranteed" results, thanks to interval computation, and on the other
hand to obtain accurate results, thanks to multiple precision
arithmetic. The MPFI library is built upon MPFR in order to benefit
from the correct roundings provided by MPFR. Further advantages of
using MPFR are its portability and compliance with the IEEE 754
standard for floating-point arithmetic.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}, mpfr-devel%{?_isa}
%rename %{old_libmpfi_devel}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

# Remove libtool archives
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# Remove dir file in the info directory
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%check
make check

%files
%doc AUTHORS NEWS TODO
%{_libdir}/*.so.*

%files devel
%{_includedir}/mpfi.h
%{_includedir}/mpfi_io.h
%{_infodir}/%{name}.info*
%{_libdir}/libmpfi.so
