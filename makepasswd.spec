Summary:	Generates (pseudo-)random passwords
Summary(pl):	Generowanie (pseudo-)losowych hase³
Name:		makepasswd
Version:	0.4.1
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.defora.org/pub/projects/makepasswd/%{name}-%{version}.tar.gz
# Source0-md5:	3759881f5957a72e3e4d201c50362b67
URL:		http://www.defora.org/projects/makepasswd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Makepasswd generates (pseudo-)random passwords of a desired length. It
is able to generate its crypted equivalent.

%description -l pl
Makepasswd generuje (pseudo-)losowe has³a o ¿±danej d³ugo¶ci. Potrafi
generowaæ ich zaszyfrowane odpowiedniki.

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
