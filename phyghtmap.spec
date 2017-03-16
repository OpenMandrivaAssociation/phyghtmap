Name: phyghtmap
Version: 1.80
Release: 1
Source0: http://katze.tfiu.de/projects/%{name}/%{name}_%{version}.orig.tar.gz
Summary: OpenStreetMap contour line generator
URL: http://wiki.openstreetmap.org/wiki/Phyghtmap
License: GPLv2
Group: Sciences/Geosciences
Requires: python2
BuildRequires: python2
BuildRequires: python2-setuptools
Requires: python2-matplotlib
Requires: python2-beautifulsoup
BuildArch: noarch

# To test, use e.g.
# wget https://planet.osm.ch/switzerland-padded.poly
# phyghtmap --source=view3 --polygon=switzerland-padded.poly -o switzerland

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
