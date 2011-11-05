# revision 18292
# category Package
# catalog-ctan /macros/latex/contrib/rotfloat
# catalog-date 2009-10-07 22:25:55 +0200
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-rotfloat
Version:	1.2
Release:	1
Summary:	Rotate floats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rotfloat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rotfloat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rotfloat.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rotfloat.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The float package provides commands to define new floats of
various styles (plain, boxed, ruled, and userdefined ones); the
rotating package provides new environments (sidewaysfigure and
sidewaystable) which are rotated by 90 or 270 degrees. But what
about new rotated floats, e.g. a rotated ruled one? This
package makes this possible; it builds a bridge between the two
packages and extends the commands from the float package to
define rotated versions of the new floats, too.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rotfloat/rotfloat.sty
%doc %{_texmfdistdir}/doc/latex/rotfloat/examples.tex
%doc %{_texmfdistdir}/doc/latex/rotfloat/rotfloat.pdf
#- source
%doc %{_texmfdistdir}/source/latex/rotfloat/rotfloat.dtx
%doc %{_texmfdistdir}/source/latex/rotfloat/rotfloat.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
