Summary: nethserver-bareos  is a module to install bareos
%define name nethserver-bareos
Name: %{name}
%define version 0.0.5
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: bareos bareos-webui bareos-database-postgresql 
Requires: nethserver-postgresql
Requires: nethserver-rh-php73-php-fpm

BuildRequires: nethserver-devtools
BuildArch: noarch

%description
Bareos (Backup Archiving Recovery Open Sourced) is a reliable, cross-network 
open source software for backup, archiving and recovery of data for all 
well-established operating systems.

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/
cp -a manifest.json %{buildroot}/usr/share/cockpit/%{name}/
cp -a logo.png %{buildroot}/usr/share/cockpit/%{name}/
cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/


rm -f %{name}-%{version}-%{release}-filelist
%{genfilelist} $RPM_BUILD_ROOT \
> %{name}-%{version}-%{release}-filelist

%post
%postun

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING

%changelog
* Fri Apr 10 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.5
- Members of bareos group are web-ui admin

* Tue Apr 07 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.4
- Use Pam to authenticate the admin user

* Sun Apr 05 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.3
- The console/admin.conf is not more a template (noreplace)
- switch to rh-php73

* Sat Apr 04 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.1
- initial