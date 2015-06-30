Summary: Disk Links by slot in an SES enclosure.
Name: udev-ses
Version: 0.2
Release: 2%{?dist}
License: None
Group: System Environment/Base
URL: http://www.pnl.gov
Source: %{name}-%{version}.tgz
Requires: udev sg3_utils
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Basic setup to link SES slot numbers to files in /dev/disk/by-slot for
disks that are in a compatible enclosure.

%prep
%setup
%build
%install
%{__install} -d -m0775 %{buildroot}/lib/udev/rules.d/
cp 65-ses-slot.rules %{buildroot}/lib/udev/rules.d/ 
cp get_slot %{buildroot}/lib/udev/
cp get_slot2 %{buildroot}/lib/udev/
%{__install} -d -m0775 %{buildroot}/lib/modules-load.d/
cp udev-ses.conf %{buildroot}/lib/modules-load.d/

%post
/usr/sbin/modprobe sg
/usr/sbin/udevadm trigger 
%preun
%clean
%files
%defattr(-, root, root, 0755)
/lib/udev/get_slot
/lib/udev/get_slot2
/lib/udev/rules.d/65-ses-slot.rules
%attr(0644,root,root) /lib/modules-load.d/udev-ses.conf

%changelog
* Mon Jun 29 2015 Evan Felix <e@pnl.gov> - 0.2
- Add element descriptor indexing link as well.
* Fri Nov 03 2014 Evan Felix <e@pnl.gov> - 0.1
- First release 
