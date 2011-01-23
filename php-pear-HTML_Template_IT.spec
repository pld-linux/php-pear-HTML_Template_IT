%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Template
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_IT

Summary:	%{_pearname} - Integrated Templates
Summary(pl.UTF-8):	%{_pearname} - zintegrowane szablony
Name:		php-pear-%{_pearname}
Version:	1.3.0
Release:	1
License:	Modified BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	cbd2fcffd32a39da7b260397156bddbb
URL:		http://pear.php.net/package/HTML_Template_IT/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-PEAR-core
Obsoletes:	php-pear-HTML_Template_IT-tests
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

%description -l pl.UTF-8
HTML_Template_IT - proste API do szablonów. API Isotemplate (template
z phplib) jest nieco zawiłe dla początkujących, ale jest najlepszym
jakie można uzyskać. template::parse() wymaga nazwania źródła i celu,
do którego przetworzony będzie aktualny blok. Źródło i cel mogą być
nazwami bloków lub nawet nazwami funkcji obsługujących. To API daje
maksymalną elastyczność, ale wymaga zawsze wiedzy, co się robi, co nie
jest normalnym stanem dla niektórych autorów skryptów PHP, takich jak
autor tego modułu. Zauważył on, że nie potrzebuje żadnej kontroli,
który blok zostaje przetworzony na który. Jeżeli wszystkie bloki są w
jednym pliku, skrypt wie, jak są zagnieżdżone i w jaki sposób powinny
zostać przetworzone. IT wie, że inner1 jest potomkiem block2, nie ma
potrzeby podawania mu tych informacji. Możliwości:
 - zagnieżdżone bloki,
 - dołączanie zewnętrznych plików,
 - własny format znaczników (domyślnie {mytag}).

HTML_Template_ITX - ta klasa daje całą siłę klasy szablonów z phplib.
Można mieć jeden plik z blokami, ale można także mieć jeden główny
plik i wiele plików zawierających po jednym bloku. Jest to przydatne,
aby pozwolić użytkownikowi na konfigurowalne serwisy. Przez użycie
bloków spoza głównego szablonu pozwala się na łatwe modyfikowanie
niektórych części wyglądu.

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
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
