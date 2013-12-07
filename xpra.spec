Summary:	Persistent remote applications for X
Name:		xpra
Version:	0.7.8
Release:	5
License:	GPLv2+
Group:		Networking/Other
URL:		http://xpra.org/
Source0:	http://xpra.org/src/%{name}-%{version}.tar.xz
Patch0:		libavcdc_lx11.patch
Patch1:		disable-x264.patch
BuildRequires:	python-setuptools
BuildRequires:	python-cython
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	pkgconfig(gdk-x11-2.0)
BuildRequires:	pkgconfig(libswscale)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pygtk2.0-devel
Requires:	pygtk2
Requires:	x11-tools
Requires:	x11-server-xvfb
Requires:	python-imaging
Requires:	python-dbus

%description
Xpra gives you "persistent remote applications" for X. That is, unlike normal
X applications, applications run with xpra are "persistent" -- you can run
them remotely, and they don't die if your connection does. You can detach them,
and reattach them later -- even from another computer -- with no loss of state.
And unlike VNC or RDP, xpra is for remote applications, not remote desktops --
individual applications show up as individual windows on your screen, managed
by your window manager. They're not trapped in a box. So basically it's screen
for remote X apps.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
sed -e "s:libwebp.so.2:libwebp.so.4:" \
	-i "xpra/webm/__init__.py" || die

python make_constants_pxi.py wimpiggy/lowlevel/constants.txt wimpiggy/lowlevel/constants.pxi
python setup.py build

%install
python setup.py install -O1  --prefix /usr --skip-build --root %{buildroot}

%files
%{_sysconfdir}/%{name}/xorg.conf
%{_sysconfdir}/%{name}/xpra.conf
%{_bindir}/parti
%{_bindir}/parti-repl
%{_bindir}/xpra*
%{_iconsdir}/%{name}.png
%{_datadir}/applications/xpra_launcher.desktop
%{python_sitearch}/xpra
%{python_sitearch}/parti
%{python_sitearch}/wimpiggy
%{python_sitearch}/parti_all-*.egg-info
%{_datadir}/xpra
%{_datadir}/parti
%{_datadir}/wimpiggy
%{_mandir}/man1/xpra.1.*
%{_mandir}/man1/parti.1.*
%{_mandir}/man1/xpra_launcher.1.*

