#!/usr/bin/env python3
"""Render the profile heading to assets/heading.svg.

Markdown can't color text, so the heading is an image. Edit LINES below and
re-run:  python3 scripts/gen_heading.py

The font is a stack, not an embedded file — it resolves to whatever monospace
the viewer has. That's how every README SVG does it; the tradeoff is the exact
glyphs differ a little between machines.
"""
from html import escape

LINES = [
    "hey, i'm maxwell",
]

COLOR   = "#8B5CF6"   # violet — holds contrast on GitHub light and dark
SIZE    = 26
LEADING = 40
PAD     = 18
FONT    = ("ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, "
           "'Liberation Mono', monospace")

def build(lines):
    width  = max(len(l) for l in lines) * SIZE * 0.62 + PAD * 2
    height = len(lines) * LEADING + PAD * 2
    rows = "\n".join(
        f'    <tspan x="50%" dy="{0 if i == 0 else LEADING}">{escape(l)}</tspan>'
        for i, l in enumerate(lines)
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}" height="{height:.0f}" viewBox="0 0 {width:.0f} {height:.0f}" role="img" aria-label="{escape(' / '.join(lines))}">
  <text x="50%" y="{PAD + SIZE}" text-anchor="middle" fill="{COLOR}"
        font-family="{FONT}" font-size="{SIZE}" font-weight="500">
{rows}
  </text>
</svg>
'''

if __name__ == "__main__":
    import pathlib
    out = pathlib.Path(__file__).resolve().parent.parent / "assets" / "heading.svg"
    out.parent.mkdir(exist_ok=True)
    out.write_text(build(LINES))
    print(f"wrote {out} ({out.stat().st_size} bytes)")
