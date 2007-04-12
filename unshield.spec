%define name	unshield
%define version 0.5
%define release %mkrel 2

%define	major	0
%define libname	%mklibname %{name} %{major}

Summary:	A program to extract InstallShield cabinet files
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	MIT
Group:		Networking/Other
URL:		http://synce.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-root

%description
Cabinet (.CAB) files are a form of archive, which is used by
the InstallShield installer software. The unshield program
simply unpacks such files.

See http://synce.sourceforge.net/ for more information.

%package -n	%{libname}
Summary:	A library to extract InstallShield cabinet files
Group:          System/Libraries

%description -n	%{libname}
Cabinet (.CAB) files are a form of archive, which is used by
the InstallShield installer software. The unshield program
simply unpacks such files.

See http://synce.sourceforge.net/ for more information.

%package -n	%{libname}-devel
Summary:	Development library and header files for %{name}
Group:		Development/C
Obsoletes:	%{name}-devel
Provides:	%{name}-devel
Provides:	lib%{name}-devel
Requires:	zlib-devel
Requires:	%{libname} = %{version}-%{release}

%description -n	%{libname}-devel
Cabinet (.CAB) files are a form of archive, which is used by
the InstallShield installer software. The unshield program
simply unpacks such files.

See http://synce.sourceforge.net/ for more information.

%prep

%setup -q -n %{name}-%{version}

%build
sh bootstrap
export CFLAGS="%{optflags} -fPIC"

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE
%{_bindir}/unshield

%files -n %{libname}
%defattr(-,root,root)
%doc README LICENSE
%{_libdir}/*.so.*
#%{_mandir}/man3/*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc TODO LICENSE
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_datadir}/aclocal/unshield.m4



