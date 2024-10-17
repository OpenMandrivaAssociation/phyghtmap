Name: phyghtmap
Version:	2.23
Release:	1
Source0: http://katze.tfiu.de/projects/%{name}/%{name}_%{version}.orig.tar.gz
Summary: OpenStreetMap contour line generator
URL: https://wiki.openstreetmap.org/wiki/Phyghtmap
License: GPLv2
Group: Sciences/Geosciences
Requires: python
BuildRequires: python
BuildRequires: python-setuptools
Requires: python-matplotlib
Requires: python-numpy
Requires: python-beautifulsoup4
# For supporting GeoTiff input files
Suggests: python-gdal
BuildArch: noarch

# To test, use e.g.
# wget https://planet.osm.ch/switzerland-padded.poly
# phyghtmap --source=view1,view3,srtm1,srtm3 --viewfinder-mask=1 --earthdata-user=bero --earthdata-password='**********' --polygon=switzerland-padded.poly -o switzerland -j20
# Or, for a smaller data set,
# wget http://download.geofabrik.de/europe/luxembourg.poly
# phyghtmap --source=view1,view3,srtm1,srtm3 --viewfinder-mask=1 --earthdata-user=bero --earthdata-password='**********' --polygon=luxembourg.poly -o luxembourg -j20

%description
A tool that generates OpenStreetMap contour lines from NASA SRTM or
viewfinderpanoramas.org data.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%{_bindir}/*
%{python_sitelib}/*
