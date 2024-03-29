from core import *


# Generated by build.py\n#

# @formatter:off
__all__ = [
    'ABBR',
    'ADDRESS',
    'ANCHOR',
    'AREA',
    'ARTICLE',
    'ASIDE',
    'AUDIO',
    'BASE',
    'BDI',
    'BDO',
    'BGSOUND',
    'BLINK',
    'BLOCKQUOTE',
    'BODY',
    'BR',
    'BUTTON',
    'CANVAS',
    'CAPTION',
    'CITE',
    'CODE',
    'COL',
    'COLGROUP',
    'COMMAND',
    'COMMENT',
    'CONTENT',
    'CONTENTEDITABLE',
    'DATA',
    'DATALIST',
    'DD',
    'DEL',
    'DETAILS',
    'DFN',
    'DIALOG',
    'DIV',
    'DL',
    'DOCTYPE',
    'DT',
    'EM',
    'EMBED',
    'FIELDSET',
    'FIGCAPTION',
    'FIGURE',
    'FOOTER',
    'FORM',
    'H1',
    'H2',
    'H3',
    'H4',
    'H5',
    'H6',
    'HEAD',
    'HEADER',
    'HGROUP',
    'HR',
    'HTML',
    'IFRAME',
    'IMAGE',
    'IMG',
    'INPUT',
    'INS',
    'KBD',
    'KEYGEN',
    'LABEL',
    'LEGEND',
    'LI',
    'LINK',
    'MAIN',
    'MAP',
    'MARK',
    'MARKDOWN',
    'MARQUEE',
    'MATH',
    'MENU',
    'MENUITEM',
    'META',
    'METER',
    'NAV',
    'NOBR',
    'NOEMBED',
    'NOSCRIPT',
    'OBJECT',
    'OL',
    'OPTGROUP',
    'OPTION',
    'OUTPUT',
    'P',
    'PARAM',
    'PICTURE',
    'PLAINTEXT',
    'PORTAL',
    'PRE',
    'PROGRESS',
    'Q',
    'RB',
    'RP',
    'RT',
    'RTC',
    'RUBY',
    'SAMP',
    'SCRIPT',
    'SECTION',
    'SELECT',
    'SHADOW',
    'SLOT',
    'SMALL',
    'SOURCE',
    'SPACER',
    'SPAN',
    'STRONG',
    'STYLE',
    'SUB',
    'SUMMARY',
    'SUP',
    'SVG',
    'TABLE',
    'TBODY',
    'TD',
    'TEMPLATE',
    'TEXTAREA',
    'TFOOT',
    'TH',
    'THEAD',
    'TIME',
    'TITLE',
    'TR',
    'TRACK',
    'UL',
    'VAR',
    'VIDEO',
    'WBR',
    'XMP'
]
# @formatter:on

# @formatter:off


# Elements
class ABBR(Element): pass
class ADDRESS(Element): pass
class ARTICLE(Element): pass
class ASIDE(Element): pass
class AUDIO(Element): pass
class BDI(Element): pass
class BDO(Element): pass
class BGSOUND(Element): pass
class BLINK(Element): pass
class BLOCKQUOTE(Element): pass
class BODY(Element): pass
class BUTTON(Element): pass
class CANVAS(Element): pass
class CAPTION(Element): pass
class CITE(Element): pass
class CODE(Element): pass
class COLGROUP(Element): pass
class COMMAND(Element): pass
class CONTENT(Element): pass
class CONTENTEDITABLE(Element): pass
class DATA(Element): pass
class DATALIST(Element): pass
class DD(Element): pass
class DEL(Element): pass
class DETAILS(Element): pass
class DFN(Element): pass
class DIALOG(Element): pass
class DIV(Element): pass
class DL(Element): pass
class DT(Element): pass
class EM(Element): pass
class FIELDSET(Element): pass
class FIGCAPTION(Element): pass
class FIGURE(Element): pass
class FOOTER(Element): pass
class FORM(Element): pass
class H1(Element): pass
class H2(Element): pass
class H3(Element): pass
class H4(Element): pass
class H5(Element): pass
class H6(Element): pass
class HEAD(Element): pass
class HEADER(Element): pass
class HGROUP(Element): pass
class HTML(Element): pass
class IFRAME(Element): pass
class IMAGE(Element): pass
class INS(Element): pass
class KBD(Element): pass
class KEYGEN(Element): pass
class LABEL(Element): pass
class LEGEND(Element): pass
class LI(Element): pass
class MAIN(Element): pass
class MAP(Element): pass
class MARK(Element): pass
class MARQUEE(Element): pass
class MATH(Element): pass
class MENU(Element): pass
class MENUITEM(Element): pass
class METER(Element): pass
class NAV(Element): pass
class NOBR(Element): pass
class NOEMBED(Element): pass
class NOSCRIPT(Element): pass
class OBJECT(Element): pass
class OL(Element): pass
class OPTGROUP(Element): pass
class OPTION(Element): pass
class OUTPUT(Element): pass
class P(Element): pass
class PICTURE(Element): pass
class PLAINTEXT(Element): pass
class PORTAL(Element): pass
class PRE(Element): pass
class PROGRESS(Element): pass
class Q(Element): pass
class RB(Element): pass
class RP(Element): pass
class RT(Element): pass
class RTC(Element): pass
class RUBY(Element): pass
class SAMP(Element): pass
class SECTION(Element): pass
class SELECT(Element): pass
class SHADOW(Element): pass
class SLOT(Element): pass
class SMALL(Element): pass
class SPACER(Element): pass
class SPAN(Element): pass
class STRONG(Element): pass
class STYLE(Element): pass
class SUB(Element): pass
class SUMMARY(Element): pass
class SUP(Element): pass
class SVG(Element): pass
class TABLE(Element): pass
class TBODY(Element): pass
class TD(Element): pass
class TEMPLATE(Element): pass
class TFOOT(Element): pass
class TH(Element): pass
class THEAD(Element): pass
class TIME(Element): pass
class TITLE(Element): pass
class TR(Element): pass
class UL(Element): pass
class VAR(Element): pass
class VIDEO(Element): pass
class XMP(Element): pass


# Empty Elements
class AREA(EmptyElement): pass
class BASE(EmptyElement): pass
class BR(EmptyElement): pass
class COL(EmptyElement): pass
class EMBED(EmptyElement): pass
class HR(EmptyElement): pass
class IMG(EmptyElement): pass
class INPUT(EmptyElement): pass
class LINK(EmptyElement): pass
class META(EmptyElement): pass
class PARAM(EmptyElement): pass
class SOURCE(EmptyElement): pass
class TRACK(EmptyElement): pass
class WBR(EmptyElement): pass

# End Generated
# @formatter:on


# Predefined elements
# noinspection DuplicatedCode
class ANCHOR(Element):
    def __init__(self, *children, **attributes):
        super().__init__(*children, **attributes)
        self._tag = "a"


# noinspection DuplicatedCode
class DOCTYPE:
    def __init__(self, document_type: str = "html"):
        """Returns a DOCTYPE element. Currently, only supports html."""
        self.document_type = document_type

    def __str__(self):
        return f"<!DOCTYPE {self.document_type}>"


# noinspection DuplicatedCode
class COMMENT:
    """Returns an html comment."""

    def __init__(self, text: str):
        self.text = text

    def __str__(self):
        return f"<!-- {self.text} -->"


# @formatter:off
class MARKDOWN(Text): pass
# @formatter:on


# noinspection DuplicatedCode
class TEXTAREA(Element):
    """Returns a textarea element. It uses the same attributes as a <input type="textarea">"""

    def __str__(self):
        properties = self._attributes
        content = properties["_value"] if "_value" in properties.keys() else ""
        if "_value" in self._attributes.keys():
            del self._attributes["_value"]
        return f"<textarea{core.mk_props(self._attributes)}>{content}</textarea>"
