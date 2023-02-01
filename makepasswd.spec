Summary:	Generates (pseudo-)random passwords
Summary(pl.UTF-8):	Generowanie (pseudo-)losowych haseł
Name:		makepasswd
Version:	0.4.2
Release:	3
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.defora.org/pub/projects/makepasswd/%{name}-%{version}.tar.gz
# Source0-md5:	ef95058753742d25f070628166d84815
URL:		http://people.defora.org/~khorben/projects/makepasswd/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Makepasswd generates (pseudo-)random passwords of a desired length. It
is able to generate its crypted equivalent.

%description -l pl.UTF-8
Makepasswd generuje (pseudo-)losowe hasła o żądanej długości. Potrafi
generować ich zaszyfrowane odpowiedniki.

%prep
%setup -q

%build
%{__make} \
	PREFIX=%{_prefix} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -ansi"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install src/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS README
%attr(755,root,root) %{_bindir}/*
