Name:           qrtr
Version:        1.0
Release:        1%{?dist}
Summary:        qrtr package

License:        BSD3
URL:            https://github.com/andersson/qrtr
Source0:        https://github.com/andersson/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc systemd-rpm-macros

%description
qrtr package description

%prep
%autosetup

%build
%make_build prefix=%{_prefix} libdir=%{_libdir}

%install
%make_install prefix=%{_prefix} libdir=%{_libdir}

%files
%license LICENSE

# These were generated mostly by _not_ having anything here, and then silencing the errors
# during rpmbuild -bb ~/rpmbuild/SPECS/qrtr.spec

# The below is pretty lazily done, this package would probably be best split into
# multiple subpackages here for the -devel, etc variants.
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_unitdir}/*

%changelog
* Fri May 05 2023 Markus Rathgeb <maggu2810@gmail.com>
- Bump to version 1.0
* Thu Oct 06 2022 Andrew Halaney <ahalaney@redhat.com>
- Initial RPM

