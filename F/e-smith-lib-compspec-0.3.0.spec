Summary: bash completion specifications for e-smith-lib utilities
%define name e-smith-lib-compspec
Name: %{name}
%define version 0.3.0
%define release 02sme02
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-lib-compspec-0.3.0-02.mitel_patch
Patch1: e-smith-lib-compspec-0.3.0-quotecur.patch
Patch2: e-smith-lib-compspec-0.3.0-dbmoved.patch
#Patch0: %{name}-%{version}.patch.2001041200
Packager: Tony Clayton <tonyc@e-smith.com>
BuildRoot: /var/tmp/e-smith-buildroot
BuildArchitectures: noarch
Requires: e-smith-lib
BuildRequires: e-smith-devtools 
AutoReqProv: no

%description
e-smith module containing bash completion specifications for the
e-smith-lib command-line utilities (db, config, expand-template, signal-event).

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build


%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT |
grep -v test.pl > %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%changelog
* Sat Jul 16 2004 Shad L. Lords <slords@lordsfam.net>
- [0.3.0-02sme02]
- Move dbs to /home/e-smith/db

* Sat Jul 16 2004 Shad L. Lords <slords@lordsfam.net>
- [0.3.0-02sme01]
- Fix quoting around $cur entries

* Tue Feb 24 2004 Tony Clayton <apc@e-smith.com>
- [0.3.0-02]
- Streamline completion algorithms for faster execution

* Tue Feb 24 2004 Tony Clayton <apc@e-smith.com>
- [0.3.0-01]
- Changing version to development stream number - 0.3.0

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [0.2.0-01]
- Changing version to stable stream number - 0.2.0

* Wed Jul 24 2002 Tony Clayton <apc@e-smith.com>
- [0.1.2-01]
- Imported into CVS, fixed description [tonyc 3819]

* Tue Jun 04 2002 Tony Clayton <tonyc@e-smith.com>
- [0.1.1-01]
- remove %post and %postun sections 

* Tue May 07 2002 Tony Clayton <tonyc@e-smith.com>
- [0.1.0-01]
- initial release.
