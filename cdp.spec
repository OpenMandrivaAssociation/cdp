%define version 0.33
%define release %mkrel 19
%define realversion 0.33-13

Summary: An interactive text-mode program for controlling audio CD-ROMs
Name: cdp
Version: %{version}
Release: %{release}
License: GPL
Group: Sound
URL: http://cdp.sourceforge.net/
BuildRequires: ncurses-devel
Source: ftp://sunsite.unc.edu/pub/Linux/apps/sound/cdrom/curses/cdp-%{realversion}.tar.bz2
Patch7: cdp-keys.patch.bz2
Patch8: cdp-cdrom_o_nonblock.patch.bz2

%description
The cdp program plays audio CDs in your computer's CD-ROM drive.
Cdp includes a full-screen interface version and a command line
version.

Install cdp to play audio CDs on your system.

%prep
%setup -q -n %{name}-%{realversion}
%patch7 -p1 
%patch8 -p1 

%build
#remove old x86 .o files
rm -fr *.o
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man,man/man1}

%makeinstall DESTDIR=$RPM_BUILD_ROOT
# DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT/usr/share
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT/usr/share/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/cdp
/usr/bin/cdplay
%{_mandir}/man1/cdp.1*
