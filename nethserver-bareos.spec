Summary: nethserver-bareos  is a module to install bareos
%define name nethserver-bareos
Name: %{name}
%define version 0.0.11
%define release 3
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: bareos bareos-webui bareos-database-postgresql 
Requires: nethserver-postgresql12
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
if [ $1 == 0 ] ; then
    /usr/bin/rm -f /etc/httpd/conf.d/zzz_bareos-webui.conf
    /usr/bin/rm -f /etc/httpd/conf.d/bareos-webui.conf
    /usr/bin/systemctl reload httpd
fi

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING
%attr(0755,root,root) /usr/lib/bareos/scripts/make_catalog_backup_nethserver.sh

%changelog
* Thu Aug 05 2021 stephane de Labrusse <stephdl@de-labrusse.fr> - 0.0.11
- Do not use the software-repo-save event
￼
* Thu Nov 19 2020  stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.10
- Remove the traillin / of linux fpm socket

* Sat Jul 04 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.9
- Remove http templates after rpm removal

* Fri May 01 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.8
- Move to rh-postgresql12

* Sat Apr 11 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.7
- Handle when account provider is not installed

* Fri Apr 10 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.6
- Members of bareos group are web-ui admin

* Tue Apr 07 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.4
- Use Pam to authenticate the admin user

* Sun Apr 05 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.3
- The console/admin.conf is not more a template (noreplace)
- switch to rh-php73

* Sat Apr 04 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.1
- initial
