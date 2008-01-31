%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Weather
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - an interface to various online weather-services
Summary(pl.UTF-8):	%{_pearname} - interfejs do różnych serwisów pogodowych
Name:		php-pear-%{_pearname}
Version:	1.4.2
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6d0bb76bfc56527cb8d013eac196f05a
URL:		http://pear.php.net/package/Services_Wheather/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-HTTP_Request >= 1.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Cache.*)' 'pear(DB.*)' 'pear(HTTP/Request.*)' 'pear(SOAP.*)' 'pear(XML/Serializer.*)' 'pear(Net/FTP.*)'

%description
Services_Weather searches for given locations and retrieves current
weather data and, dependent on the used service, also forecasts. Up to
now, GlobalWeather from CapeScience, a XML service from weather.com
and METAR from noaa.gov are supported. Further services will get
included, if they become available, have a usable API and are properly
documented.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Services_Weather wyszukuje pogodę, oraz w zależności od użytego
serwisu, także prognozę dla podanej lokalizacji. Jak do tej pory
obsługiwane są: GlobalWeather z CapeScience, usługa XML z weather.com
oraz METAR z noaa.gov. Wsparcie dla kolejnych serwisów zostanie
dodane, o ile będą one dostępne, będą miały użyteczne API i będą
odpowiednio udokumentowane.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
sed -i -e '1s#/usr/local/bin/php#%{_bindir}/php#' ./%{php_pear_dir}/data/%{_pearname}/buildMetarDB.php
install -d docs/%{_pearname}
mv ./%{php_pear_dir}/data/%{_pearname}/buildMetarDB.php docs/%{_pearname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%{php_pear_dir}/data/%{_pearname}
