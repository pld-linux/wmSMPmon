Summary:	WindowMaker memory/swap/CPUs monitor of SMP systems
Summary(pl):	Aplet monitoruj±cy zasoby systemowe maszyn SMP
Name:		wmSMPmon
Version:	2.2
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://goupilfr.org/arch/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://goupilfr.org/?soft=wmsmpmon
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
wmSMPmon is an WindowMaker applet for monitoring memory, swap and CPUs
of SMP systems.

%description -l pl
wmSMPmon jest apletem dla WindowMakera monitoruj±cym obci±¿enie
procesorów, wykorzystanie pamiêci i partycji wymiany w systemach
wieloprocesorowych.

%prep
%setup -q -n %{name}-2.x

%build
%{__make} -C %{name} \
        CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/DockApplets}

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
#install %{SOURCE1}	$RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc GREETINGS LISEZ-MOI
%attr(755,root,root) %{_bindir}/%{name}

#%{_applnkdir}/DockApplets/%{name}.desktop
