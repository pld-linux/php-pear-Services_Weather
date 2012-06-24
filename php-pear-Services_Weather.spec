%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Weather
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - an interface to various online weather-services
Summary(pl):	%{_pearname} - interfejs do r�nych serwis�w pogodowych
Name:		php-pear-%{_pearname}
Version:	1.4.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a83fbf5e2e7ffd22219c513cfefe6b52
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

%description -l pl
Services_Weather wyszukuje pogod�, oraz w zale�no�ci od u�ytego
serwisu, tak�e prognoz� dla podanej lokalizacji. Jak do tej pory
obs�ugiwane s�: GlobalWeather z CapeScience, us�uga XML z weather.com
oraz METAR z noaa.gov. Wsparcie dla kolejnych serwis�w zostanie
dodane, o ile b�d� one dost�pne, b�d� mia�y u�yteczne API i b�d�
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
