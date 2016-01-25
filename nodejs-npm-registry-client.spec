%{?scl:%scl_package nodejs-npm-registry-client}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-npm-registry-client
Version:        7.0.8
Release:        1%{?dist}
Summary:        Client for the npm registry

Group:          System Environment/Libraries
License:        BSD
URL:            https://github.com/isaacs/npm-registry-client
Source0:        http://registry.npmjs.org/npm-registry-client/-/npm-registry-client-%{version}.tgz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  %{?scl_prefix}nodejs-devel

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif


%description
Client for the npm registry, or private servers using the npm registry software.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{nodejs_sitelib}/npm-registry-client
cp -pr package.json index.js lib %{buildroot}%{nodejs_sitelib}/npm-registry-client

%nodejs_symlink_deps

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/npm-registry-client
%doc README.md LICENSE

%changelog
* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 7.0.8-1
- New upstream release

* Fri Nov 27 2015 Tomas Hrcka <thrcka@redhat.com> - 4.0.3-1
- Rebase to latest upstream

* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 2.0.7-1
- New upstream release 2.0.7

* Wed Feb 19 2014 Tomas Hrcka <thrcka@redhat.com> - 0.3.3-1
- New upstream release 0.3.3

* Thu Jan 16 2014 Tomas Hrcka <thrcka@redhat.com> - 0.3.2-1
- New upstream release 0.3.2

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.2.28-2
- replace provides and requires with macro

* Fri Sep 06 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.28-1
- update to upstream release 0.2.28
- add ExclusiveArch logic

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.27-2
- fix semver dep

* Fri Jul 12 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.27-1
- new upstream release 0.2.27

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.25-1
- new upstream release 0.2.25

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.20-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.20-2
- add macro for EPEL6 dependency generation

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.2.20-2
- Add support for software collections

* Wed Apr 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.20-1
- new upstream release 0.2.20

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.18-2
- fix request dep

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.18-1
- new upstream release 0.2.18

* Wed Feb 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.15-1
- new upstream release 0.2.15
- graceful-fs dep good now

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.13-2
- fix graceful-fs dep for 1.2.0

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.13-1
- new upstream release 0.2.13

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.11-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.11-1
- initial package generated by npm2rpm
