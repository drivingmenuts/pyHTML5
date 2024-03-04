import logging
import markdown

logger = logging.getLogger(__name__)

__all__ = [
    "clean_attribute",
    "mk_props",
    "Node",
    "Element",
    "EmptyElement",
    "Text",
]


def clean_attribute(attribute: str,
                    lowercase_props: bool = True,
                    allow_underscore: bool = True) -> str:
    """The leading underscore is required to prevent collision with reserved words.."""
    attribute = attribute[1:] if attribute[:1] == "_" else attribute

    """clean an attribute name"""
    if lowercase_props:
        attribute = attribute.lower()
    if not allow_underscore:
        attribute = attribute.replace("_", "")
    return attribute


def mk_props(properties: dict) -> str:
    """build a properties string"""
    if len(properties):
        plist = []
        for key in properties.keys():
            value = properties[key]
            plist.append(f'{clean_attribute(key)}="{value}"')
        return " " + " ".join(plist)
    else:
        return ""


class Node:
    """create a node"""
    _tag = None
    _children = []
    _attributes = {}

    def __init__(self, *children, **attributes):
        self._tag = "?"
        self._children = children
        logger.debug(f"{attributes.keys()}")
        for k in attributes.keys():
            if k[:1] != "_":
                raise ValueError(f"Invalid attribute/event name: '{k}' should be '_{k}'.")
        self._attributes = attributes

    @property
    def _content(self):
        return "".join(str(c) for c in self._children)

    def __str__(self) -> str:
        return f"<{self._tag}{mk_props(self._attributes)}>{self._content}</{self._tag}>"


class Element(Node):
    """create an element node"""

    def __init__(self, *children, **attributes):
        super().__init__(*children, **attributes)
        self._tag = self.__class__.__name__.lower()


class EmptyElement(Element):
    """create an empty element node"""

    def __str__(self) -> str:
        return f"<{self._tag.lower()}{mk_props(self._attributes)} />"


# Not exported - not used by the template
class Doctype(Node):
    """create a doctype node"""

    def __str__(self) -> str:
        return "<!DOCTYPE html>"


# Not exported - not used by the template
class Comment(Node):
    """create a comment node"""

    def __str__(self):
        return f"<!-- {str(self._children[0])} -->"


class Text:
    """create a text node"""
    _template = None
    _entries = {}

    def __init__(self, template, entries=None):
        self._template = template
        self._entries = entries

    def __str__(self):
        for k, v in self._entries.items():
            self._template = self._template.replace(f"{{{k}}}", str(v))
        return markdown.markdown(self._template)


if __name__ == "__main__":
    # @formatter:off
    class P(Element): pass
    class BR(EmptyElement): pass
    # @formatter:on

    print(Doctype())
    print(Comment("This is a comment"))
    print(P("This is a paragraph", _style="color:red; font-size:20px;", _id="p1"))
    print(BR(_class="br"))
    print(Text("{name} is {age} *years* \{old\}.", {"name": "John", "age": 30}))
