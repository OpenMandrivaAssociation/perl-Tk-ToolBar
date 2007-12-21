
%define realname   Tk-ToolBar
%define version    0.09
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    A toolbar widget for Perl/Tk
Source:     http://www.cpan.org/modules/by-module/Tk/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Tk::CursorControl)

BuildArch: noarch

%description
This module implements a dockable toolbar. It is in the same spirit as the
"short-cut" toolbars found in most major applications, such as most web browsers
and text editors (where you find the "back" or "save" and other shortcut buttons).

Buttons of any type (regular, menu, check, radio) can be created inside this widget.
You can also create Label, Entry and LabEntry widgets.
Moreover, the ToolBar itself can be made dockable, such that it can be dragged to
any edge of your window. Dragging is done in "real-time" so that you can see the
contents of your ToolBar as you are dragging it. Furthermore, if you are close to
a stickable edge, a visual indicator will show up along that edge to guide you.
ToolBars can be made "floatable" such that if they are dragged beyond their
associated window, they will detach and float on the desktop.
Also, multiple ToolBars are embeddable inside each other.

If you drag a ToolBar to within 15 pixels of an edge, it will stick to that
edge. If the ToolBar is further than 15 pixels away from an edge and still
inside the window, but you
release it over another ToolBar widget, then it will be embedded inside the
second ToolBar. You can "un-embed" an embedded ToolBar simply by dragging it
out. You can change the 15 pixel limit using the B<-close> option.



%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*



