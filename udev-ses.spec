Summary: Disk Links by slot in an SES enclosure.
Name: udev-ses
Version: 0.1
Release: 1%{?dist}
License: None
Group: System Environment/Base
URL: http://www.pnl.gov
Source: %{name}-%{version}.tgz
Requires: udev
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

%post
%preun
%clean
%files
%defattr(-, root, root, 0755)
/lib/udev/get_slot
/lib/udev/rules.d/65-ses-slot.rules


%changelog
* Fri Nov 03 2014 Evan Felix <e@pnl.gov> - 0.1
- First release 
