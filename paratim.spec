Summary:	Remake of the old DOS game Paratrooper
Summary(pl.UTF-8):	Remake starej dosowej gry Paratrooper
Name:		paratim
Version:	0.1.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/paratim/%{name}-%{version}.tar.bz2
# Source0-md5:	96eb704cf93134a25ae977f1f474c308
URL:		http://paratim.sourceforge.net/
BuildRequires:	SDL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Paratim (Paratrooper Improved) is a remake of the old DOS game
Paratrooper.

%description -l pl.UTF-8
Paratim (Paratrooper Improved) jest remakiem starej dosowej gry
Paratrooper.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
