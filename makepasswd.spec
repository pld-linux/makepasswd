Summary:	Generates (pseudo-)random passwords
Summary(pl):	Generuje (pseudo-)losowe has�a
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
Makepasswd generuje (pseudo-)losowe has�a o ��danej d�ugosci. Potrafi
generowa� ich cryptowane odpowiedniki.

%prep
%setup -q

%build
%{__make} \
	PREFIX=%{_prefix}

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
