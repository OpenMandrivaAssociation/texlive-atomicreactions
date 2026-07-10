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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Simple representation of atomic shell reactions like direct ionisation
or excitation-autoionisation. It also provides a low-level Bohr model
illustration.

