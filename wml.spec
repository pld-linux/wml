%include        %{_libdir}/rpm/macros.perl
Summary:	Website META Language
Summary(pl):	META Jêzyk do obs³ugi serwisów WWW
Name:		wml
Version:	2.0.3
Release:	1
Copyright:	GPL
Group:		Applications/Publishing
Group(pl):	Aplikacje/Publikowanie
Vendor:		Ralf S. Engelschall <rse@engelschall.com>
Source0:	http://www.engelschall.com/sw/wml/%{name}-%{version}.tar.gz
Patch0:		wml-DESTDIR.patch
Patch1:		wml-install.patch
Patch2:		wml-PL_curstash.patch
URL:		http://www.engelschall.com/sw/wml/
BuildRequires:	rpm-perlprov
BuildRequires:	perl >= 5.003
BuildRequires:	ncurses-devel
BuildRequires:	libpng-devel
BuildRequires:	perl-Bit-Vector >= 5.2
BuildRequires:	perl-File-PathConvert
BuildRequires:	perl-Image-Size >= 2.6
BuildRequires:	perl-HTML-Clean
BuildRequires:	sed
BuildRequires:	findutils
# BuildRequires:	perl-IO-File # tego nie mamy
BuildRequires:	perl-Term-ReadKey >= 2.11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WML is a free and extensible Webdesigner's off-line HTML generation
toolkit for Unix. WML consists of a control frontend driving up to
nine backends in a sequential pass-oriented filtering scheme. Each
backend provides one particular core language. For maximum power WML
additionally ships with a well-suited set of include files which
provide higher-level features build on top of the backends core
languages. While not trivial and idiot proof WML provides most of the
core features real hackers always wanted for HTML generation.

%description -l pl
WML jest darmowym i ³atwo rozszerzalnym zbiorem narzêdzi do
generowania plików HTML. WML udostêpnia dziewiêæ sekwencyjnie
uruchamianych systemów filtrów. Ka¿dy filtr udostêpnia jeden g³ówny
jêzyk. WML udostêpnia wiêkszo¶æ narzêdzi jednak prawdziwi twórcy
plików HTML s± nadal potrzebni.

%prep 
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure \
	--with-perl=%{_bindir}/perl \
	--with-openworld \
	--with-forced-cc="gcc $RPM_OPT_FLAGS -I%{_includedir}/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# fix paths
for file in `find $RPM_BUILD_ROOT -type f`; do
	sed -e "s#${RPM_BUILD_ROOT}##g" ${file} > ${file}.new
	mv ${file}.new ${file}
done

gzip -9nf ANNOUNCE BUGREPORT COPYRIGHT CREDITS ChangeLog \
	  NEWS README README.mp4h SUPPORT VERSION.HISTORY \
	  $RPM_BUILD_ROOT%{_mandir}/man*/*
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/aux
%dir %{_libdir}/%{name}/exec
%attr(755,root,root) %{_libdir}/%{name}/exec/*
%{_libdir}/%{name}/include
%{_libdir}/%{name}/perl
%{_mandir}/man*/*
