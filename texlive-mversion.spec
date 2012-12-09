# revision 24330
# category Package
# catalog-ctan /macros/latex/contrib/mversion
# catalog-date 2011-10-19 16:05:14 +0200
# catalog-license lppl1.2
# catalog-version 1.0
Name:		texlive-mversion
Version:	1.0
Release:	2
Summary:	Keeping track of document versions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mversion
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mversion.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mversion.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mversion.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables the user to keep track of different
versions of a latex document. The command \version prints the
version and build numbers; each time you compile your document,
the build number is increased by one. By placing \version in
the header or footer, each page can be marked with the unique
build number describing the progress of your document.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mversion/mVersion.sty
%doc %{_texmfdistdir}/doc/latex/mversion/README
%doc %{_texmfdistdir}/doc/latex/mversion/mVersion.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mversion/mVersion.dtx
%doc %{_texmfdistdir}/source/latex/mversion/mVersion.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 754240
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719093
- texlive-mversion
- texlive-mversion
- texlive-mversion
- texlive-mversion

