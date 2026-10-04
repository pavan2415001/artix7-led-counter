import os

docs_dir = r"c:\Users\ASUS\OneDrive\Documents\LibraryManagementSystem\Artix7_LED_Counter\docs"
os.makedirs(docs_dir, exist_ok=True)

# -----------------------------------------------------------------------------
# 1. Overview Comparison SVG (waveform_overview.svg)
# -----------------------------------------------------------------------------
svg_overview = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 440" width="100%" height="100%" font-family="system-ui, -apple-system, 'SF Pro Display', Segoe UI, Roboto, Helvetica, sans-serif">
  <defs>
    <linearGradient id="bgGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <filter id="glow1" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="960" height="440" rx="12" fill="url(#bgGrad)" stroke="#334155" stroke-width="1.5"/>

  <!-- Title & Subtitle -->
  <text x="480" y="38" text-anchor="middle" fill="#f8fafc" font-size="17" font-weight="700" letter-spacing="0.5">LED0 Speed Select Comparison (2-Second Real Time Window)</text>
  <text x="480" y="58" text-anchor="middle" fill="#94a3b8" font-size="12">Driven by 100 MHz System Clock (10 ns period per cycle)</text>

  <!-- 100 MHz Clock Banner -->
  <g transform="translate(160, 80)">
    <text x="-140" y="15" fill="#cbd5e1" font-size="13" font-weight="600">clk (100 MHz)</text>
    <rect x="0" y="0" width="750" height="22" rx="4" fill="#334155" opacity="0.6" stroke="#475569"/>
    <text x="375" y="15" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="600">200,000,000 clock cycles in 2.0 s (10 ns resolution prescaler count)</text>
  </g>

  <!-- Time Grid Markers -->
  <g stroke="#334155" stroke-dasharray="4,4" stroke-width="1">
    <line x1="160" y1="115" x2="160" y2="385"/>
    <line x1="347.5" y1="115" x2="347.5" y2="385"/>
    <line x1="535" y1="115" x2="535" y2="385"/>
    <line x1="722.5" y1="115" x2="722.5" y2="385"/>
    <line x1="910" y1="115" x2="910" y2="385"/>
  </g>

  <!-- Time Labels -->
  <g fill="#94a3b8" font-size="12" font-weight="600" text-anchor="middle">
    <text x="160" y="405">0.0 s</text>
    <text x="347.5" y="405">0.5 s</text>
    <text x="535" y="405">1.0 s</text>
    <text x="722.5" y="405">1.5 s</text>
    <text x="910" y="405">2.0 s</text>
  </g>

  <!-- Signal 1: 1 Hz (freq = 00) -->
  <g transform="translate(0, 130)">
    <text x="20" y="24" fill="#38bdf8" font-size="13" font-weight="700">freq[1:0] = 00</text>
    <text x="20" y="40" fill="#64748b" font-size="11">1 Hz LED0 blink</text>
    <path d="M160,45 L347.5,45 L347.5,10 L535,10 L535,45 L722.5,45 L722.5,10 L910,10" fill="none" stroke="#38bdf8" stroke-width="2.5" filter="url(#glow1)"/>
  </g>

  <!-- Signal 2: 2 Hz (freq = 01) -->
  <g transform="translate(0, 195)">
    <text x="20" y="24" fill="#4ade80" font-size="13" font-weight="700">freq[1:0] = 01</text>
    <text x="20" y="40" fill="#64748b" font-size="11">2 Hz LED0 blink</text>
    <path d="M160,45 L253.75,45 L253.75,10 L347.5,10 L347.5,45 L441.25,45 L441.25,10 L535,10 L535,45 L628.75,45 L628.75,10 L722.5,10 L722.5,45 L816.25,45 L816.25,10 L910,10" fill="none" stroke="#4ade80" stroke-width="2.5" filter="url(#glow1)"/>
  </g>

  <!-- Signal 3: 5 Hz (freq = 10) -->
  <g transform="translate(0, 260)">
    <text x="20" y="24" fill="#fbbf24" font-size="13" font-weight="700">freq[1:0] = 10</text>
    <text x="20" y="40" fill="#64748b" font-size="11">5 Hz LED0 blink</text>
    <path d="M160,45 L197.5,45 L197.5,10 L235,10 L235,45 L272.5,45 L272.5,10 L310,10 L310,45 L347.5,45 L347.5,10 L385,10 L385,45 L422.5,45 L422.5,10 L460,10 L460,45 L497.5,45 L497.5,10 L535,10 L535,45 L572.5,45 L572.5,10 L610,10 L610,45 L647.5,45 L647.5,10 L685,10 L685,45 L722.5,45 L722.5,10 L760,10 L760,45 L797.5,45 L797.5,10 L835,10 L835,45 L872.5,45 L872.5,10 L910,10" fill="none" stroke="#fbbf24" stroke-width="2.5" filter="url(#glow1)"/>
  </g>

  <!-- Signal 4: 10 Hz (freq = 11) -->
  <g transform="translate(0, 325)">
    <text x="20" y="24" fill="#f43f5e" font-size="13" font-weight="700">freq[1:0] = 11</text>
    <text x="20" y="40" fill="#64748b" font-size="11">10 Hz LED0 blink</text>
    <path d="M160,45 L178.75,45 L178.75,10 L197.5,10 L197.5,45 L216.25,45 L216.25,10 L235,10 L235,45 L253.75,45 L253.75,10 L272.5,10 L272.5,45 L291.25,45 L291.25,10 L310,10 L310,45 L328.75,45 L328.75,10 L347.5,10 L347.5,45 L366.25,45 L366.25,10 L385,10 L385,45 L403.75,45 L403.75,10 L422.5,10 L422.5,45 L441.25,45 L441.25,10 L460,10 L460,45 L478.75,45 L478.75,10 L497.5,10 L497.5,45 L516.25,45 L516.25,10 L535,10 L535,45 L553.75,45 L553.75,10 L572.5,10 L572.5,45 L591.25,45 L591.25,10 L610,10 L610,45 L628.75,45 L628.75,10 L647.5,10 L647.5,45 L666.25,45 L666.25,10 L685,10 L685,45 L703.75,45 L703.75,10 L722.5,10 L722.5,45 L741.25,45 L741.25,10 L760,10 L760,45 L778.75,45 L778.75,10 L797.5,10 L797.5,45 L816.25,45 L816.25,10 L835,10 L835,45 L853.75,45 L853.75,10 L872.5,10 L872.5,45 L891.25,45 L891.25,10 L910,10" fill="none" stroke="#f43f5e" stroke-width="2.5" filter="url(#glow1)"/>
  </g>
</svg>
"""

with open(os.path.join(docs_dir, "waveform_overview.svg"), "w", encoding="utf-8") as f:
    f.write(svg_overview)

# -----------------------------------------------------------------------------
# Function to generate Detailed Mode SVGs (1 Hz, 2 Hz, 5 Hz, 10 Hz)
# -----------------------------------------------------------------------------
def make_mode_svg(mode_name, freq_bits, limit_val, limit_formatted, tick_ms, tick_hz, led0_hz, led_color, tick_offsets):
    # tick_offsets are percentages or positions along 750px width for 4 ticks
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 680" width="100%" height="100%" font-family="system-ui, -apple-system, 'SF Pro Display', Segoe UI, Roboto, Helvetica, sans-serif">
  <defs>
    <linearGradient id="bgGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="960" height="680" rx="12" fill="url(#bgGrad)" stroke="#334155" stroke-width="1.5"/>

  <!-- Header -->
  <text x="480" y="36" text-anchor="middle" fill="#f8fafc" font-size="18" font-weight="700">Mode freq[1:0] = {freq_bits} : {led0_hz} LED0 Blink Rate</text>
  <text x="480" y="56" text-anchor="middle" fill="#94a3b8" font-size="12">Limit = {limit_formatted} | Terminal Count Period = {tick_ms} ms ({tick_hz} Tick Rate)</text>

  <!-- Section A: 100 MHz Clock Zoom -->
  <g transform="translate(20, 80)">
    <rect width="920" height="210" rx="8" fill="#1e293b" opacity="0.7" stroke="#334155"/>
    <text x="16" y="24" fill="#f8fafc" font-size="13" font-weight="700">A) Prescaler Zoom (1 Clock Cycle = 10 ns)</text>

    <!-- clk waveform -->
    <text x="16" y="60" fill="#cbd5e1" font-size="12" font-weight="600">clk (100 MHz)</text>
    <path d="M160,65 L160,45 L195,45 L195,65 L230,65 L230,45 L265,45 L265,65 L300,65" fill="none" stroke="#e2e8f0" stroke-width="2"/>
    <text x="365" y="60" text-anchor="middle" fill="#64748b" font-size="14" font-weight="700">• • •</text>
    <path d="M430,65 L430,45 L465,45 L465,65 L500,65 L500,45 L535,45 L535,65 L570,65 L570,45 L605,45 L605,65 L640,65 L640,45 L675,45 L675,65 L710,65 L710,45 L745,45 L745,65 L780,65" fill="none" stroke="#e2e8f0" stroke-width="2"/>

    <!-- countr bus -->
    <text x="16" y="110" fill="#cbd5e1" font-size="12" font-weight="600">countr[25:0]</text>
    <g fill="#0f172a" stroke="#475569" stroke-width="1.5">
      <rect x="160" y="95" width="70" height="26" rx="4"/>
      <rect x="230" y="95" width="70" height="26" rx="4"/>
      <rect x="430" y="95" width="70" height="26" rx="4"/>
      <rect x="500" y="95" width="70" height="26" rx="4"/>
      <rect x="570" y="95" width="70" height="26" rx="4" fill="#312e81" stroke="#6366f1"/>
      <rect x="640" y="95" width="70" height="26" rx="4"/>
      <rect x="710" y="95" width="70" height="26" rx="4"/>
    </g>
    <g fill="#f1f5f9" font-size="11" font-weight="600" text-anchor="middle">
      <text x="195" y="112">0</text>
      <text x="265" y="112">1</text>
      <text x="365" y="112" fill="#64748b">• • •</text>
      <text x="465" y="112">{limit_val - 2:,}</text>
      <text x="535" y="112">{limit_val - 1:,}</text>
      <text x="605" y="112" fill="#818cf8">{limit_formatted}</text>
      <text x="675" y="112">0</text>
      <text x="745" y="112">1</text>
    </g>

    <!-- enable pulse -->
    <text x="16" y="160" fill="#cbd5e1" font-size="12" font-weight="600">terminal_count</text>
    <path d="M160,165 L570,165 L570,140 L640,140 L640,165 L780,165" fill="none" stroke="#fb923c" stroke-width="2.5" filter="url(#glow)"/>
    <text x="605" y="182" text-anchor="middle" fill="#fb923c" font-size="10" font-weight="700">1-Cycle Enable Pulse</text>

    <!-- count bus -->
    <text x="16" y="198" fill="#cbd5e1" font-size="12" font-weight="600">count[3:0]</text>
    <g fill="#0f172a" stroke="#475569" stroke-width="1.5">
      <rect x="160" y="185" width="410" height="22" rx="4"/>
      <rect x="570" y="185" width="70" height="22" rx="4"/>
      <rect x="640" y="185" width="140" height="22" rx="4" fill="#064e3b" stroke="#10b981"/>
    </g>
    <g fill="#f1f5f9" font-size="11" font-weight="600" text-anchor="middle">
      <text x="365" y="200">N</text>
      <text x="605" y="200">N</text>
      <text x="710" y="200" fill="#34d399">N + 1</text>
    </g>
  </g>

  <!-- Section B: Real-time LED Waveforms -->
  <g transform="translate(20, 305)">
    <rect width="920" height="355" rx="8" fill="#1e293b" opacity="0.7" stroke="#334155"/>
    <text x="16" y="24" fill="#f8fafc" font-size="13" font-weight="700">B) 4-Bit Binary Counter LED Waveforms (2.0 s Time Window)</text>

    <!-- Time Grid Lines -->
    <g stroke="#334155" stroke-dasharray="4,4" stroke-width="1">
      <line x1="160" y1="35" x2="160" y2="315"/>
      <line x1="347.5" y1="35" x2="347.5" y2="315"/>
      <line x1="535" y1="35" x2="535" y2="315"/>
      <line x1="722.5" y1="35" x2="722.5" y2="315"/>
      <line x1="910" y1="35" x2="910" y2="315"/>
    </g>

    <!-- Enable Ticks -->
    <text x="16" y="55" fill="#cbd5e1" font-size="12" font-weight="600">terminal_count</text>
    <line x1="160" y1="58" x2="910" y2="58" stroke="#475569" stroke-width="1.5"/>
"""
    # Draw tick spikes
    for pos in tick_offsets:
        svg += f'    <rect x="{pos-1.5}" y="42" width="3" height="16" fill="#fb923c" rx="1"/>\n'

    # LED0 (count[0])
    svg += f"""
    <text x="16" y="105" fill="{led_color}" font-size="12" font-weight="700">count[0] (LED0)</text>
    <text x="16" y="120" fill="#64748b" font-size="10">{led0_hz} Blink Rate</text>
"""
    # Generate path for count[0], count[1], count[2], count[3] based on ticks
    # For count[0]: toggles on every tick in tick_offsets
    path_c0 = f"M160,115 "
    curr_y = 115
    curr_x = 160
    high_y = 85
    low_y = 115
    state = 0
    for tick_x in tick_offsets:
        path_c0 += f"L{tick_x},{curr_y} "
        state = 1 - state
        curr_y = high_y if state == 1 else low_y
        path_c0 += f"L{tick_x},{curr_y} "
    path_c0 += f"L910,{curr_y}"

    svg += f'    <path d="{path_c0}" fill="none" stroke="{led_color}" stroke-width="2.5" filter="url(#glow)"/>\n'

    # count[1] (LED1): toggles every 2 ticks
    path_c1 = "M160,175 "
    state = 0
    curr_y = 175
    high_y = 145
    low_y = 175
    for i, tick_x in enumerate(tick_offsets):
        if (i % 2) == 1:
            path_c1 += f"L{tick_x},{curr_y} "
            state = 1 - state
            curr_y = high_y if state == 1 else low_y
            path_c1 += f"L{tick_x},{curr_y} "
    path_c1 += f"L910,{curr_y}"

    svg += f"""
    <text x="16" y="165" fill="#4ade80" font-size="12" font-weight="700">count[1] (LED1)</text>
    <text x="16" y="180" fill="#64748b" font-size="10">{led0_hz/2:.3g} Hz</text>
    <path d="{path_c1}" fill="none" stroke="#4ade80" stroke-width="2.5"/>
"""

    # count[2] (LED2): toggles every 4 ticks
    path_c2 = "M160,235 "
    state = 0
    curr_y = 235
    high_y = 205
    low_y = 235
    for i, tick_x in enumerate(tick_offsets):
        if (i % 4) == 3:
            path_c2 += f"L{tick_x},{curr_y} "
            state = 1 - state
            curr_y = high_y if state == 1 else low_y
            path_c2 += f"L{tick_x},{curr_y} "
    path_c2 += f"L910,{curr_y}"

    svg += f"""
    <text x="16" y="225" fill="#38bdf8" font-size="12" font-weight="700">count[2] (LED2)</text>
    <text x="16" y="240" fill="#64748b" font-size="10">{led0_hz/4:.3g} Hz</text>
    <path d="{path_c2}" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
"""

    # count[3] (LED3): toggles every 8 ticks
    path_c3 = "M160,295 "
    state = 0
    curr_y = 295
    high_y = 265
    low_y = 295
    for i, tick_x in enumerate(tick_offsets):
        if (i % 8) == 7:
            path_c3 += f"L{tick_x},{curr_y} "
            state = 1 - state
            curr_y = high_y if state == 1 else low_y
            path_c3 += f"L{tick_x},{curr_y} "
    path_c3 += f"L910,{curr_y}"

    svg += f"""
    <text x="16" y="285" fill="#a855f7" font-size="12" font-weight="700">count[3] (LED3)</text>
    <text x="16" y="300" fill="#64748b" font-size="10">{led0_hz/8:.3g} Hz</text>
    <path d="{path_c3}" fill="none" stroke="#a855f7" stroke-width="2.5"/>

    <!-- Time Labels -->
    <g fill="#94a3b8" font-size="11" font-weight="600" text-anchor="middle">
      <text x="160" y="335">0.0 s</text>
      <text x="347.5" y="335">0.5 s</text>
      <text x="535" y="335">1.0 s</text>
      <text x="722.5" y="335">1.5 s</text>
      <text x="910" y="335">2.0 s</text>
    </g>
  </g>
</svg>
"""
    return svg

# Ticks calculations: 160 to 910 is width 750px representing 2.0 seconds (375px per sec)

# 1 Hz mode: tick every 0.5s -> 4 ticks in 2s window at x = 160 + 0.5*375, 160 + 1.0*375, 160 + 1.5*375, 160 + 2.0*375
ticks_1hz = [160 + 0.5*375, 160 + 1.0*375, 160 + 1.5*375, 160 + 2.0*375]
svg_1hz = make_mode_svg("1Hz", "00", 49999999, "49,999,999", 500, "2 Hz", 1, "#38bdf8", ticks_1hz)
with open(os.path.join(docs_dir, "waveform_1hz.svg"), "w", encoding="utf-8") as f:
    f.write(svg_1hz)

# 2 Hz mode: tick every 0.25s -> 8 ticks in 2s
ticks_2hz = [160 + i*0.25*375 for i in range(1, 9)]
svg_2hz = make_mode_svg("2Hz", "01", 24999999, "24,999,999", 250, "4 Hz", 2, "#4ade80", ticks_2hz)
with open(os.path.join(docs_dir, "waveform_2hz.svg"), "w", encoding="utf-8") as f:
    f.write(svg_2hz)

# 5 Hz mode: tick every 0.1s -> 20 ticks in 2s
ticks_5hz = [160 + i*0.1*375 for i in range(1, 21)]
svg_5hz = make_mode_svg("5Hz", "10", 9999999, "9,999,999", 100, "10 Hz", 5, "#fbbf24", ticks_5hz)
with open(os.path.join(docs_dir, "waveform_5hz.svg"), "w", encoding="utf-8") as f:
    f.write(svg_5hz)

# 10 Hz mode: tick every 0.05s -> 40 ticks in 2s
ticks_10hz = [160 + i*0.05*375 for i in range(1, 41)]
svg_10hz = make_mode_svg("10Hz", "11", 4999999, "4,999,999", 50, "20 Hz", 10, "#f43f5e", ticks_10hz)
with open(os.path.join(docs_dir, "waveform_10hz.svg"), "w", encoding="utf-8") as f:
    f.write(svg_10hz)

print("All SVGs generated successfully!")
