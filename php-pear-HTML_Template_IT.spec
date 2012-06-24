%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Template
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_IT

Summary:	%{_pearname} - Integrated Templates
Summary(pl):	%{_pearname} - zintegrowane szablony
Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1d4bf6f13ed4de43a0f837c0de9f2d7a
URL:		http://pear.php.net/package/HTML_Template_IT/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# included in tests
%define		_noautoreq 'pear(Console_TestListener.php)' 'pear(IT_api_testcase.php)' 'pear(IT_usage_testcase.php)'

%description
HTML_Template_IT: Simple template API. The Isotemplate API is somewhat
tricky for a beginner although it is the best one you can build.
template::parse() [phplib template = Isotemplate] requests you to name
a source and a target where the current block gets parsed into. Source
and target can be block names or even handler names. This API gives
you a maximum of fexibility but you always have to know what you do
which is quite unusual for PHP skripter like me. I noticed that I do
not any control on which block gets parsed into which one. If all
blocks are within one file, the script knows how they are nested and
in which way you have to parse them. IT knows that inner1 is a child
of block2, there's no need to tell him about this. Features:
 - Nested blocks,
 - Include external file,
 - Custom tags format (default {mytag}).

HTML_Template_ITX: With this class you get the full power of the
phplib template class. You may have one file with blocks in it but you
have as well one main file and multiple files one for each block. This
is quite useful when you have user configurable websites. Using blocks
not in the main template allows you to modify some parts of your
layout easily.

In PEAR status of this package is: %{_status}.

%description -l pl
HTML_Template_IT - proste API do szablon�w. API Isotemplate (template
z phplib) jest nieco zawi�e dla pocz�tkuj�cych, ale jest najlepszym
jakie mo�na uzyska�. template::parse() wymaga nazwania �r�d�a i celu,
do kt�rego przetworzony b�dzie aktualny blok. �r�d�o i cel mog� by�
nazwami blok�w lub nawet nazwami funkcji obs�uguj�cych. To API daje
maksymaln� elastyczno��, ale wymaga zawsze wiedzy, co si� robi, co nie
jest normalnym stanem dla niekt�rych autor�w skrypt�w PHP, takich jak
autor tego modu�u. Zauwa�y� on, �e nie potrzebuje �adnej kontroli,
kt�ry blok zostaje przetworzony na kt�ry. Je�eli wszystkie bloki s� w
jednym pliku, skrypt wie, jak s� zagnie�d�one i w jaki spos�b powinny
zosta� przetworzone. IT wie, �e inner1 jest potomkiem block2, nie ma
potrzeby podawania mu tych informacji. Mo�liwo�ci:
 - zagnie�d�one bloki,
 - do��czanie zewn�trznych plik�w,
 - w�asny format znacznik�w (domy�lnie {mytag}).

HTML_Template_ITX - ta klasa daje ca�� si�� klasy szablon�w z phplib.
Mo�na mie� jeden plik z blokami, ale mo�na tak�e mie� jeden g��wny
plik i wiele plik�w zawieraj�cych po jednym bloku. Jest to przydatne,
aby pozwoli� u�ytkownikowi na konfigurowalne serwisy. Przez u�ycie
blok�w spoza g��wnego szablonu pozwala si� na �atwe modyfikowanie
niekt�rych cz�ci wygl�du.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

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
%{php_pear_dir}/%{_class}/%{_subclass}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
