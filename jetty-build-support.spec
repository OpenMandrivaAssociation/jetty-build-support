%{?_javapackages_macros:%_javapackages_macros}
Name:           jetty-build-support
Version:        1.1
Release:        8.1
Summary:        Jetty build support files


# licensing bug upstream
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=362646
# - commit stating the license is already there
License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{name}-%{version}.tar.bz2
# rpmlint config file (fedpkg lint will use this)
#Source1:        .rpmlint
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-enforcer-api
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  jetty-toolchain
BuildRequires:  junit

Requires:       maven
Requires:       maven-project
Requires:       maven-enforcer
Requires:       jpackage-utils
Requires:       jetty-toolchain
Requires:       maven-enforcer-api
Requires:       plexus-containers-container-default

%description
Build Support for Jetty. Contains enforcer rules, PMD rulesets, etc.

%package        javadoc
Summary:        API documentation for %{name}

Requires:       jpackage-utils

%description    javadoc
%{summary}.


%prep
%setup -q

%build
pushd %{name}
%mvn_build

%install
pushd %{name}
%mvn_install

%files -f %{name}/.mfiles
%doc jetty-distribution-remote-resources/src/main/resources/*

%files javadoc -f %{name}/.mfiles-javadoc
%doc jetty-distribution-remote-resources/src/main/resources/*

%changelog
* Mon Aug 05 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1-8
- Update to latest packaging guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Dec 10 2012 Michal Srb <msrb@redhat.com> - 1.1-4
- migrated to plexus-components-component-default (#878549)

* Wed Oct 17 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-3
- Install license files

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Nov  3 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1-1
- Initial version of the package

