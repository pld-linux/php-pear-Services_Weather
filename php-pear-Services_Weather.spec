%include	/usr/lib/rpm/macros.php
%define         _class          Services
%define         _subclass       Weather
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} acts as an interface to various online weather-services
Summary(pl):	%{_pearname} pe�ni rol� interfejsu do r�nych serwis�w pogodowych
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	0.RC2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}RC2.tgz
# Source0-md5:	d93c70efc6875a0a4584b579dffd5607
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
Services_Weather wyszukuje pogod�, oraz w zale�no�ci od u�ytego
serwisu, tak�e prognoz� dla podanej lokalizacji. Jak do tej pory
obs�ugiwane s�: GlobalWeather z CapeScience, us�uga XML z weather.com
oraz METAR z noaa.gov. Wsparcie dla kolejnych serwis�w zostanie
dodane, o ile b�d� one dost�pne, b�d� mia�y u�yteczne API i b�d�
odpowiednio udokumentowane.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c -n %{name}-%{version}RC2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}RC2/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}RC2/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}RC2/examples
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
