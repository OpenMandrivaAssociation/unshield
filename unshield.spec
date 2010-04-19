%define major 0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	A program to extract InstallShield cabinet files
Name:		unshield
Version:	0.6
Release:	%mkrel 2
License:	MIT
Group:		Networking/Other
URL:		http://synce.sourceforge.net/
Source0:	http://downloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
BuildRequires:	zlib-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
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
Obsoletes:	%{mklibname %{name} 0 -d}

%description -n	%{develname}
Cabinet (.CAB) files are a form of archive, which is used by
the InstallShield installer software. The unshield program
simply unpacks such files.

See http://synce.sourceforge.net/ for more information.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x --with-ssl
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

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
%doc ChangeLog LICENSE README TODO
%{_bindir}/unshield
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc ChangeLog LICENSE README TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
