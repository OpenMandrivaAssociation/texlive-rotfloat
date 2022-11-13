Name:		texlive-rotfloat
Version:	18292
Release:	1
Summary:	Rotate floats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rotfloat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rotfloat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rotfloat.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rotfloat.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The float package provides commands to define new floats of
various styles (plain, boxed, ruled, and userdefined ones); the
rotating package provides new environments (sidewaysfigure and
sidewaystable) which are rotated by 90 or 270 degrees. But what
about new rotated floats, e.g. a rotated ruled one? This
package makes this possible; it builds a bridge between the two
packages and extends the commands from the float package to
define rotated versions of the new floats, too.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rotfloat/rotfloat.sty
%doc %{_texmfdistdir}/doc/latex/rotfloat/examples.tex
%doc %{_texmfdistdir}/doc/latex/rotfloat/rotfloat.pdf
#- source
%doc %{_texmfdistdir}/source/latex/rotfloat/rotfloat.dtx
%doc %{_texmfdistdir}/source/latex/rotfloat/rotfloat.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
