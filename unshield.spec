%define major 0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	A program to extract InstallShield cabinet files
Name:		unshield
Version:	1.5.1
Release:	1
License:	MIT
Group:		Networking/Other
URL:		http://synce.sourceforge.net/
Source0:	https://github.com/twogood/unshield/archive/%{version}.tar.gz
BuildRequires:	zlib-devel
BuildRequires:	cmake
BuildRequires:	pkgconfig(openssl)

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
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files
%doc ChangeLog LICENSE
%{_bindir}/unshield
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc ChangeLog LICENSE
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
