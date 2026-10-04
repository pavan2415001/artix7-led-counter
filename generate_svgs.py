#!/usr/bin/env python3
"""Generate the dark-theme timing diagrams in docs/ for the Artix-7 LED counter.

Design modelled: clk (100 MHz) -> countr -> toggle clkf every (limit+1) clk cycles
-> count increments on every RISING edge of clkf.
Run:  python generate_svgs.py
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
os.makedirs(OUT, exist_ok=True)

CLK_HZ = 100_000_000
WIN = 4.0                       # seconds shown in part B
MODES = [("1hz", "00", 1), ("2hz", "01", 2), ("5hz", "10", 5), ("10hz", "11", 10)]
C_LED = ["#38bdf8", "#4ade80", "#f472b6", "#fbbf24"]   # count[0..3]
C_CLKF, C_TERM, C_NEW = "#a78bfa", "#fb923c", "#34d399"
FONT = "system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, sans-serif"


def hz(v):
    return f"{v:g}"


def step_path(xs, vals, yt, yb):
    y0 = yt if vals[0] else yb
    p = f"M{xs[0]:.1f},{y0}"
    for i, v in enumerate(vals):
        y = yt if v else yb
        p += f" L{xs[i]:.1f},{y} L{xs[i+1]:.1f},{y}"
    return p


def svg_open(w, h):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" font-family="{FONT}">',
        '<defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0f172a"/>'
        '<stop offset="100%" stop-color="#1e293b"/></linearGradient>'
        '</defs>',
        f'<rect width="{w}" height="{h}" rx="12" fill="url(#bg)" stroke="#334155" stroke-width="1.5"/>',
    ]


def header(s, title, sub):
    s.append(f'<text x="480" y="36" text-anchor="middle" fill="#f8fafc" font-size="18" font-weight="700">{title}</text>')
    s.append(f'<text x="480" y="57" text-anchor="middle" fill="#94a3b8" font-size="12">{sub}</text>')


def panel(s, y, h, title):
    s.append(f'<rect x="20" y="{y}" width="920" height="{h}" rx="8" fill="#1e293b" opacity="0.7" stroke="#334155"/>')
    s.append(f'<text x="36" y="{y+24}" fill="#f8fafc" font-size="13" font-weight="700">{title}</text>')


def label(s, y, text, color="#cbd5e1", sub=None):
    s.append(f'<text x="36" y="{y}" fill="{color}" font-size="12" font-weight="700">{text}</text>')
    if sub:
        s.append(f'<text x="36" y="{y+14}" fill="#64748b" font-size="10">{sub}</text>')


def section_a(s, y, cyc):
    """Zoom on the 100 MHz clock around one terminal count. Returns bottom y."""
    L = cyc - 1
    h = 326
    panel(s, y, h, "A) Zoom on the 100 MHz clock  (1 cell = 1 clk cycle = 10 ns)")
    cells = [0, 1, 2, None, L - 2, L - 1, L, 0, 1]
    w, x0, RH = 70, 180, 44
    xs = [x0 + i * w for i in range(len(cells))]
    names = ["clk (100 MHz)", "countr[25:0]", "countr = limit", "clkf", "count[3:0]"]
    rows = []
    for r, n in enumerate(names):
        yt = y + 46 + r * RH
        yb = yt + 26
        rows.append((yt, yb))
        label(s, (yt + yb) / 2 + 4, n)
    for i, c in enumerate(cells):
        x = xs[i]
        if c is None:
            for (yt, yb) in rows:
                s.append(f'<text x="{x+w/2}" y="{(yt+yb)/2+5}" text-anchor="middle" fill="#64748b" font-size="14" font-weight="700">• • •</text>')
            continue
        # clk
        yt, yb = rows[0]
        s.append(f'<path d="M{x},{yb} L{x},{yt} L{x+w/2},{yt} L{x+w/2},{yb} L{x+w},{yb}" fill="none" stroke="#e2e8f0" stroke-width="2"/>')
        # countr
        yt, yb = rows[1]
        term = (i == 6)
        fill, stroke = ("#312e81", "#6366f1") if term else ("#0f172a", "#475569")
        s.append(f'<rect x="{x}" y="{yt}" width="{w}" height="{yb-yt}" rx="4" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
        s.append(f'<text x="{x+w/2}" y="{(yt+yb)/2+4}" text-anchor="middle" fill="{"#818cf8" if term else "#f1f5f9"}" font-size="10.5" font-weight="600">{c:,}</text>')
        # count
        yt, yb = rows[4]
        new = i >= 7
        s.append(f'<rect x="{x}" y="{yt}" width="{w}" height="{yb-yt}" rx="4" fill="{"#064e3b" if new else "#0f172a"}" stroke="{C_NEW if new else "#475569"}" stroke-width="1.5"/>')
        s.append(f'<text x="{x+w/2}" y="{(yt+yb)/2+4}" text-anchor="middle" fill="{C_NEW if new else "#f1f5f9"}" font-size="11" font-weight="700">{"N + 1" if new else "N"}</text>')
    # terminal-count pulse and clkf drawn as single continuous paths (crisp, no filters)
    tt, tb = rows[2]
    s.append(f'<path d="M{xs[0]},{tb} L{xs[3]},{tb}" fill="none" stroke="{C_TERM}" stroke-width="2.5"/>')
    s.append(f'<path d="M{xs[4]},{tb} L{xs[6]},{tb} L{xs[6]},{tt} L{xs[7]},{tt} L{xs[7]},{tb} L{xs[8]+w},{tb}" fill="none" stroke="{C_TERM}" stroke-width="2.5" stroke-linejoin="miter"/>')
    ft, fb = rows[3]
    s.append(f'<path d="M{xs[0]},{fb} L{xs[3]},{fb}" fill="none" stroke="{C_CLKF}" stroke-width="2.5"/>')
    s.append(f'<path d="M{xs[4]},{fb} L{xs[7]},{fb} L{xs[7]},{ft} L{xs[8]+w},{ft}" fill="none" stroke="{C_CLKF}" stroke-width="2.5" stroke-linejoin="miter"/>')
    ya = y + 46 + 5 * RH + 12
    s.append(f'<text x="{xs[3]+w/2}" y="{ya}" text-anchor="middle" fill="#94a3b8" font-size="11">{cyc-6:,} more cycles</text>')
    s.append(f'<text x="{xs[6]+w/2}" y="{ya}" text-anchor="middle" fill="{C_TERM}" font-size="11" font-weight="700">terminal count</text>')
    s.append(f'<text x="{xs[6]+w}" y="{ya+18}" text-anchor="middle" fill="{C_NEW}" font-size="11" font-weight="700">clkf rises → count + 1, countr → 0</text>')
    s.append(f'<text x="{xs[6]+w}" y="{ya+34}" text-anchor="middle" fill="#94a3b8" font-size="11">next terminal count: clkf falls, count unchanged</text>')
    return y + h


def grid(s, y0, y1, win, X0=180, X1=910):
    for k in range(5):
        x = X0 + k * (X1 - X0) / 4
        s.append(f'<line x1="{x}" y1="{y0}" x2="{x}" y2="{y1}" stroke="#334155" stroke-dasharray="4,4" stroke-width="1"/>')
        s.append(f'<text x="{x}" y="{y1+18}" text-anchor="middle" fill="#94a3b8" font-size="11" font-weight="600">{win*k/4:g} s</text>')


def section_b(s, y, f):
    X0, X1, RH = 180, 910, 52
    rows = ["clkf", "count[0] (LED0)", "count[1] (LED1)", "count[2] (LED2)", "count[3] (LED3)"]
    h = 46 + RH * 5 + 40
    panel(s, y, h, f"B) Resulting waveforms over {WIN:g} s of real time  (clkf = {f} Hz)")
    nh = int(WIN * 2 * f)
    xs = [X0 + j * (X1 - X0) / nh for j in range(nh + 1)]
    grid(s, y + 36, y + 46 + RH * 5 - 4, WIN)
    rates = [f"{f} Hz", f"{f/2:g} Hz", f"{f/4:g} Hz", f"{f/8:g} Hz", f"{f/16:g} Hz"]
    for r, n in enumerate(rows):
        yt = y + 46 + r * RH
        yb = yt + 26
        col = C_CLKF if r == 0 else C_LED[r - 1]
        label(s, yt + 12, n, col, rates[r])
        vals = [j & 1 for j in range(nh)] if r == 0 else [(((j + 1) // 2) >> (r - 1)) & 1 for j in range(nh)]
        s.append(f'<path d="{step_path(xs, vals, yt, yb)}" fill="none" stroke="{col}" stroke-width="2.5"/>')
    return y + h


def mode_svg(name, sel, f):
    cyc = CLK_HZ // (2 * f)
    parts = []
    y = 76
    A = []; yb = section_a(A, y, cyc)
    B = []; yb2 = section_b(B, yb + 14, f)
    H = yb2 + 16
    s = svg_open(960, H)
    header(s, f"Mode freq[1:0] = {sel}:  clkf = {f} Hz,  LED0 blinks at {f/2:g} Hz",
           f"limit = {cyc-1:,}  |  clkf toggles every {cyc:,} clk cycles ({cyc*10/1e6:g} ms)  |  count increments on each rising edge of clkf")
    s += A + B + ["</svg>"]
    open(os.path.join(OUT, f"waveform_{name}.svg"), "w", encoding="utf-8").write("\n".join(s))


def overview():
    X0, X1, RH = 180, 910, 62
    H = 76 + 60 + RH * 4 + 60
    s = svg_open(960, H)
    header(s, f"LED0 in all four modes, same {WIN:g} s time scale",
           "counter increments at 1, 2, 5, 10 Hz  →  LED0 blinks at 0.5, 1, 2.5, 5 Hz")
    panel(s, 76, H - 92, "LED0 = count[0]")
    y0 = 112
    label(s, y0 + 16, "clk (100 MHz)")
    s.append(f'<rect x="{X0}" y="{y0}" width="{X1-X0}" height="24" rx="4" fill="#334155"/>')
    s.append(f'<text x="{(X0+X1)/2}" y="{y0+16}" text-anchor="middle" fill="#e2e8f0" font-size="12">{int(CLK_HZ*WIN):,} clock edges in {WIN:g} s (too dense to draw)</text>')
    ytop = y0 + 44
    grid(s, ytop - 6, ytop + RH * 4 - 6, WIN)
    for r, (name, sel, f) in enumerate(MODES):
        yt = ytop + r * RH + 6
        yb = yt + 28
        col = C_LED[r]
        label(s, yt + 12, f"freq = {sel}", col, f"clkf {f} Hz → LED0 {f/2:g} Hz")
        nh = int(WIN * 2 * f)
        xs = [X0 + j * (X1 - X0) / nh for j in range(nh + 1)]
        s.append(f'<path d="{step_path(xs, [((j+1)//2) & 1 for j in range(nh)], yt, yb)}" fill="none" stroke="{col}" stroke-width="2.5"/>')
    s.append("</svg>")
    open(os.path.join(OUT, "waveform_overview.svg"), "w", encoding="utf-8").write("\n".join(s))


if __name__ == "__main__":
    for m in MODES:
        mode_svg(*m)
    overview()
    print("Wrote SVGs to", OUT)
