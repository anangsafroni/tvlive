%define name tvlive.ign
<<<<<<< HEAD
%define release 2
%define version 2.0
%define license MIT
%define url http://anangsafroni.web.id
=======
%define release 1
%define version 1.0
%define license MIT
%define url http://ignsdk.web.id
>>>>>>> 364cb8698168c36eb6d057c90a450b7f232ab040
%define group System Environment/Base

Summary:IGOS Nusantara SDK Application
Name:%{name}
Version:%{version}
Release:%{release}
License:%{license}
Group:%{group}
URL:%{url}
Source0:%{name}.tar.gz
BuildRoot:%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:ignsdk
BuildArch:noarch
%description
%{description}
IGOS Nusantara SDK Application

%prep
%setup -q -n %{name}

%install
install -d -m 755 $RPM_BUILD_ROOT/opt/ignsdk/%{name}
install -d -m 755 $RPM_BUILD_ROOT/opt/ignsdk/%{name}/icons
<<<<<<< HEAD
install -d -m 755 $RPM_BUILD_ROOT/opt/ignsdk/%{name}/ch
=======
>>>>>>> 364cb8698168c36eb6d057c90a450b7f232ab040
install -d -m 755 $RPM_BUILD_ROOT/opt/ignsdk/%{name}/bin
install -d -m 755 $RPM_BUILD_ROOT/usr/share/applications
cp -rf ignsdk.json $RPM_BUILD_ROOT/opt/ignsdk/%{name}
cp -rf index.html $RPM_BUILD_ROOT/opt/ignsdk/%{name}
cp -rf bin $RPM_BUILD_ROOT/opt/ignsdk/%{name}
cp -rf icons/* $RPM_BUILD_ROOT/opt/ignsdk/%{name}/icons
cp -rf menu/* $RPM_BUILD_ROOT/usr/share/applications
<<<<<<< HEAD
cp -rf ch/* $RPM_BUILD_ROOT/opt/ignsdk/%{name}/ch
=======
>>>>>>> 364cb8698168c36eb6d057c90a450b7f232ab040

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir
%config %attr(0755,root,root) 
/opt/ignsdk/*
/usr/share/applications/*

%changelog

* Mon Feb 18 2013 foo <foo@bar.org>
- First Build
