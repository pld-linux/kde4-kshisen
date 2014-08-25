%define		_state		stable
%define		orgname		kshisen
%define		qtver		4.8.0

Summary:	KDE Shisen-Sho
Summary(pl.UTF-8):	Shisen-Sho dla KDE
Summary(pt_BR.UTF-8):	Jogo Shisen para o KDE
Name:		kde4-%{orgname}
Version:	4.14.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	9a10d6e79d7c97ea6fb1ff9f00da8647
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	kde4-libkmahjongg-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shisen-Sho is similar to Mahjongg and uses the same set of tiles as
KMahjongg. The object of the game is to remove all tiles from the
field.

%description -l pl.UTF-8
Shisen-Sho to gra podobna do Mahjongg i wykorzystująca ten sam zestaw
kostek. Celem gry jest usunięcie wszystkich kostek z planszy.

%description -l pt_BR.UTF-8
Jogo Shisen para o KDE.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kshisen
%{_desktopdir}/kde4/kshisen.desktop
%{_datadir}/config.kcfg/kshisen.kcfg
%{_datadir}/apps/kshisen
%{_datadir}/sounds/kshisen
%{_iconsdir}/*/*/apps/kshisen.png
