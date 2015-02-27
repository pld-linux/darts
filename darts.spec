Summary:	Double ARray Trie System
Summary(pl.UTF-8):	System DARTS (Double ARray Trie System)
Name:		darts
Version:	0.32
Release:	2
License:	LGPL or BSD
Group:		Libraries
Source0:	http://chasen.org/~taku/software/darts/src/%{name}-%{version}.tar.gz
# Source0-md5:	2149e32b8e33cf38864f7fc25a6532fb
URL:		http://chasen.org/~taku/software/darts/
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
# COPYING is general file; LGPL text is in LGPL file
%doc AUTHORS BSD COPYING ChangeLog
%lang(ja) %doc doc/*
%dir %{_libdir}/darts
%attr(755,root,root) %{_libdir}/darts/darts
%attr(755,root,root) %{_libdir}/darts/mkdarts
%{_includedir}/darts.h
