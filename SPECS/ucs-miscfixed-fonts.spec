%global fontname ucs-miscfixed
%global fontconf 66-%{fontname}.conf

Name: %{fontname}-fonts
Version: 0.3
Release: 17%{?dist}
License: Public Domain
URL: http://www.cl.cam.ac.uk/~mgk25/ucs-fonts.html
Source0: http://www.cl.cam.ac.uk/~mgk25/download/ucs-fonts.tar.gz
Source1: 66-ucs-miscfixed.conf
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Group: User Interface/X
Summary: Selected set of bitmap fonts
BuildRequires: fontpackages-devel
BuildRequires: xorg-x11-font-utils

%description
The usc-fixed-fonts package provides bitmap fonts for
locations such as terminals.


%prep
%setup -q -c
rm helvR12.bdf

%build

%install
rm -rf $RPM_BUILD_ROOT

install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p *.bdf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
	%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%clean
rm -rf $RPM_BUILD_ROOT

%_font_pkg -f %{fontconf} *.bdf

%doc README	

%changelog
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 12 2012 Pravin Satpute <psatpute@redhat.com> - 0.3-8
- removed gzip 
- upstream new source , #597403

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 25 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-5
- removed \ from description

* Thu Oct 22 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-4
- chnaged conf file priority

* Thu Sep 29 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-3
- modified license field

* Thu Sep 29 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-2
- updated as per package review suggestion, bug 526204


* Thu Sep 29 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-1
- initial packaging
- these fonts was there in bitmap-fonts package previously, packaging it separate as per merger review suggetion.
