Name: mythes-uk
Summary: Ukrainian thesaurus
Version: 1.6.5
Release: 5%{?dist}
Source: http://downloads.sourceforge.net/ispell-uk/spell-uk-%{version}.tgz
Group: Applications/Text
URL: http://sourceforge.net/projects/ispell-uk
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#unused myspell dicts are under GPLv2+ or LGPLv2+ or MPLv1.1
#unused hyphenation dicts are under GPLv2+
#toplevel is GPLv2+ or LGPLv2+
License: (GPLv2+ or LGPLv2+) and (GPLv2+ or LGPLv2+ or MPLv1.1) and GPLv2+
BuildRequires: perl, mythes-devel
BuildArch: noarch
Requires: mythes

%description
Ukrainian thesaurus.

%prep
%setup -q -n spell-uk-%{version}

%build
cd src/thesaurus
mv -f th_uk_UA.dat th_uk_UA_v2.dat
th_gen_idx.pl < th_uk_UA_v2.dat > th_uk_UA_v2.idx

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p src/thesaurus/th_uk_UA_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README README.uk COPYING.GPL COPYING.LGPL Copyright
%{_datadir}/mythes/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 06 2012 Caolán McNamara <caolanm@redhat.com> - 1.6.5-4
- clarify license

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun May 22 2011 Caolán McNamara <caolanm@redhat.com> - 1.6.5-1
- latest version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Apr 04 2010 Caolan McNamara <caolanm@redhat.com> - 1.6.0-2
- mythes now owns /usr/share/mythes

* Tue Aug 18 2009 Caolán McNamara <caolanm@redhat.com> - 1.6.0-1
- latest version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 06 2009 Caolán McNamara <caolanm@redhat.com> - 1.5.7-1
- initial version
