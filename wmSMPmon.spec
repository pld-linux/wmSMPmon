Summary:	WindowMaker memory/swap/CPUs monitor of SMP systems
Summary(pl):	Aplet monitoruj±cy zasoby systemowe maszyn SMP
Name:		wmSMPmon
Version:	2.1
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://goupil.linuxfr.org/creations/archives/arch/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
wmSMPmon is an WindowMaker applet for monitoring memory, swap and CPUs
of SMP systems.

%description -l pl
wmSMPmon jest apletem dla WindowMakera monitoruj±cym obci±¿enie procesorów,
wykorzystanie pamiêci i partycji wymiany w systemach wieloprocesorowych.

%prep
%setup -q -n %{name}-2.x

%build
make -C %{name} \
        CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/DockApplets}

install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} 	   $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf GREETINGS LISEZ-MOI

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {GREETINGS,LISEZ-MOI}.gz
%attr(755,root,root) %{_bindir}/%{name}

%{_applnkdir}/DockApplets/%{name}.desktop
