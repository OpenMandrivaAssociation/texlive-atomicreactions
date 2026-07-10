%global tl_name atomicreactions
%global tl_revision 79355

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	Simple representation of atomic shell reactions and Bohr model
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/atomicreactions
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/atomicreactions.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/atomicreactions.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Simple representation of atomic shell reactions like direct ionisation
or excitation-autoionisation. It also provides a low-level Bohr model
illustration.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/atomicreactions
%dir %{_datadir}/texmf-dist/tex/latex/atomicreactions
%doc %{_datadir}/texmf-dist/doc/latex/atomicreactions/README.md
%doc %{_datadir}/texmf-dist/doc/latex/atomicreactions/atomicreactions-manual.pdf
%doc %{_datadir}/texmf-dist/doc/latex/atomicreactions/atomicreactions-manual.tex
%doc %{_datadir}/texmf-dist/doc/latex/atomicreactions/atomicreactions.bib
%{_datadir}/texmf-dist/tex/latex/atomicreactions/atomicreactions.sty
