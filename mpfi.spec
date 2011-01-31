%define name			mpfi
%define version			1.5
%define release			%mkrel 1
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

%clean
rm -rf %{buildroot}

%files		-n %{libmpfi}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files		-n %{libmpfi_devel}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_infodir}/*

%files		-n %{libmpfi_static_devel}
%defattr(-,root,root)
%{_libdir}/*.a
