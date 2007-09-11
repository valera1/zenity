Summary:	The GNOME port of dialog
Summary(pl.UTF-8):	Port dialog dla GNOME
Name:		zenity
Version:	2.19.2
Release:	1
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/zenity/2.19/%{name}-%{version}.tar.bz2
# Source0-md5:	e72dc92169ecdb5b32bf0839b91055b9
URL:		http://freshmeat.net/projects/zenity/
BuildRequires:	GConf2-devel >= 2.19.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	gnome-common >= 2.18.0
BuildRequires:	gnome-doc-utils >= 0.11.2
BuildRequires:	intltool >= 0.36.1
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomecanvas-devel >= 2.19.2
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
Requires:	libgnomecanvas >= 2.19.2
Conflicts:	gnome-utils < 2.3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zenity is a rewrite of gdialog, the GNOME port of dialog which allows
you to display dialog boxes from the commandline and shell scripts.

%description -l pl.UTF-8
zenity jest kontynuacją programu gdialog, portu dialog dla GNOME.
Umożliwia on wyświetlanie okien dialogowych z linii komend i ze
skryptów powłoki.

%prep
%setup -q

%build
%{__gnome_doc_prepare}
%{__intltoolize}
%{__gnome_doc_common}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# zenity-0.1.mo but gnome/help/zenity
%find_lang %{name}-0.1 --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f %{name}-0.1.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_omf_dest_dir}/zenity
%{_omf_dest_dir}/zenity/zenity-C.omf
%lang(bg) %{_omf_dest_dir}/zenity/zenity-bg.omf
%lang(en_GB) %{_omf_dest_dir}/zenity/zenity-en_GB.omf
%lang(es) %{_omf_dest_dir}/zenity/zenity-es.omf
%lang(fr) %{_omf_dest_dir}/zenity/zenity-fr.omf
%lang(ru) %{_omf_dest_dir}/zenity/zenity-ru.omf
%lang(sv) %{_omf_dest_dir}/zenity/zenity-sv.omf
%lang(uk) %{_omf_dest_dir}/zenity/zenity-uk.omf
%{_datadir}/%{name}
%{_mandir}/man1/*
