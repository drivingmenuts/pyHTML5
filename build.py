import logging
import sys

from rich.logging import RichHandler

logging.basicConfig(level=logging.INFO, handlers=[RichHandler()])
logger = logging.getLogger(__name__)

# Explicit is better than implicit ... sometimes it's painful

# Use for indenting
TAB_WIDTH = 4

DEPRECATED_ELEMENTS = [
    "acronym",
    "applet",
    "basefont",
    "big",
    "center",
    "dir",
    "font",
    "frame",
    "frameset",
    "noframes",
    "s",
    "strike",
    "tt",
    "b",
    "u",
    "i"
]

# from https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes
GLOBAL_ATTRIBUTES = [
    "accesskey",
    "autocapitalize",
    "class",
    "contenteditable",
    "contextmenu",
    "data-*",  # special case (see is_valid_attr)
    "dir",
    "draggable",
    "hidden",
    "id",
    "itemprop",
    "lang",
    "role",
    "slot",
    "spellcheck",
    "style",
    "tabindex",
    "title",
    "translate"
]

# from https://developer.mozilla.org/en-US/docs/Web/HTML/Element
STANDARD_ELEMENTS = {
    "a": [
        "download",
        "href",
        "hreflang",
        "media",
        "ping",
        "referrerpolicy",
        "rel",
        "shape",
        "target"
    ],
    "abbr": [],
    "acronym": [],
    "address": [],
    "applet": [
        "align",
        "alt",
        "code",
        "codebase"
    ],
    "article": [],
    "aside": [],
    "audio": [
        "autoplay",
        "buffered",
        "controls",
        "crossorigin",
        "loop",
        "muted",
        "preload",
        "src"
    ],
    "b": [],
    "basefont": [
        "color"
    ],
    "bdi": [],
    "bdo": [],
    "bgsound": [
        "loop"
    ],
    "big": [],
    "blink": [],
    "blockquote": [
        "cite"
    ],
    "body": [
        "background",
        "bgcolor"
    ],
    "button": [
        "autofocus",
        "disabled",
        "form",
        "formaction",
        "formenctype",
        "formmethod",
        "formnovalidate",
        "formtarget",
        "name",
        "type",
        "value"
    ],
    "canvas": [
        "height",
        "width"
    ],
    "caption": [
        "align"
    ],
    "center": [],
    "cite": [],
    "code": [],
    "colgroup": [
        "align",
        "bgcolor",
        "span"
    ],
    "command": [
        "checked",
        "disabled",
        "icon",
        "radiogroup",
        "type"
    ],
    "content": [],
    "contenteditable": [
        "enterkeyhint",
        "inputmode"
    ],
    "data": [
        "value"
    ],
    "datalist": [],
    "dd": [],
    "del": [
        "cite",
        "datetime"
    ],
    "details": [
        "open"
    ],
    "dfn": [],
    "dialog": [
        "open"
    ],
    "dir": [],
    "div": [],
    "dl": [],
    "dt": [],
    "em": [],
    "fieldset": [
        "disabled",
        "form",
        "name"
    ],
    "figcaption": [],
    "figure": [],
    "font": [
        "color"
    ],
    "footer": [],
    "form": [
        "accept",
        "accept-charset",
        "action",
        "autocomplete",
        "enctype",
        "method",
        "name",
        "novalidate",
        "target"
    ],
    "frame": [],
    "frameset": [],
    "h1": [],
    "h2": [],
    "h3": [],
    "h4": [],
    "h5": [],
    "h6": [],
    "head": [],
    "header": [],
    "hgroup": [],
    "html": [
        "lang",
        "manifest"
    ],
    "i": [],
    "iframe": [
        "align",
        "allow",
        "csp",
        "height",
        "importance",
        "loading",
        "name",
        "referrerpolicy",
        "sandbox",
        "src",
        "srcdoc",
        "width"
    ],
    "image": [],

    "ins": [
        "cite",
        "datetime"
    ],
    "kbd": [],
    "keygen": [
        "autofocus",
        "challenge",
        "disabled",
        "form",
        "keytype",
        "name"
    ],
    "label": [
        "for",
        "form"
    ],
    "legend": [],
    "li": [
        "value"
    ],
    "main": [],
    "map": [
        "name"
    ],
    "mark": [],
    "marquee": [
        "bgcolor",
        "loop"
    ],
    "math": [],
    "menu": [
        "type"
    ],
    "menuitem": [],
    "meter": [
        "form",
        "high",
        "low",
        "max",
        "min",
        "optimum",
        "value"
    ],
    "nav": [],
    "nobr": [],
    "noembed": [],
    "noframes": [],
    "noscript": [],
    "object": [
        "border",
        "data",
        "form",
        "height",
        "name",
        "type",
        "usemap",
        "width"
    ],
    "ol": [
        "reversed",
        "start"
    ],
    "optgroup": [
        "disabled",
        "label"
    ],
    "option": [
        "disabled",
        "label",
        "selected",
        "value"
    ],
    "output": [
        "for",
        "form",
        "name"
    ],
    "p": [],
    "picture": [],
    "plaintext": [],
    "portal": [],
    "pre": [],
    "progress": [
        "form",
        "max",
        "value"
    ],
    "q": [
        "cite"
    ],
    "rb": [],
    "rp": [],
    "rt": [],
    "rtc": [],
    "ruby": [],
    "s": [],
    "samp": [],
    "script": [
        "async",
        "charset",
        "crossorigin",
        "defer",
        "importance",
        "integrity",
        "language",
        "referrerpolicy",
        "src",
        "type"
    ],
    "section": [],
    "select": [
        "autocomplete",
        "autofocus",
        "disabled",
        "form",
        "multiple",
        "name",
        "required",
        "size"
    ],
    "shadow": [],
    "slot": [],
    "small": [],
    "spacer": [],
    "span": [],
    "strike": [],
    "strong": [],
    "style": [
        "media",
        "scoped",
        "type"
    ],
    "sub": [],
    "summary": [],
    "sup": [],
    "svg": [],
    "table": [
        "align",
        "background",
        "bgcolor",
        "border",
        "summary"
    ],
    "tbody": [
        "align",
        "bgcolor"
    ],
    "td": [
        "align",
        "background",
        "bgcolor",
        "colspan",
        "headers",
        "rowspan"
    ],
    "template": [],
    "tfoot": [
        "align",
        "bgcolor"
    ],
    "th": [
        "align",
        "background",
        "bgcolor",
        "colspan",
        "headers",
        "rowspan",
        "scope"
    ],
    "thead": [
        "align"
    ],
    "time": [
        "datetime"
    ],
    "title": [],
    "tr": [
        "align",
        "bgcolor"
    ],
    "tt": [],
    "u": [],
    "ul": [],
    "var": [],
    "video": [
        "autoplay",
        "buffered",
        "controls",
        "crossorigin",
        "height",
        "loop",
        "muted",
        "poster",
        "preload",
        "src",
        "width"
    ],
    "xmp": []
}

# https://developer.mozilla.org/en-US/docs/Web/HTML/Element
EMPTY_ELEMENTS = {
    "area": [
        "alt",
        "coords",
        "download",
        "href",
        "hreflang",
        "media",
        "ping",
        "referrerpolicy",
        "rel",
        "shape",
        "target"
    ],
    "base": [
        "href",
        "target"
    ],
    "br": [],
    "col": [
        "align",
        "bgcolor",
        "span"
    ],
    "embed": [
        "height",
        "src",
        "type",
        "width"
    ],
    "hr": [
        "align",
        "color"
    ],
    "img": [
        "align",
        "alt",
        "border",
        "crossorigin",
        "decoding",
        "height",
        "importance",
        "intrinsicsize",
        "ismap",
        "loading",
        "referrerpolicy",
        "sizes",
        "src",
        "srcset",
        "usemap",
        "width"
    ],
    "input": [
        "accept",
        "alt",
        "autocomplete",
        "autofocus",
        "capture",
        "checked",
        "dirname",
        "disabled",
        "form",
        "formaction",
        "formenctype",
        "formmethod",
        "formnovalidate",
        "formtarget",
        "height",
        "list",
        "max",
        "maxlength",
        "minlength",
        "min",
        "multiple",
        "name",
        "pattern",
        "placeholder",
        "readonly",
        "required",
        "size",
        "src",
        "step",
        "type",
        "usemap",
        "value",
        "width"
    ],
    "link": [
        "crossorigin",
        "href",
        "hreflang",
        "importance",
        "integrity",
        "media",
        "referrerpolicy",
        "rel",
        "sizes",
        "type"
    ],
    "meta": [
        "charset",
        "content",
        "http-equiv",
        "name"
    ],
    "param": [
        "name",
        "value"
    ],
    "source": [
        "media",
        "sizes",
        "src",
        "srcset",
        "type"
    ],
    "track": [
        "default",
        "kind",
        "label",
        "src",
        "srclang"
    ],
    "wbr": [],
}

# These are elements that need special handling.
SPECIAL_ELEMENTS = {
    "anchor": [],
    "comment": [],
    "doctype": [],
    "markdown": [],
    "script": [],
    "textarea": [
        "autocomplete",
        "autofocus",
        "cols",
        "dirname",
        "disabled",
        "enterkeyhint",
        "form",
        "inputmode",
        "maxlength",
        "minlength",
        "name",
        "placeholder",
        "readonly",
        "required",
        "rows",
        "wrap"
    ],
}

# Classes that need to be renamed in the exports list.
RENAMED_EXPORTS = {
    "A": "ANCHOR",
}

# https://developer.mozilla.org/en-US/docs/Web/Events
EVENT_HANDLERS = {
    "Window": [
        "onafterprint",
        "onbeforeprint",
        "onbeforeunload"
        "onerror",
        "onhashchange",
        "onload",
        "onmessage",
        "onoffline",
        "ononline",
        "onpagehide",
        "onpageshow",
        "onpopstate",
        "onresize",
        "onstorage",
        "onunload"
    ],
    "Form": [
        "onblur",
        "onchange",
        "oncontextmenu",
        "onfocus",
        "oninput",
        "oninvalid",
        "onreset",
        "onsearch",
        "onselect",
        "onsubmit"
    ],
    "Keyboard": [
        "onkeydown",
        "onkeypress",
        "onkeyup"
    ],
    "Mouse": [
        "onclick",
        "ondblclick",
        "onmousedown",
        "onmousemove",
        "onmouseout",
        "onmouseover",
        "onmouseup",
        "onmousewheel",
        "onwheel"
    ],
    "Drag": [
        "ondrag",
        "ondragend",
        "ondragenter",
        "ondragleave",
        "ondragover",
        "ondragstart",
        "ondrop",
        "onscroll"
    ],
    "Clipboard": [
        "oncopy",
        "oncut",
        "onpaste"
    ],
    "Media": [
        "onabort",
        "oncanplay",
        "oncanplaythrough",
        "ondurationchange",
        "onemptied",
        "onended",
        "onerror",
        "onloadeddata",
        "onloadedmetadata",
        "onloadstart",
        "onpause",
        "onplay",
        "onplaying",
        "onprogress",
        "onratechange",
        "onseeked",
        "onseeking",
        "onstalled",
        "onsuspend",
        "ontimeupdate",
        "onvolumechange",
        "onwaiting"
    ]
}

ALL = []
ELEMENTS = []


def generator():
    global ALL
    global ELEMENTS

    logger.info("Generating ...")

    ELEMENTS.append("\n\n# Elements")

    logger.info("Standard Elements ...")
    for cname in STANDARD_ELEMENTS.keys():
        if cname in DEPRECATED_ELEMENTS:
            continue
        if cname in SPECIAL_ELEMENTS:
            continue
        if cname.upper() in RENAMED_EXPORTS.keys():
            continue
        class_name = cname.upper()
        class_def = f"class {class_name}(Element): pass"
        ELEMENTS.append(class_def)
        logger.info(ELEMENTS[-1])
        ALL.append(f"'{class_name}'")

    ELEMENTS.append("\n\n# Empty Elements")

    logger.info("Empty Elements ...")
    for cname in EMPTY_ELEMENTS.keys():
        if cname in DEPRECATED_ELEMENTS:
            continue
        if cname in SPECIAL_ELEMENTS:
            continue
        if cname.upper() in RENAMED_EXPORTS.keys():
            continue
        class_name = cname.upper()
        class_def = f"class {class_name}(EmptyElement): pass"
        ELEMENTS.append(class_def)
        logger.info(ELEMENTS[-1])
        ALL.append(f"'{class_name}'")

    ELEMENTS.append("\n# End Generated")

    # Renaming of exports
    logger.info("Renaming Elements ...")
    for c in RENAMED_EXPORTS.keys():
        if c in ALL:
            del ALL[ALL.index(f"'{c.upper()}'")]

    # Renaming of exports
    logger.info("Special Elements ...")
    for c in SPECIAL_ELEMENTS.keys():
        ALL.append(f"'{c.upper()}'")

    # template = ""
    with open("template.py") as f:
        template = f.read()

    spacer = " " * TAB_WIDTH
    _ALL = f",\n{spacer}".join(sorted(ALL))

    template = template.replace("# all", f"__all__ = [\n{spacer}{_ALL}\n]")
    template = template.replace("# elements", "\n".join(ELEMENTS))

    with open("pyhtml5.py", "w") as f:
        f.write(template)

    logger.info("Done!")


if __name__ == "__main__":
    generator()
