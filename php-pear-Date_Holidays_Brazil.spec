%define		_class		Date
%define		_subclass	Holidays_Brazil
%define		_status		alpha
%define		_pearname	Date_Holidays_Brazil
Summary:	%{_pearname} - Driver based class to calculate holidays in Brazil
Summary(pl.UTF-8):	%{_pearname} - klasa do obliczania świąt brazylijskich
Name:		php-pear-%{_pearname}
Version:	0.1.2
Release:	3
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	057a53a7d12cc7de9609d8bcc0a8c6f5
URL:		http://pear.php.net/package/Date_Holidays_Brazil/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Date_Holidays >= 0.18.0
Obsoletes:	php-pear-Date_Holidays_Brazil-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Date_Holidays helps you calculate the dates and titles of holidays and
other special celebrations. This is the driver for calculating
holidays in Brazil.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Date_Holidays pozwala na obliczenie dat oraz tytułów świąt oraz
specjalnych okazji. Klasa ta pozwala na wyliczenie świąt
brazylijskich.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Date/Holidays/Driver/Brazil.php
