"""Outline the QUADRANT wordmark (Jost 400, tracked +0.16em) into SVG path data.

One-time asset step: the output (wordmark.json) is committed, so the main
build (build.py) needs only the standard library.

Usage:
    pip install fonttools
    python outline_wordmark.py path/to/Jost-400.ttf > wordmark.json

Get the TTF from Google Fonts (https://fonts.google.com/specimen/Jost).
Coordinates are in units where the font size is 1000, y pointing down,
baseline at y = cap height (so cap tops sit at y = 0). `bounds` is the
real ink box [x_min, y_min, x_max, y_max]; the Q's tail drops below the baseline.
"""

import json
import sys

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

TEXT = "QUADRANT"
TRACKING = 0.16  # em


def main(ttf_path: str) -> None:
    font = TTFont(ttf_path)
    upm = font["head"].unitsPerEm
    scale = 1000 / upm
    cap = font["OS/2"].sCapHeight * scale
    cmap = font.getBestCmap()
    glyphs = font.getGlyphSet()
    hmtx = font["hmtx"]

    svg_pen = SVGPathPen(glyphs, ntos=lambda n: f"{n:.1f}".rstrip("0").rstrip("."))
    bounds = BoundsPen(glyphs)
    x = 0.0
    for i, ch in enumerate(TEXT):
        name = cmap[ord(ch)]
        # flip y and move baseline down to the cap height
        pen = TransformPen(svg_pen, (scale, 0, 0, -scale, x, cap))
        glyphs[name].draw(pen)
        glyphs[name].draw(TransformPen(bounds, (scale, 0, 0, -scale, x, cap)))
        x += hmtx[name][0] * scale
        if i < len(TEXT) - 1:
            x += TRACKING * 1000

    x_min, y_min, x_max, y_max = bounds.bounds

    json.dump(
        {
            "text": TEXT,
            "font": "Jost 400",
            "tracking_em": TRACKING,
            "cap_height": round(cap, 1),
            "bounds": [round(v, 1) for v in (x_min, y_min, x_max, y_max)],
            "d": svg_pen.getCommands(),
        },
        sys.stdout,
        indent=2,
    )
    sys.stdout.write("\n")


if __name__ == "__main__":
    main(sys.argv[1])
