#-
# Copyright 2014 Emmanuel Vadot <elbarto@bocal.org>
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted providing that the following conditions 
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

Name:		lightdm-config-exam
Version:        0.1
Release:        0
Summary:        BLINUX config of lightdm
License:        BSD-2-Clause
Group:          System/X11/Displaymanagers

Source0:        lightdm.conf
BuildRequires:  lightdm
BuildRequires:	lightdm-gtk-greeter
BuildRequires:	sysconfig-cli
Requires:	sysconfig-cli
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

Vendor:         Bocal
Packager:       Emmanuel Vadot <elbarto@bocal.org>
Url:            http://www.blinux.fr

%description
LightDM configuration for exam mode of Blinux

%prep

%build

%install
install -D -p -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf

%clean
rm -rf %{buildroot}

%post
sysconfig-cli displaymanager DISPLAYMANAGER lightdm
sysconfig-cli displaymanager DISPLAYMANAGER_AUTOLOGIN exam
sysconfig-cli displaymanager DISPLAYMANAGER_PASSWORD_LESS_LOGIN yes

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/lightdm/lightdm.conf

%changelog
* Wed Aug 27 2014 Emmanuel Vadot <elbarto@bocal.org> - 0.1-0
- Package creation
