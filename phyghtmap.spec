Name: phyghtmap
Version: 1.50
Release: 1
Source0: http://katze.tfiu.de/projects/%{name}/%{name}_%{version}.orig.tar.gz
Summary: OpenStreetMap contour line generator
URL: http://phyghtmap.sf.net/
License: GPLv2
Group: Sciences/Geosciences
Requires: python2
BuildRequires: python2
BuildRequires: python2-setuptools
Requires: python2-matplotlib
BuildArch: noarch

%description
A tool that generates OpenStreetMap contour lines from NASA SRTM or
viewfinderpanoramas.org data.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot}

%files
%{_bindir}/*
%{python2_sitelib}/*
