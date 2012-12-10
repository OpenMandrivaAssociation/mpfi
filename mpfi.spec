%define name			mpfi
%define version			1.5
%define release			%mkrel 2
%define major			0
%define libmpfi			%mklibname %{name} %{major}
%define libmpfi_devel		%mklibname %{name} -d
%define libmpfi_static_devel	%mklibname %{name} -d -s

Name:		%{name}
Group:		Sciences/Mathematics
License:	LGPL
Summary:	Interval arithmetic multi-precision based on GMP and MPFR
Version:	%{version}
Release:	%{release}
Source:		http://gforge.inria.fr/frs/download.php/22256/%{name}-%{version}.tar.bz2
URL:		http://gforge.inria.fr/projects/mpfi/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	gmp-devel
BuildRequires:	mpfr-devel

%description
MPFI is a C library for interval arithmetic multi-precision based on
the GMP and MPFR libraries.

%package	-n %{libmpfi}
Summary:	lib%{name} dynamic library
Group:		System/Libraries
Provides:	lib%{name} = %{version}-%{release}

%description	-n %{libmpfi}
lib%{name} dynamic library. MPFI is a C library for interval
arithmetic multi-precision based on the GMP and MPFR libraries.

%package	-n %{libmpfi_devel}
Summary:	lib%{name} libraries, includes, etc
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libmpfi} = %{version}-%{release}

%description	-n %{libmpfi_devel}
lib%{name} libraries, includes, etc. MPFI is a C library for interval
arithmetic multi-precision based on the GMP and MPFR libraries.

%package	-n %{libmpfi_static_devel}
Summary:	lib%{name} static libraries
Group:		Development/C
Provides:	%{name}-static-devel = %{version}-%{release}

%description	-n %{libmpfi_static_devel}
lib%{name} static libraries. MPFI is a C library for interval
arithmetic multi-precision based on the GMP and MPFR libraries.

%prep
%setup -q -n %{name}-%{version}

%build
export CFLAGS="%{optflags} -fPIC"
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std
rm %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%files		-n %{libmpfi}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files		-n %{libmpfi_devel}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_infodir}/*

%files		-n %{libmpfi_static_devel}
%defattr(-,root,root)
%{_libdir}/*.a


%changelog
* Wed Dec 07 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.5-2mdv2012.0
+ Revision: 738701
- Rebuild for .la file removal.

* Mon Jan 31 2011 Funda Wang <fwang@mandriva.org> 1.5-1
+ Revision: 634340
- new version 1.5

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Wed Sep 09 2009 Paulo Andrade <pcpa@mandriva.com.br> 1.4-4mdv2010.0
+ Revision: 436127
+ rebuild (emptylog)

* Wed Sep 09 2009 Paulo Andrade <pcpa@mandriva.com.br> 1.4-3mdv2010.0
+ Revision: 435719
- Split package in dynamic, devel and static libraries

* Mon Aug 31 2009 Paulo Andrade <pcpa@mandriva.com.br> 1.4-2mdv2010.0
+ Revision: 423025
+ rebuild (emptylog)

* Tue Aug 25 2009 Paulo Andrade <pcpa@mandriva.com.br> 1.4-1mdv2010.0
+ Revision: 420682
- update to latest upstream release version 1.4.

* Wed May 20 2009 Paulo Andrade <pcpa@mandriva.com.br> 1.3.4-3mdv2010.0
+ Revision: 377882
+ rebuild (emptylog)

* Fri May 08 2009 Paulo Andrade <pcpa@mandriva.com.br> 1.3.4-2mdv2010.0
+ Revision: 373561
+ rebuild (emptylog)

* Thu Mar 26 2009 Paulo Andrade <pcpa@mandriva.com.br> 1.3.4-1mdv2009.1
+ Revision: 361479
- Initial import of mpfi, version 1.3.4, rc3.
  MPFI is a C library for interval arithmetic multi-precision based on
  the GMP and MPFR libraries.
  http://gforge.inria.fr/projects/mpfi/
- mpfi

