"""Generate the hand-drawn SVG assets used by the profile README.

Text is converted to glyph outlines (Caveat + Patrick Hand, both OFL) so the
SVGs render identically everywhere, with no web fonts to load. Run:

    pip install fonttools uharfbuzz
    python scripts/generate.py
"""

import io
import math
import random
import urllib.request
from pathlib import Path

import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
FONT_DIR = ROOT / ".fonts"
FONT_URLS = {
    "Caveat.ttf": "https://github.com/google/fonts/raw/main/ofl/caveat/Caveat%5Bwght%5D.ttf",
    "PatrickHand.ttf": "https://github.com/google/fonts/raw/main/ofl/patrickhand/PatrickHand-Regular.ttf",
}

INK = "#2B2A35"
SOFT_INK = "#5B5A68"
PURPLE = "#6D28D9"
RED_PEN = "#DC2626"
GREEN_PEN = "#15803D"
AMBER_PEN = "#B45309"
BLUE_PEN = "#1D4ED8"
PAPER = "#FFFDF6"
RULE = "#CFE0F5"
MARGIN = "#F3A6A6"
TAPE = "#EADFC0"


# --------------------------------------------------------------------------- fonts

def font_path(name):
    path = FONT_DIR / name
    if not path.exists():
        FONT_DIR.mkdir(exist_ok=True)
        urllib.request.urlretrieve(FONT_URLS[name], path)
    return path


class Font:
    def __init__(self, key, file, wght=None):
        tt = TTFont(font_path(file))
        if wght is not None:
            tt = instancer.instantiateVariableFont(tt, {"wght": wght})
        buf = io.BytesIO()
        tt.save(buf)
        data = buf.getvalue()
        self.key = key
        self.tt = TTFont(io.BytesIO(data))
        self.upm = self.tt["head"].unitsPerEm
        self.glyphs = self.tt.getGlyphSet()
        self.order = self.tt.getGlyphOrder()
        self.hb = hb.Font(hb.Face(hb.Blob(data)))

    def shape(self, text):
        buf = hb.Buffer()
        buf.add_str(text)
        buf.guess_segment_properties()
        hb.shape(self.hb, buf, {"kern": True, "liga": True})
        return [
            (self.order[info.codepoint], pos.x_advance, pos.x_offset, pos.y_offset)
            for info, pos in zip(buf.glyph_infos, buf.glyph_positions)
        ]

    def width(self, text, size):
        return sum(g[1] for g in self.shape(text)) * size / self.upm

    def outline(self, name):
        pen = SVGPathPen(self.glyphs, ntos=lambda v: str(round(v)))
        self.glyphs[name].draw(pen)
        return pen.getCommands()


HAND = Font("cv", "Caveat.ttf", wght=700)
HAND_REG = Font("cr", "Caveat.ttf", wght=500)
PRINT = Font("ph", "PatrickHand.ttf")


def wrap(font, text, size, max_width):
    lines, line = [], ""
    for word in text.split():
        trial = f"{line} {word}".strip()
        if line and font.width(trial, size) > max_width:
            lines.append(line)
            line = word
        else:
            line = trial
    if line:
        lines.append(line)
    return lines


# --------------------------------------------------------------------------- svg document

class Svg:
    def __init__(self, w, h, title, seed=7):
        self.w, self.h, self.title = w, h, title
        self.defs, self.body, self.glyph_ids = [], [], set()
        self.rand = random.Random(seed)
        self.uid = 0

    def next_id(self, prefix):
        self.uid += 1
        return f"{prefix}{self.uid}"

    def add(self, s):
        self.body.append(s)

    def j(self, amount):
        return self.rand.uniform(-amount, amount)

    # ---- text -------------------------------------------------------------
    def text(self, font, s, x, y, size, fill=INK, anchor="start", reveal=None, extra=""):
        """Draw text as glyph outlines. Returns the drawn width.

        reveal=(begin, dur) wipes the text in from left to right like it is being written.
        """
        width = font.width(s, size)
        if anchor == "middle":
            x -= width / 2
        elif anchor == "end":
            x -= width
        scale = size / font.upm
        uses, pen = [], 0
        for name, adv, xo, yo in font.shape(s):
            gid = f"{font.key}-{name}"
            if gid not in self.glyph_ids:
                d = font.outline(name)
                if d:
                    self.defs.append(f'<path id="{gid}" d="{d}"/>')
                self.glyph_ids.add(gid)
                if not d:
                    self.glyph_ids.add(gid + "!empty")
            if gid + "!empty" not in self.glyph_ids:
                uses.append(f'<use href="#{gid}" x="{pen + xo}" y="{yo}"/>')
            pen += adv
        group = (
            f'<g fill="{fill}" transform="translate({x:.1f} {y:.1f}) scale({scale:.5f} {-scale:.5f})"{extra}>'
            + "".join(uses)
            + "</g>"
        )
        if reveal:
            cid = self.next_id("clip")
            begin, dur = reveal
            total = begin + dur
            k = begin / total
            pad = size * 0.6
            rw = width + 2 * pad
            self.defs.append(
                f'<clipPath id="{cid}"><rect x="{x - pad:.1f}" y="{y - size * 1.4:.1f}" width="{rw:.1f}" height="{size * 2:.1f}">'
                f'<animate attributeName="width" values="0;0;{rw:.1f}" keyTimes="0;{k:.3f};1" dur="{total}s" fill="freeze"/>'
                f"</rect></clipPath>"
            )
            group = f'<g clip-path="url(#{cid})">{group}</g>'
        self.add(group)
        return width

    # ---- strokes ------------------------------------------------------------
    def stroke(self, d, color=INK, width=3, opacity=1, draw=None, cap="round"):
        """A pen stroke. draw=(begin, dur) animates it being drawn."""
        anim = ""
        dash = ""
        if draw:
            begin, dur = draw
            total = begin + dur
            k = begin / total
            dash = ' pathLength="1" stroke-dasharray="1 1"'
            anim = (
                f'<animate attributeName="stroke-dashoffset" values="1;1;0" keyTimes="0;{k:.3f};1" '
                f'dur="{total}s" fill="freeze"/>'
            )
        self.add(
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="{cap}" '
            f'stroke-linejoin="round" opacity="{opacity}"{dash}>{anim}</path>'
        )

    def rough_line_d(self, x1, y1, x2, y2, wobble=2.0):
        mx, my = (x1 + x2) / 2 + self.j(wobble), (y1 + y2) / 2 + self.j(wobble)
        return (
            f"M{x1 + self.j(wobble / 2):.1f} {y1 + self.j(wobble / 2):.1f} "
            f"Q{mx:.1f} {my:.1f} {x2 + self.j(wobble / 2):.1f} {y2 + self.j(wobble / 2):.1f}"
        )

    def rough_rect(self, x, y, w, h, color=INK, width=2.2, passes=2, wobble=2.5, fill=None, draw=None):
        if fill:
            self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{fill}"/>')
        for _ in range(passes):
            d = " ".join(
                [
                    self.rough_line_d(x, y, x + w, y, wobble),
                    self.rough_line_d(x + w, y, x + w, y + h, wobble),
                    self.rough_line_d(x + w, y + h, x, y + h, wobble),
                    self.rough_line_d(x, y + h, x, y, wobble),
                ]
            )
            self.stroke(d, color, width, opacity=0.9, draw=draw)

    def rough_ellipse(self, cx, cy, rx, ry, color=PURPLE, width=3, draw=None):
        pts = []
        start = self.rand.uniform(0, math.tau)
        steps = 28
        for i in range(steps + 4):  # overshoot so the loop doesn't quite close
            t = start + i / steps * math.tau * 1.08
            grow = 1 + 0.04 * i / steps
            pts.append(
                (cx + rx * grow * math.cos(t) + self.j(1.5), cy + ry * grow * math.sin(t) + self.j(1.5))
            )
        self.stroke(smooth(pts), color, width, draw=draw)

    def underline(self, x, y, w, color=PURPLE, width=4, waves=None, amp=3, draw=None):
        waves = waves or max(2, int(w / 60))
        pts = [
            (x + w * i / (waves * 4), y + amp * math.sin(i / 4 * math.tau) * 0.5 + self.j(1) + i * 0.15)
            for i in range(waves * 4 + 1)
        ]
        self.stroke(smooth(pts), color, width, draw=draw)

    def highlight(self, x, y, w, size, color="#FDE68A", draw=None):
        # two overlapping marker passes
        h = size * 0.55
        d = (
            f"M{x - 4:.1f} {y - h * 0.45:.1f} L{x + w + 4:.1f} {y - h * 0.5 + self.j(2):.1f} "
            f"M{x + w:.1f} {y - h * 0.25:.1f} L{x - 2:.1f} {y - h * 0.2 + self.j(2):.1f}"
        )
        self.stroke(d, color, h * 0.75, opacity=0.85, draw=draw, cap="butt")

    def arrow(self, x1, y1, x2, y2, color=PURPLE, width=3, bend=0.25, draw=None):
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        dx, dy = x2 - x1, y2 - y1
        cx, cy = mx - dy * bend, my + dx * bend
        ang = math.atan2(y2 - cy, x2 - cx)
        head = 14
        a1, a2 = ang + math.radians(150), ang - math.radians(150)
        d = (
            f"M{x1:.1f} {y1:.1f} Q{cx:.1f} {cy:.1f} {x2:.1f} {y2:.1f} "
            f"M{x2 + head * math.cos(a1):.1f} {y2 + head * math.sin(a1):.1f} L{x2:.1f} {y2:.1f} "
            f"L{x2 + head * math.cos(a2):.1f} {y2 + head * math.sin(a2):.1f}"
        )
        self.stroke(d, color, width, draw=draw)

    def check(self, x, y, s=22, color=GREEN_PEN, draw=None):
        d = f"M{x:.1f} {y + s * 0.5:.1f} Q{x + s * 0.25:.1f} {y + s * 0.7:.1f} {x + s * 0.38:.1f} {y + s:.1f} Q{x + s * 0.6:.1f} {y + s * 0.3:.1f} {x + s * 1.15:.1f} {y - s * 0.15:.1f}"
        self.stroke(d, color, 4, draw=draw)

    def tape(self, cx, cy, w, h, angle):
        pts = []
        teeth = 5
        for i in range(teeth + 1):  # left torn edge
            pts.append((-w / 2 + (3 if i % 2 else -3), -h / 2 + h * i / teeth))
        for i in range(teeth + 1):  # right torn edge
            pts.append((w / 2 + (3 if i % 2 else -3), h / 2 - h * i / teeth))
        poly = " ".join(f"{px:.1f},{py:.1f}" for px, py in pts)
        self.add(
            f'<g transform="translate({cx} {cy}) rotate({angle})">'
            f'<polygon points="{poly}" fill="{TAPE}" opacity="0.82"/>'
            f'<polygon points="{poly}" fill="url(#tapeLines)" opacity="0.35"/></g>'
        )

    def pin(self, cx, cy, color="#E11D48"):
        self.add(
            f'<g filter="url(#shadow)"><circle cx="{cx}" cy="{cy}" r="11" fill="{color}"/>'
            f'<circle cx="{cx - 3.5}" cy="{cy - 3.5}" r="3.5" fill="#fff" opacity="0.55"/></g>'
        )

    # ---- output -------------------------------------------------------------
    def save(self, name):
        common = (
            '<filter id="shadow" x="-10%" y="-10%" width="120%" height="130%">'
            '<feDropShadow dx="2" dy="5" stdDeviation="5" flood-color="#000" flood-opacity="0.22"/></filter>'
            '<pattern id="tapeLines" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(70)">'
            '<line x1="0" y1="0" x2="0" y2="6" stroke="#fff" stroke-width="2"/></pattern>'
        )
        svg = (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}" '
            f'role="img" aria-label="{escape(self.title)}"><title>{escape(self.title)}</title>'
            f"<defs>{common}{''.join(self.defs)}</defs>{''.join(self.body)}</svg>"
        )
        ASSETS.mkdir(exist_ok=True)
        (ASSETS / name).write_text(svg)
        print(f"{name:28} {len(svg) / 1024:6.1f} KB")


def smooth(pts):
    d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
    for i in range(1, len(pts) - 1):
        mx, my = (pts[i][0] + pts[i + 1][0]) / 2, (pts[i][1] + pts[i + 1][1]) / 2
        d += f" Q{pts[i][0]:.1f} {pts[i][1]:.1f} {mx:.1f} {my:.1f}"
    d += f" L{pts[-1][0]:.1f} {pts[-1][1]:.1f}"
    return d


def escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace('"', "&quot;")


def paper_lines(svg, x, y, w, h, first, step, margin=None, color=RULE):
    lines = "".join(
        f'<line x1="{x}" y1="{ly}" x2="{x + w}" y2="{ly}"/>' for ly in range(first, int(y + h) - 6, step)
    )
    svg.add(f'<g stroke="{color}" stroke-width="1.5">{lines}</g>')
    if margin:
        svg.add(f'<line x1="{margin}" y1="{y}" x2="{margin}" y2="{y + h}" stroke="{MARGIN}" stroke-width="2"/>')


# --------------------------------------------------------------------------- assets

def header():
    s = Svg(1000, 450, "Hey, I'm Yash. Student and indie developer from New Delhi, India. "
            "I build native Mac and iPhone apps, and tools for AI coding agents. Now shipping: ZenVoice.")
    px, py, pw, ph = 30, 28, 940, 392
    hole_mask = "".join(f'<circle cx="74" cy="{cy}" r="13" fill="#000"/>' for cy in (120, 224, 328))
    s.defs.append(
        f'<mask id="holes"><rect x="0" y="0" width="1000" height="450" fill="#fff"/>{hole_mask}</mask>'
    )
    s.add(f'<g transform="rotate(-0.7 500 225)"><g mask="url(#holes)" filter="url(#shadow)">')
    s.add(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="3" fill="{PAPER}"/>')
    paper_lines(s, px, py, pw, ph, first=176, step=36, margin=124)
    s.add("</g>")

    s.tape(500, 30, 150, 38, -3)

    # title
    tx = 156
    hey = "Hey, I'm "
    w1 = s.text(HAND, hey, tx, 140, 104, INK, reveal=(0.2, 0.9))
    w2 = s.text(HAND, "Yash", tx + w1, 140, 104, PURPLE, reveal=(1.1, 0.6))
    s.underline(tx + w1 - 4, 158, w2 + 14, PURPLE, 6, waves=3, amp=4, draw=(1.7, 0.5))
    ex = tx + w1 + w2 + 26  # little sparkle doodle
    for ang, ln in ((-60, 22), (-20, 26), (20, 20)):
        a = math.radians(ang)
        s.stroke(f"M{ex + 10 * math.cos(a):.1f} {80 + 10 * math.sin(a):.1f} L{ex + ln * 1.6 * math.cos(a):.1f} {80 + ln * 1.6 * math.sin(a):.1f}",
                 PURPLE, 4, draw=(2.0, 0.3))

    s.text(PRINT, "student  ·  indie developer  ·  New Delhi, India", tx, 208, 31, SOFT_INK, reveal=(2.1, 0.8))

    pre = "I build "
    hl = "native Mac & iPhone apps"
    x0 = tx + PRINT.width(pre, 34)
    s.highlight(x0, 278, PRINT.width(hl, 34), 34, draw=(3.0, 0.5))
    s.text(PRINT, pre + hl + ",", tx, 278, 34, INK, reveal=(2.8, 0.9))
    pre2 = "and tools for "
    circ = "AI coding agents"
    s.text(PRINT, pre2 + circ + ".", tx, 314, 34, INK, reveal=(3.6, 0.8))
    cw = PRINT.width(circ, 34)
    cx0 = tx + PRINT.width(pre2, 34)
    s.rough_ellipse(cx0 + cw / 2 + 2, 302, cw / 2 + 9, 23, PURPLE, 3, draw=(4.4, 0.6))

    s.text(HAND_REG, "~ local-first, private by default ~", tx, 386, 30, SOFT_INK, reveal=(4.9, 0.7))
    s.add("</g>")

    # sticky note: now shipping
    s.add('<g transform="rotate(5 830 300)" filter="url(#shadow)">')
    s.add('<rect x="720" y="214" width="220" height="176" fill="#FFF4A3"/>')
    s.add('<path d="M720 390 L940 390 L940 372 Q900 392 720 390 Z" fill="#000" opacity="0.04"/>')
    s.add("</g>")
    s.add('<g transform="rotate(5 830 300)">')
    s.text(HAND_REG, "now shipping:", 742, 258, 32, SOFT_INK)
    zw = s.text(HAND, "ZenVoice", 742, 318, 56, PURPLE)
    s.check(742 + zw + 14, 284, 24, GREEN_PEN, draw=(5.4, 0.4))
    s.text(PRINT, "getzenvoice.com", 742, 360, 23, INK)
    s.add("</g>")
    s.pin(828, 222)
    s.text(HAND_REG, "go try it!", 770, 150, 32, PURPLE, reveal=(5.6, 0.4))
    s.arrow(885, 140, 905, 214, PURPLE, 3, bend=-0.3, draw=(5.9, 0.4))
    s.save("header.svg")


def heading(name, label, angle=-1.5):
    size = 46
    tw = HAND.width(label, size)
    w, h = int(tw + 90), 92
    s = Svg(w, h, label, seed=len(label))
    s.add(f'<g filter="url(#shadow)">')
    s.tape(w / 2, h / 2, tw + 56, 58, angle)
    s.add("</g>")
    s.add(f'<g transform="rotate({angle} {w / 2} {h / 2})">')
    s.text(HAND, label, w / 2, h / 2 + 15, size, INK, anchor="middle")
    s.add("</g>")
    s.save(name)


STATUS = {
    "live": ("live", GREEN_PEN),
    "soon": ("coming soon", AMBER_PEN),
    "dev": ("in development", BLUE_PEN),
}


def sticky(name, title, status, desc, link, color, angle, seed):
    s = Svg(440, 460, f"{title} ({STATUS[status][0]}): {desc}", seed=seed)
    nx, ny, nw, nh = 40, 46, 360, 380
    s.add(f'<g transform="rotate({angle} 220 235)">')
    s.add(f'<g filter="url(#shadow)"><path d="M{nx} {ny} H{nx + nw} V{ny + nh - 26} Q{nx + nw - 10} {ny + nh - 6} {nx + nw - 40} {ny + nh} H{nx} Z" fill="{color}"/></g>')
    s.add(f'<path d="M{nx + nw} {ny + nh - 26} Q{nx + nw - 10} {ny + nh - 6} {nx + nw - 40} {ny + nh} Q{nx + nw - 34} {ny + nh - 30} {nx + nw} {ny + nh - 26} Z" fill="#000" opacity="0.08"/>')
    x = nx + 28
    tw = s.text(HAND, title, x, ny + 84, 62, INK)
    s.underline(x - 2, ny + 98, tw + 8, PURPLE, 4, waves=2, amp=3)

    label, pen = STATUS[status]
    lw = PRINT.width(label, 22)
    s.rough_rect(x, ny + 116, lw + 40, 34, pen, 2, passes=1, wobble=2)
    if status == "live":
        s.check(x + 9, ny + 124, 15, pen)
    else:
        s.add(f'<circle cx="{x + 17}" cy="{ny + 133}" r="6" fill="{pen}"/>')
    s.text(PRINT, label, x + 32, ny + 141, 22, pen)

    for i, line in enumerate(wrap(PRINT, desc, 24, nw - 56)[:5]):
        s.text(PRINT, line, x, ny + 190 + i * 30, 24, INK)
    if link:
        lw = s.text(HAND, link, x, ny + nh - 22, 30, PURPLE)
        s.arrow(x + lw + 8, ny + nh - 30, x + lw + 44, ny + nh - 30, PURPLE, 3, bend=0.12)
    s.add("</g>")
    s.tape(220, 50, 120, 34, -angle * 2 + 2)
    s.save(name)


def index_card(name, title, tag, desc, angle, seed):
    s = Svg(500, 250, f"{title}: {desc} ({tag})", seed=seed)
    cx, cy, cw, ch = 22, 18, 456, 210
    s.add(f'<g transform="rotate({angle} 250 125)">')
    s.add(f'<g filter="url(#shadow)"><rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="3" fill="#FFFFFF"/></g>')
    paper_lines(s, cx, cy, cw, ch, first=cy + 106, step=30)
    s.add(f'<line x1="{cx}" y1="{cy + 66}" x2="{cx + cw}" y2="{cy + 66}" stroke="{MARGIN}" stroke-width="2"/>')
    x = cx + 24
    s.text(HAND, title, x, cy + 52, 44, INK)
    tw = PRINT.width(tag, 19)
    s.rough_rect(cx + cw - tw - 46, cy + 22, tw + 26, 30, PURPLE, 1.8, passes=1, wobble=1.5)
    s.text(PRINT, tag, cx + cw - tw - 33, cy + 43, 19, PURPLE)
    for i, line in enumerate(wrap(PRINT, desc, 23, cw - 48)[:4]):
        s.text(PRINT, line, x, cy + 101 + i * 30, 23, INK)
    s.add("</g>")
    s.save(name)


def button(name, label, seed):
    size = 32
    tw = HAND.width(label, size)
    w, h = int(tw + 96), 72
    s = Svg(w, h, label, seed=seed)
    s.add(f'<g filter="url(#shadow)"><rect x="10" y="10" width="{w - 20}" height="{h - 24}" rx="6" fill="{PAPER}"/></g>')
    s.rough_rect(10, 10, w - 20, h - 24, INK, 2, passes=2, wobble=2)
    s.text(HAND, label, 30, 45, size, INK)
    s.arrow(30 + tw + 10, 40, 30 + tw + 34, 24, PURPLE, 3, bend=0.1)
    s.save(name)


def toolbox():
    rows = [
        ("apple", "Swift, SwiftUI, AppKit, SwiftData, AVFoundation, Xcode"),
        ("web", "TypeScript, React, Next.js, Tailwind CSS, Cloudflare Workers"),
        ("backend", "Node.js, Python, PostgreSQL, SQL"),
        ("AI & agents", "Codex, Claude Code, OpenRouter, WebMCP, on-device speech"),
        ("workflow", "Git, GitHub, Figma, Obsidian"),
    ]
    alt = "Toolbox. " + ". ".join(f"{k}: {v}" for k, v in rows)
    s = Svg(1000, 330, alt, seed=11)
    s.add('<g transform="rotate(0.5 500 165)">')
    s.add('<g filter="url(#shadow)"><rect x="24" y="16" width="952" height="296" rx="3" fill="#FFFFFF"/></g>')
    grid = "".join(f'<line x1="{x}" y1="16" x2="{x}" y2="312"/>' for x in range(44, 976, 24))
    grid += "".join(f'<line x1="24" y1="{y}" x2="976" y2="{y}"/>' for y in range(28, 312, 24))
    s.add(f'<g stroke="#DCE8F5" stroke-width="1">{grid}</g>')
    for i, (k, v) in enumerate(rows):
        y = 74 + i * 52
        s.text(HAND, k, 230, y, 38, PURPLE, anchor="end", reveal=(0.2 + i * 0.35, 0.4))
        s.arrow(246, y - 12, 296, y - 12, SOFT_INK, 2.5, bend=0.08, draw=(0.5 + i * 0.35, 0.25))
        s.text(PRINT, v, 312, y, 28, INK, reveal=(0.6 + i * 0.35, 0.5))
    s.add("</g>")
    s.save("toolbox.svg")


def todo():
    items = [
        (True, "ship ZenVoice", "it's live!"),
        (False, "launch BuilderHelm", None),
        (False, "finish ClipHelm", None),
        (False, "build Rove, a browser for builders", None),
        (False, "make agent UIs humans can actually trust", None),
    ]
    alt = "To-do: " + "; ".join(("done: " if d else "") + t for d, t, _ in items)
    s = Svg(640, 430, alt, seed=5)
    s.add('<g transform="rotate(-1 320 215)">')
    s.add('<g filter="url(#shadow)"><rect x="30" y="30" width="580" height="370" rx="3" fill="#FFF8D6"/></g>')
    paper_lines(s, 30, 30, 580, 370, first=146, step=48, color="#EAD9A2")
    tw = s.text(HAND, "to-do:", 80, 102, 60, INK)
    s.underline(78, 116, tw + 10, RED_PEN, 4, waves=2)
    for i, (done, label, note) in enumerate(items):
        y = 182 + i * 48
        t = 0.4 + i * 0.45
        s.rough_rect(82, y - 26, 26, 26, INK, 2, passes=1, wobble=1.2)
        lw = s.text(PRINT, label, 126, y - 2, 29, SOFT_INK if done else INK, reveal=(t, 0.4))
        if done:
            s.check(84, y - 32, 24, GREEN_PEN, draw=(t + 0.5, 0.35))
            s.stroke(s.rough_line_d(122, y - 12, 130 + lw, y - 14, 1.5), RED_PEN, 3, draw=(t + 0.8, 0.35))
            s.text(HAND_REG, note, 150 + lw, y - 2, 32, GREEN_PEN, reveal=(t + 1.1, 0.4))
    s.add("</g>")
    s.tape(320, 34, 140, 36, 2)
    s.save("todo.svg")


def footer():
    quote = "Build systems that remain trustworthy when the demo is over."
    s = Svg(1000, 220, quote + " — Yash", seed=3)
    pts = [(60, 40)]
    for i in range(1, 30):  # torn bottom edge
        pts.append((60 + 880 * i / 29, 176 + (6 if i % 2 else -2) + s.j(3)))
    poly = "60,40 940,34 " + " ".join(f"{x:.1f},{y:.1f}" for x, y in reversed(pts[1:])) + " 60,180"
    s.add(f'<g filter="url(#shadow)" transform="rotate(-0.6 500 110)"><polygon points="{poly}" fill="{PAPER}"/></g>')
    s.text(HAND_REG, quote, 500, 104, 40, INK, anchor="middle", reveal=(0.2, 1.4))
    sw = s.text(HAND, "— Yash", 820, 158, 50, PURPLE, anchor="end", reveal=(1.7, 0.6))
    s.underline(820 - sw * 0.6, 168, sw * 0.65, PURPLE, 3, waves=2, amp=5, draw=(2.3, 0.4))
    s.tape(90, 46, 90, 30, -30)
    s.tape(910, 42, 90, 30, 28)
    s.save("footer.svg")


if __name__ == "__main__":
    header()
    for file, label, ang in [
        ("h-building.svg", "what I'm building", -1.5),
        ("h-open-source.svg", "open source", 1.2),
        ("h-toolbox.svg", "my toolbox", -1),
        ("h-stats.svg", "github stats", 1.5),
        ("h-now.svg", "right now", -1.2),
    ]:
        heading(file, label, ang)

    sticky("note-zenvoice.svg", "ZenVoice", "live",
           "Private dictation for Mac. Press a shortcut, speak, and clean text lands in any app. No cloud, no account, no subscription.",
           "getzenvoice.com", "#FFF4A3", -2, 1)
    sticky("note-builderhelm.svg", "BuilderHelm", "soon",
           "Your agents. You at the helm. One local-first desktop app to run, coordinate, and review coding agents.",
           "builderhelm.com", "#FFD6E0", 1.6, 2)
    sticky("note-cliphelm.svg", "ClipHelm", "dev",
           "AI finds the moments. You publish them. Long videos in, captioned and reframed short clips out.",
           "view source", "#CDEBFF", 1.2, 3)
    sticky("note-rove.svg", "Rove", "dev",
           "A native browser for people who build. More soon.",
           None, "#D4F5C9", -1.8, 4)

    cards = [
        ("card-cliphelm.svg", "ClipHelm", "Swift · AVFoundation",
         "AI video clipping for macOS. Transcribes on-device or via OpenRouter, ranks moments, burns in captions."),
        ("card-codex-micro.svg", "Codex Micro", "Swift · SwiftUI",
         "An iPhone control pad for Codex on your Mac. Paired over secure LAN; the phone never holds credentials."),
        ("card-agent-city.svg", "Agent City", "TypeScript · WebMCP",
         "A miniature internet where humans and AI agents share state through typed WebMCP tools."),
        ("card-goals-overlay.svg", "Goals Overlay", "Swift · AppKit",
         "Pins today's goals above every app and Space, with a goals CLI and natural-language deadlines."),
        ("card-ui-ux-audit.svg", "UI/UX Audit", "JavaScript",
         "Measured UI audits for coding agents: contrast, target size, focus, and overflow, checked against WCAG 2.2."),
        ("card-app-store-auditor.svg", "App Store Auditor", "Python",
         "Read-only App Store release-readiness checks for coding agents."),
        ("card-notchdeck.svg", "NotchDeck", "Swift",
         "A command center built around the MacBook notch. Early development."),
        ("card-signalcheck.svg", "SignalCheck", "Python",
         "Educational symptom-screening dashboard with explainable models trained on synthetic data."),
    ]
    for i, (file, title, tag, desc) in enumerate(cards):
        index_card(file, title, tag, desc, (-0.9, 0.8, 0.6, -0.7)[i % 4], 20 + i)

    button("btn-website.svg", "yashchaudhary.dev", 31)
    button("btn-x.svg", "X  @builderhelmai", 32)
    button("btn-linkedin.svg", "LinkedIn", 33)

    toolbox()
    todo()
    footer()
