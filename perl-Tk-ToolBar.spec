%define upstream_name Tk-ToolBar
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	A toolbar widget for Perl/Tk
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Tk/%{upstream_name}-%{upstream_version}.zip

BuildRequires:	perl(Tk::CursorControl)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module implements a dockable toolbar. It is in the same spirit as the
"short-cut" toolbars found in most major applications, such as most web
browsers and text editors (where you find the "back" or "save" and other
shortcut buttons).

Buttons of any type (regular, menu, check, radio) can be created inside this
widget.  You can also create Label, Entry and LabEntry widgets.  Moreover, the
ToolBar itself can be made dockable, such that it can be dragged to any edge of
your window. Dragging is done in "real-time" so that you can see the contents
of your ToolBar as you are dragging it. Furthermore, if you are close to a
stickable edge, a visual indicator will show up along that edge to guide you.
ToolBars can be made "floatable" such that if they are dragged beyond their
associated window, they will detach and float on the desktop.
Also, multiple ToolBars are embeddable inside each other.

If you drag a ToolBar to within 15 pixels of an edge, it will stick to that
edge. If the ToolBar is further than 15 pixels away from an edge and still
inside the window, but you release it over another ToolBar widget, then it will
be embedded inside the second ToolBar. You can "un-embed" an embedded ToolBar
simply by dragging it out. You can change the 15 pixel limit using the
-close option.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.100.0-3
+ Revision: 773578
- cleanout spec
- package is noarch
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild for perl 5.12

* Sun Feb 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.1
+ Revision: 512613
- update to

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 401499
- rebuild using %%perl_convert_version
- fixed license field

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.09-5mdv2009.0
+ Revision: 258659
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.09-4mdv2009.0
+ Revision: 246657
- rebuild
- fix description-line-too-long

* Mon Feb 04 2008 Jérôme Quelin <jquelin@mandriva.org> 0.09-2mdv2008.1
+ Revision: 162066
- binary module: removing noarch tag

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Jérôme Quelin <jquelin@mandriva.org> 0.09-1mdv2008.1
+ Revision: 110511
- import perl-Tk-ToolBar


