Summary:	WindowMaker memory/swap/CPUs monitor of SMP systems
Summary(pl.UTF-8):	Aplet monitorujący zasoby systemowe maszyn SMP
Name:		wmSMPmon
Version:	2.2
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://goupilfr.org/arch/%{name}-%{version}.tar.gz
# Source0-md5:	1c4c1729f87082002c2f196a96b9e7d1
Source1:	%{name}.desktop
URL:		http://goupilfr.org/?soft=wmsmpmon
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmSMPmon is an WindowMaker applet for monitoring memory, swap and CPUs
of SMP systems.

%description -l pl.UTF-8
wmSMPmon jest apletem dla WindowMakera monitorującym obciążenie
procesorów, wykorzystanie pamięci i partycji wymiany w systemach
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

#%%{_applnkdir}/DockApplets/%{name}.desktop
