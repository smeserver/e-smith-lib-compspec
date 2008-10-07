# $Id: e-smith-lib-compspec.spec,v 1.2 2008/10/07 18:42:14 slords Exp $

Summary: bash completion specifications for e-smith-lib utilities
%define name e-smith-lib-compspec
Name: %{name}
%define version 2.0.0
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
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
* Tue Oct 7 2008 Shad L. Lords <slords@mail.com> 2.0.0-1.sme
- Roll new stream to separate sme7/sme8 trees [SME: 4633]

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Thu Mar 16 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.0-01
- Roll stable stream version. [SME: 1016]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 0.3.0-05
- Bump release number only

* Mon Jul 18 2005 Charlie Brady <charlieb@e-smith.com>
- [0.3.0-04]
- Be prepared for move of dbs to /home/e-smith/db [SF: 1216546]

* Fri Jul 15 2005 Tony Clayton <apc@e-smith.com>
- [0.3.0-03]
- Fix db/signal-event completion algorithms
- Optimize expand-template completion algorithm

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
