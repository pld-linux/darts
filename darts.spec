Summary:	Double ARray Trie System
Summary(pl.UTF-8):	System DARTS (Double ARray Trie System)
Name:		darts
Version:	0.2
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://cl.aist-nara.ac.jp/~taku-ku/software/darts/src/%{name}-%{version}.tar.gz
# Source0-md5:	779084cfe955320b5db102dcb254162b
URL:		http://cl.aist-nara.ac.jp/~taku-ku/software/darts/
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}

%description
Double ARray Trie System.

%description -l pl.UTF-8
System DARTS (Double ARray Trie System).

%prep
%setup -q

%build
%configure
%{__make} \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%lang(ja) %doc doc/*
%attr(755,root,root) %{_libdir}/darts
%{_includedir}/darts.h
