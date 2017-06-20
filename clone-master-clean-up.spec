#
# spec file for package clone-master-clean-up
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           clone-master-clean-up
Version:        1.2
Release:        0
License:        GPL-2.0+
Summary:        Clean up a system for cloning preparation
Url:            https://www.suse.com
Group:          System/Management
Source0:        clone-master-clean-up
Source1:        clone-master-clean-up.1
Source2:        sysconfig.clone-master-clean-up
Source3:        custom_remove.template
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       systemd sed curl coreutils
BuildArch:      noarch

%description
Clean up a system for cloning preparation by cleaning up usage history and log files, etc.

%prep

%build

%install
mkdir -p %{buildroot}%{_sbindir}
install -m700 %{S:0} %{buildroot}/%{_sbindir}/clone-master-clean-up
# manpage
mkdir -p %{buildroot}%{_mandir}/man1
install -m644 %{S:1} %{buildroot}/%{_mandir}/man1/clone-master-clean-up.1
# sysconfig file
mkdir -p %{buildroot}/%{_localstatedir}/adm/fillup-templates/
install -m644 %{S:2} %{buildroot}/%{_localstatedir}/adm/fillup-templates/sysconfig.clone-master-clean-up
# template
mkdir -p %{buildroot}/%{_localstatedir}/adm/%{name}/
install -m644 %{S:3} %{buildroot}/%{_localstatedir}/adm/%{name}/custom_remove.template

%post
%fillup_only -n clone-master-clean-up

%files
%defattr(-,root,root)
%{_sbindir}/*
%{_mandir}/man1/*
%config %{_localstatedir}/adm/fillup-templates/*
%dir %{_localstatedir}/adm/%{name}
%config %{_localstatedir}/adm/%{name}/custom_remove.template
%ghost %config %{_localstatedir}/adm/%{name}/custom_remove
