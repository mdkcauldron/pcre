%define pcre_major 1
%define pcrecpp_major 0
%define pcreposix_major 1
%define pcreposix_compat_major 0
%define libname_orig lib%{name}
%define libname16_orig lib%{name}16
%define libname32_orig lib%{name}32
%define libname	%mklibname pcre %{pcre_major}
%define libname16 %mklibname pcre 16 %{pcrecpp_major}
%define libname32 %mklibname pcre 32 %{pcrecpp_major}
%define libnamecpp %mklibname pcrecpp %{pcrecpp_major}
%define libnameposix %mklibname pcreposix %{pcreposix_major}
%define libnameposix_compat %mklibname pcreposix %{pcreposix_compat_major}
%define develname %mklibname -d pcre
%define develcpp %mklibname -d pcrecpp
%define develposix %mklibname -d pcreposix
%define olddevelname %mklibname %{name} 0 -d

%define build_pcreposix_compat 1

Summary:	Perl-compatible regular expression library
Name:		pcre
Version:	8.35
Release:	%mkrel 2
License:	BSD-Style
Group:		File tools
URL:		http://www.pcre.org/
Source0:	ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/%{name}-%{version}.tar.bz2.sig
Requires:	%{libname} = %{version}-%{release}
BuildRequires:	automake
Patch0:		pcre-0.6.5-fix-detect-into-kdelibs.patch
Patch1:		pcre-8.33-linkage-fix.patch
# from debian:
Patch4:		pcre-pcreposix-glibc-conflict.patch
# from fedora
# upstream bug #1463
Patch5:		pcre-8.35-Do-not-rely-on-wrapping-signed-integer-while-parsein.patch
# upstream bug #1492
Patch6:		pcre-8.35-Fix-bad-starting-data-when-char-with-more-than-one-o.patch
# upstream bug #1493
Patch7:		pcre-8.35-Fix-not-including-VT-in-starting-characters-for-s.patch
# upstream bug #1494
Patch8:		pcre-8.35-Fix-bad-compile-of-Qx-.-where-x-is-any-character.patch
# upstream bug #1500
Patch9:		pcre-8.35-Fix-empty-matching-possessive-zero-repeat-groups-bug.patch
# upstream bug #1502
Patch10:	pcre-8.35-Fixed-several-memory-leaks-in-pcregrep.patch
# upstream bug #1503
Patch11:	pcre-8.35-Fix-compiler-crash-misbehaviour-for-zero-repeated-gr.patch
# upstream bug #1515
Patch12:	pcre-8.35-Fix-compile-time-loop-for-recursive-reference-within.patch


%description
PCRE has its own native API, but a set of "wrapper" functions that are based on
the POSIX API are also supplied in the library libpcreposix. Note that this
just provides a POSIX calling interface to PCRE: the regular expressions
themselves still follow Perl syntax and semantics. 
This package contains a grep variant based on the PCRE library.

%package -n	%{libname}
Group:		System/Libraries
Summary:	Perl-compatible regular expression library
Requires(pre):	filesystem >= 2.1.9-18
Provides:	%{libname_orig} = %{version}-%{release}

%description -n	%{libname}
This package contains the shared library libpcre.

%package -n	%{libname16}
Group:		System/Libraries
Summary:	Perl-compatible regular expression library
Requires(pre):	filesystem >= 2.1.9-18
Provides:	%{libname16_orig} = %{version}-%{release}
Obsoletes:	%{_lib}pcre16_1 < %{version}-%{release}

%description -n	%{libname16}
This package contains the shared library libpcre.

%package -n	%{libname32}
Group:		System/Libraries
Summary:	Perl-compatible regular expression library
Requires(pre):	filesystem >= 2.1.9-18
Provides:	%{libname32_orig} = %{version}-%{release}
Obsoletes:	%{_lib}pcre32_1 < %{version}-%{release}

%description -n	%{libname32}
This package contains the shared library libpcre.

%package -n	%{libnamecpp}
Group:		System/Libraries
Summary:	Perl-compatible regular expression library
Conflicts:	%{_lib}pcre0 < 8.21-3

%description -n	%{libnamecpp}
This package contains the shared library libpcrecpp.


%package -n	%{libnameposix}
Group:		System/Libraries
Summary:	Perl-compatible regular expression library
Conflicts:	%{_lib}pcre0 < 8.21-3

%description -n	%{libnameposix}
This package contains the shared library libpcreposix.


%package -n	%{libnameposix_compat}
Group:		System/Libraries
Summary:	Perl-compatible regular expression library
Conflicts:	%{_lib}pcre0 < 8.21-3

%description -n	%{libnameposix_compat}
This package contains the shared library libpcreposix compat.


%package -n	%{develname}
Group:		Development/C
Summary:	Headers and static lib for pcre development
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libname16} = %{version}-%{release}
Requires:	%{libname32} = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{olddevelname} < 8.21-3

%description -n	%{develname}
Install this package if you want do compile applications using the pcre
library.

%package -n	%{develcpp}
Group:		Development/C++
Summary:	Headers and static lib for pcrecpp development
Provides:	pcrecpp-devel = %{version}-%{release}
Requires:	%{libnamecpp} = %{version}-%{release}
Requires:	%{develname} = %{version}-%{release}
Conflicts:	pcre-devel < 8.32-4

%description -n	%{develcpp}
Install this package if you want do compile applications using the pcrecpp
library.

%package -n	%{develposix}
Group:		Development/C
Summary:	Headers and static lib for pcreposix development
Provides:	pcreposix-devel = %{version}-%{release}
Requires:	%{libnameposix} = %{version}-%{release}
Requires:	%{develname} = %{version}-%{release}
Conflicts:	pcre-devel < 8.32-4

%description -n	%{develposix}
Install this package if you want do compile applications using the pcre
library.

The header file for the POSIX-style functions is called pcreposix.h. The
official POSIX name is regex.h, but I didn't want to risk possible problems
with existing files of that name by distributing it that way. To use it with an
existing program that uses the POSIX API, it will have to be renamed or pointed
at by a link.

%prep
%setup -q
%patch0 -p1 -b .detect-into-kdelibs
%patch1 -p1 -b .linkage-fix
%patch5 -p1 -b .do-not-rely
%patch6 -p1 -b .bad-start
%patch7 -p1 -b .vt-not-included
%patch8 -p1 -b .bad-Qx-compile
%patch9 -p1 -b .empty-matching
%patch10 -p1 -b .memory-leaks
%patch11 -p1 -b .zero-grs
%patch12 -p1 -b .recurse-within

%if %{build_pcreposix_compat}
  # pcre-pcreposix-glibc-conflict patch below breaks compatibility,
  # create a libpcreposix.so.0 without the patch
  cp -a . ../pcre-with-pcreposix_compat && mv ../pcre-with-pcreposix_compat .
%endif
%patch4 -p1 -b .symbol-conflict

%build
%if %{build_pcreposix_compat}
dirs="pcre-with-pcreposix_compat ."
%else
dirs="."
%endif
for i in $dirs; do
  cd $i
  mkdir -p m4
  autoreconf -fi
  %configure2_5x \
	--disable-static \
	--enable-utf \
	--enable-unicode-properties \
	--enable-pcre8 \
	--enable-pcre16 \
	--enable-pcre32 \
	--enable-jit
  %make
  cd -
done

%check
export LC_ALL=C
make check

%install
%if %{build_pcreposix_compat}
%makeinstall_std -C pcre-with-pcreposix_compat
%endif
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/pcre-config

# Remove unwanted files
rm -f %{buildroot}%{_docdir}/pcre/{AUTHORS,ChangeLog,COPYING,LICENCE,NEWS}
rm -f %{buildroot}%{_docdir}/pcre/{pcre-config.txt,pcre.txt,pcregrep.txt}
rm -f %{buildroot}%{_docdir}/pcre/{pcretest.txt,README}
rm -rf %{buildroot}%{_docdir}/pcre/html
rm -f %{buildroot}%{_libdir}/*.la

%files
%doc AUTHORS COPYING LICENCE NEWS README
%{_mandir}/man1/pcregrep.1*
%{_mandir}/man1/pcretest.1*
%{_bindir}/pcregrep  
%{_bindir}/pcretest

%files -n %{libname}
%{_libdir}/libpcre.so.%{pcre_major}*

%files -n %{libname16}
%{_libdir}/libpcre16.so.%{pcrecpp_major}*

%files -n %{libname32}
%{_libdir}/libpcre32.so.%{pcrecpp_major}*

%files -n %{libnamecpp}
%{_libdir}/libpcrecpp.so.%{pcrecpp_major}*

%if %{build_pcreposix_compat}
%files -n %{libnameposix_compat}
%{_libdir}/libpcreposix.so.%{pcreposix_compat_major}*
%endif

%files -n %{libnameposix}
%{_libdir}/libpcreposix.so.%{pcreposix_major}*

%files -n %{develname}
%doc doc/html
%doc ChangeLog 
%{_libdir}/libpcre.so
%{_libdir}/libpcre16.so
%{_libdir}/libpcre32.so
%{_includedir}/pcre.h
%{_includedir}/pcre_*.h
%{_libdir}/pkgconfig/libpcre.pc
%{_libdir}/pkgconfig/libpcre16.pc
%{_libdir}/pkgconfig/libpcre32.pc
%{_bindir}/pcre-config
%multiarch %{multiarch_bindir}/pcre-config
%{_mandir}/man1/pcre-config.1*
%{_mandir}/man3/*.3*
%exclude %{_libdir}/libpcreposix.so
%exclude %{_mandir}/man3/pcreposix.3*

%files -n %{develcpp}
%{_includedir}/pcrecpp*.h
%{_libdir}/libpcrecpp.so
%{_libdir}/pkgconfig/libpcrecpp.pc
%{_mandir}/man3/pcrecpp.3*

%files -n %{develposix}
%{_includedir}/pcreposix.h
%{_libdir}/libpcreposix.so
%{_libdir}/pkgconfig/libpcreposix.pc
%{_mandir}/man3/pcreposix.3*
