%include	/usr/lib/rpm/macros.perl
Summary:	Website META Language
Summary(pl):	META Jêzyk do obs³ugi serwisów WWW
Name:		wml
Version:	2.0.9
Release:	2
License:	GPL
Group:		Applications/Publishing
Source0:	http://thewml.org/distrib/%{name}-%{version}.tar.gz
# Source0-md5:	a7c9da3b58f7e40706e3c29c37b4822b
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-install.patch
Patch2:		%{name}-PL_curstash.patch
Patch3:		%{name}-acfix.patch
URL:		http://thewml.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRequires:	ncurses-devel
BuildRequires:	perl-Bit-Vector >= 5.2
BuildRequires:	perl-File-PathConvert
BuildRequires:	perl-HTML-Clean
# BuildRequires:	perl-IO-File # we don't have this one
BuildRequires:	perl-Image-Size >= 2.6
BuildRequires:	perl-Term-ReadKey >= 2.11
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if "%{_lib}" == "lib64"
%define		libsubdir	64/wml
%else
%define		libsubdir	/wml
%endif

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
%patch3 -p1

%build
cp -f /usr/share/automake/config.* etc
cp -f /usr/share/automake/config.* wml_backend/p2_mp4h
cd wml_backend/p3_eperl
%{__autoconf}
cd ../p4_gm4
%{__autoconf}
cd ../../wml_aux/iselect
%{__autoconf}
cd ../../wml_common/gd
%{__autoconf}
cd ../..
%configure \
	--with-incdir=/usr/include/ncurses \
	--with-perl=%{__perl} \
	--with-openworld
%{__make} \
	libsubdir=%{libsubdir}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libsubdir=%{libsubdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE BUGREPORT COPYRIGHT CREDITS ChangeLog
%doc NEWS README README.mp4h SUPPORT VERSION.HISTORY
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/exec
%attr(755,root,root) %{_libdir}/%{name}/exec/*
%{_libdir}/%{name}/include
%{_libdir}/%{name}/perl
%{_mandir}/man*/*
