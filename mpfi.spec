%define name		mpfi
%define version		1.3.4
%define release		%mkrel 3
%define major		1
%define devname		%mklibname %{name} -d

Name:		%{name}
Group:		Sciences/Mathematics
License:	LGPL
Summary:	Interval arithmetic multi-precision based on GMP and MPFR
Version:	%{version}
Release:	%{release}
Source:		http://gforge.inria.fr/frs/download.php/468/%{name}-%{version}-RC3.tar.gz
URL:		http://gforge.inria.fr/projects/mpfi/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	gmp-devel
BuildRequires:	mpfr-devel

%description
MPFI is a C library for interval arithmetic multi-precision based on
the GMP and MPFR libraries.

%package	-n %{devname}
Summary:	lib%{name} libraries, includes, etc
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}

%description	-n %{devname}
lib%{name} libraries, includes, etc. MPFI is a C library for interval
arithmetic multi-precision based on the GMP and MPFR libraries.

%prep
%setup -q -n %{name}-%{version}-RC3

%build
%configure

%make CFLAGS="%{optflags} -fPIC"

%install
%makeinstall_std

%clean
rm -rf %{buildroot}

%files		-n %{devname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*
%{_infodir}/*
