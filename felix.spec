#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : felix
Version  : 1.8.0
Release  : 3
URL      : http://archive.apache.org/dist/felix/felix-1.8.0.tar.gz
Source0  : http://archive.apache.org/dist/felix/felix-1.8.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0

%description
No detailed description available

%prep
%setup -q -n felix-1.8.0

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/share
pushd %{buildroot}/usr/share
tar -axf %{SOURCE0}
popd
mkdir -p %{buildroot}/usr/bin
ln -s ../share/felix-1.8.0/bin/felix.jar %{buildroot}/usr/bin/felix.jar

%files
%defattr(-,root,root,-)
/usr/bin/felix.jar
/usr/share/felix-1.8.0
