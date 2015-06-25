%global pypi_name monotonic

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        0.1
Release:        1%{?dist}
Summary:        An implementation of time.monotonic() for Python 2 & < 3.3

# Missing license file from source package
# https://github.com/atdt/monotonic/pull/4
License:        ASL 2.0
URL:            https://github.com/atdt/%{pypi_name}
Source0:        https://pypi.python.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools


%description
This module provides a ``monotonic()`` function which
returns the
value (in fractional seconds) of a clock which never goes
backwards.

On Python 3.3 or newer, ``monotonic`` will be an alias of
``time.monotonic`` from the standard library. On older versions,
it will fall


%if 0%{with_python3}
%package -n python3-%{pypi_name}
Summary:        An implementation of time.monotonic() for Python 2 & < 3.3

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{pypi_name}
This module provides a ``monotonic()`` function which
returns the
value (in fractional seconds) of a clock which never goes
backwards.

On Python 3.3 or newer, ``monotonic`` will be an alias of
``time.monotonic`` from the standard library. On older versions,
it will fall
%endif


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif


%build
%{__python2} setup.py build

%if 0%{with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif


%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%if 0%{with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif


%files
#%license LICENSE
%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{with_python3}
%files -n python3-%{pypi_name}
#%license LICENSE
%{python3_sitelib}/__pycache__/%{pypi_name}.*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Thu Jun 18 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1-1
- Initial package
