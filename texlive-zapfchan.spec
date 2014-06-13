# revision 31835
# category Package
# catalog-ctan /fonts/urw/base35
# catalog-date 2012-06-06 22:57:48 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-zapfchan
Version:	20120606
Release:	6
Summary:	URW "Base 35" font pack for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/urw/base35
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zapfchan.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: - Century Schoolbook (substituting for
Adobe's New Century Schoolbook); - Dingbats (substituting for
Adobe's Zapf Dingbats); - Nimbus Mono L (substituting for
Abobe's Courier); - Nimbus Roman No9 L (substituting for
Adobe's Times); - Nimbus Sans L (substituting for Adobe's
Helvetica); - Standard Symbols L (substituting for Adobe's
Symbol); - URW Bookman; - URW Chancery L Medium Italic
(substituting for Adobe's Zapf Chancery); - URW Gothic L Book
(substituting for Adobe's Avant Garde); and - URW Palladio L
(substituting for Adobe's Palatino).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/zapfchan/config.uzc
%{_texmfdistdir}/fonts/afm/adobe/zapfchan/pzcmi8a.afm
%{_texmfdistdir}/fonts/afm/urw/zapfchan/uzcmi8a.afm
%{_texmfdistdir}/fonts/map/dvips/zapfchan/uzc.map
%{_texmfdistdir}/fonts/tfm/adobe/zapfchan/pzcmi.tfm
%{_texmfdistdir}/fonts/tfm/adobe/zapfchan/pzcmi7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/zapfchan/pzcmi8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/zapfchan/pzcmi8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/zapfchan/pzcmi8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/zapfchan/uzcmi7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/zapfchan/uzcmi8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/zapfchan/uzcmi8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/zapfchan/uzcmi8t.tfm
%{_texmfdistdir}/fonts/type1/urw/zapfchan/uzcmi8a.pfb
%{_texmfdistdir}/fonts/type1/urw/zapfchan/uzcmi8a.pfm
%{_texmfdistdir}/fonts/vf/adobe/zapfchan/pzcmi.vf
%{_texmfdistdir}/fonts/vf/adobe/zapfchan/pzcmi7t.vf
%{_texmfdistdir}/fonts/vf/adobe/zapfchan/pzcmi8c.vf
%{_texmfdistdir}/fonts/vf/adobe/zapfchan/pzcmi8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/zapfchan/uzcmi7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/zapfchan/uzcmi8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/zapfchan/uzcmi8t.vf
%{_texmfdistdir}/tex/latex/zapfchan/8ruzc.fd
%{_texmfdistdir}/tex/latex/zapfchan/omluzc.fd
%{_texmfdistdir}/tex/latex/zapfchan/omsuzc.fd
%{_texmfdistdir}/tex/latex/zapfchan/ot1uzc.fd
%{_texmfdistdir}/tex/latex/zapfchan/t1uzc.fd
%{_texmfdistdir}/tex/latex/zapfchan/ts1uzc.fd

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts tex %{buildroot}%{_texmfdistdir}
