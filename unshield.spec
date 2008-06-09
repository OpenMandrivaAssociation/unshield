%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	A program to extract InstallShield cabinet files
Name:		unshield
Version:	0.5
Release:	%mkrel 3
License:	MIT
Group:		Networking/Other
URL:		http://synce.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		unshield-antibork.diff
BuildRequires:	zlib-devel
BuildRequires:	libtool
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

%package -n	%{develname}
Summary:	Development library and header files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	zlib-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname %{name} 0 -d}

%description -n	%{develname}
Cabinet (.CAB) files are a form of archive, which is used by
the InstallShield installer software. The unshield program
simply unpacks such files.

See http://synce.sourceforge.net/ for more information.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p1

%build
#sh bootstrap
libtoolize --copy --force --automake; aclocal -I m4; autoheader; automake --copy --foreign --add-missing; autoconf

export CFLAGS="%{optflags} -fPIC"

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

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

%files -n %{develname}
%defattr(-,root,root)
%doc TODO LICENSE
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_datadir}/aclocal/unshield.m4
