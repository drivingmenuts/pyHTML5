import pyhtml5 as h

print(h.DOCTYPE(),
      h.H1("Hello, World!"),
      h.P("This is a paragraph."),
      h.BR(),
      h.MARKDOWN("This is a **markdown** text and an {anchor}.",
                 {"anchor": h.ANCHOR("link", _href="https://example.com")}), )
