Summary:	Ruby event-driven HTTP server
Summary(pl.UTF-8):	Serwer HTTP sterowany zdarzeniami dla języka Ruby
Name:		ruby-eventmachine_httpserver
Version:	0.0.1
Release:	1
License:	Ruby
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/18523/eventmachine_httpserver-%{version}.gem
# Source0-md5:	49be4af3e878ff32b20478ba2ad8b365
URL:		http://rubyforge.org/projects/eventmachine/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	ruby-modules
BuildRequires:	setup.rb
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-eventmachine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby/EventMachine is a fast, simple event-processing library for Ruby
programs. It lets you write network clients and servers without
handling sockets - all you do is send and receive data.
Single-threaded socket engine - scalable and FAST!

The HTTP Server module makes a simple HTTP server based on the
EventMachine framework.

%description -l pl.UTF-8
Ruby/EventMachine to szybka, prosta biblioteka przetwarzania zdarzeń
dla programów w języku Ruby. Pozwala pisać klientów i serwery sieciowe
bez obsługi gniazd sieciowych - wystarczy wysyłać i odbierać dane.
Jednowątkowy silnik gniazd - skalowalny i szybki.

Moduł serwera HTTP to prosty serwer HTTP oparty na szkielecie
EventMachine.

%prep
%setup -q -c -T
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-

%build
cp %{_datadir}/setup.rb .
touch ext/MANIFEST
ruby setup.rb config --rbdir=%{ruby_rubylibdir} --sodir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/*.rb
%dir %{ruby_rubylibdir}/evma_httpserver
%{ruby_rubylibdir}/evma_httpserver/*.rb
%attr(755,root,root) %{ruby_archdir}/*.so
