Name:		texlive-mversion
Version:	29370
Release:	1
Summary:	Keeping track of document versions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mversion
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mversion.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mversion.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mversion.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
