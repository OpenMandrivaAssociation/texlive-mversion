%global tl_name mversion
%global tl_revision 29370

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	Keeping track of document versions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mversion
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mversion.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mversion.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mversion.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package enables the user to keep track of different versions of a
LaTeX document. The command \version prints the version and build
numbers; each time you compile your document, the build number is
increased by one. By placing \version in the header or footer, each page
can be marked with the unique build number describing the progress of
your document.

