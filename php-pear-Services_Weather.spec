%include	/usr/lib/rpm/macros.php
%define         _class          Services
%define         _subclass       Weather
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} acts as an interface to various online weather-services
Summary(pl):	%{_pearname} pe³ni rolê interfejsu do ró¿nych serwisów pogodowych
Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	10dd2cff725b175c1908f402c26f4228
URL:		http://pear.php.net/package/Services_Wheather/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Services_Weather searches for given locations and retrieves current
weather data and, dependent on the used service, also forecasts. Up to
now, GlobalWeather from CapeScience, a XML service from weather.com
and METAR from noaa.gov are supported. Further services will get
included, if they become available, have a usable API and are properly
documented.

This class has in PEAR status: %{_status}.

%description -l pl
Services_Weather wyszukuje pogodê, oraz w zale¿no¶ci od u¿ytego
serwisu, tak¿e prognozê dla podanej lokalizacji. Jak do tej pory
obs³ugiwane s±: GlobalWeather z CapeScience, us³uga XML z weather.com
oraz METAR z noaa.gov. Wsparcie dla kolejnych serwisów zostanie
dodane, o ile bêd± one dostêpne, bêd± mia³y u¿yteczne API i bêd±
odpowiednio udokumentowane.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c
cd %{_pearname}-%{version}
sed 's#/usr/local/bin/php#/usr/bin/php#' buildMetarDB.php >> tmp
mv -f tmp buildMetarDB.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
