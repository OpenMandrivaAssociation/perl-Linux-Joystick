%define upstream_name    Linux-Joystick
%define upstream_version v0.0.1

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Linux-Joystick - Perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Linux-Joystick
Source0:	https://cpan.metacpan.org/authors/id/B/BW/BWATSON/Linux-Joystick-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Linux-Joystick - Perl module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

