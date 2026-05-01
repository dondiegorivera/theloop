---
adapter: svg
max_iters: 10
score_threshold: 0.95
no_improvement_for: 7
---

# Mechanical Pocket Watch

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="100%" height="100%">
<defs>
<!-- Metallic Gradients -->
<linearGradient id="brassGradient" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" style="stop-color:#d4af37;stop-opacity:1" />
<stop offset="50%" style="stop-color:#f9e596;stop-opacity:1" />
<stop offset="100%" style="stop-color:#aa7c11;stop-opacity:1" />
</linearGradient>
<linearGradient id="silverGradient" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" style="stop-color:#e0e0e0;stop-opacity:1" />
<stop offset="50%" style="stop-color:#ffffff;stop-opacity:1" />
<stop offset="100%" style="stop-color:#b0b0b0;stop-opacity:1" />
</linearGradient>
<radialGradient id="dialGradient" cx="50%" cy="50%" r="50%">
<stop offset="0%" style="stop-color:#ffffff;stop-opacity:1" />
<stop offset="80%" style="stop-color:#f5f5dc;stop-opacity:1" />
<stop offset="100%" style="stop-color:#e8e0c8;stop-opacity:1" />
</radialGradient>
<filter id="dropShadow" x="-20%" y="-20%" width="140%" height="140%">
<feGaussianBlur in="SourceAlpha" stdDeviation="3"/>
<feOffset dx="2" dy="2" result="offsetblur"/>
<feComponentTransfer>
<feFuncA type="linear" slope="0.3"/>
</feComponentTransfer>
<feMerge>
<feMergeNode/>
<feMergeNode in="SourceGraphic"/>
</feMerge>
</filter>
</defs>

<!-- Background (Transparent) -->
<rect width="600" height="600" fill="transparent" />

<!-- Chain -->
<g id="chain" stroke="url(#brassGradient)" stroke-width="4" fill="none">
<path d="M 300 80 Q 350 40 380 60 T 420 40" stroke-linecap="round" />
<path d="M 300 80 Q 250 40 220 60 T 180 40" stroke-linecap="round" />
<!-- Links -->
<ellipse cx="300" cy="80" rx="8" ry="4" transform="rotate(-30 300 80)" fill="url(#brassGradient)" stroke="none" />
<ellipse cx="330" cy="65" rx="8" ry="4" transform="rotate(-15 330 65)" fill="url(#brassGradient)" stroke="none" />
<ellipse cx="360" cy="55" rx="8" ry="4" transform="rotate(0 360 55)" fill="url(#brassGradient)" stroke="none" />
<ellipse cx="270" cy="65" rx="8" ry="4" transform="rotate(15 270 65)" fill="url(#brassGradient)" stroke="none" />
<ellipse cx="240" cy="55" rx="8" ry="4" transform="rotate(0 240 55)" fill="url(#brassGradient)" stroke="none" />
</g>

<!-- Crown and Stem -->
<g id="crown">
<rect x="290" y="100" width="20" height="40" fill="url(#silverGradient)" stroke="#888" stroke-width="1" />
<path d="M 285 100 L 315 100 L 310 80 L 290 80 Z" fill="url(#brassGradient)" stroke="#aa7c11" stroke-width="1" />
<line x1="292" y1="85" x2="292" y2="95" stroke="#888" stroke-width="1" />
<line x1="300" y1="85" x2="300" y2="95" stroke="#888" stroke-width="1" />
<line x1="308" y1="85" x2="308" y2="95" stroke="#888" stroke-width="1" />
</g>

<!-- Outer Case -->
<g id="case" filter="url(#dropShadow)">
<circle cx="300" cy="300" r="200" fill="url(#brassGradient)" stroke="#886600" stroke-width="2" />
<!-- Bezel Ring -->
<circle cx="300" cy="300" r="190" fill="none" stroke="#f9e596" stroke-width="4" opacity="0.6" />
<circle cx="300" cy="300" r="185" fill="none" stroke="#aa7c11" stroke-width="1" />
</g>

<!-- Dial -->
<g id="dial">
<circle cx="300" cy="300" r="170" fill="url(#dialGradient)" stroke="#d4af37" stroke-width="2" />

<!-- Minute Ticks -->
<g id="minute-ticks" stroke="#555" stroke-width="1">
<!-- Generated 60 ticks -->
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(6 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(12 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(18 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(24 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(30 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(36 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(42 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(48 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(54 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(60 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(66 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(72 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(78 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(84 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(90 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(96 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(102 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(108 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(114 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(120 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(126 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(132 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(138 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(144 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(150 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(156 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(162 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(168 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(174 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(180 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(186 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(192 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(198 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(204 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(210 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(216 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(222 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(228 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(234 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(240 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(246 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(252 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(258 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(264 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(270 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(276 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(282 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(288 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(294 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(300 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(306 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(312 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(318 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(324 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(330 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(336 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(342 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(348 300 300)" />
<line x1="300" y1="130" x2="300" y2="135" transform="rotate(354 300 300)" />
</g>

<!-- Hour Markers -->
<g id="hour-markers" stroke="#333" stroke-width="3" stroke-linecap="round">
<line x1="300" y1="135" x2="300" y2="155" transform="rotate(0 300 300)" />
<line x1="300" y1="135" x2="300" y2="155" transform="rotate(30 300 300)" />
<line x1="300" y1="135" x2="300" y2="155" transform="rotate(60 300 300)" />
<line x1="300" y1="135" x2="300" y2="155" transform="rotate(90 300 300)" />
<line x1="300" y1="135" x2="300" y2="155" transform="rotate(120 300 300)" />
<line x1="300" y1="135" x2="300" y2="155" transform="rotate(150 300 300)" />
<line x1="300" y1="135" x2="300" y2="155" transform="rotate(180 300 300)" />
<line x1="300" y1="135" x2="300" y2="155" transform="rotate(210 300 300)" />
<line x1="300" y1="135" x2="300" y2="155" transform="rotate(240 300 300)" />
<line x1="300" y1="135" x2="300" y2="155" transform="rotate(270 300 300)" />
<line x1="300" y1="135" x2="300" y2="155" transform="rotate(300 300 300)" />
<line x1="300" y1="135" x2="300" y2="155" transform="rotate(330 300 300)" />
</g>

<!-- Roman Numerals -->
<g id="roman-numerals" font-family="serif" font-size="24" fill="#333" text-anchor="middle" dominant-baseline="central">
<text x="300" y="175">XII</text>
<text x="387" y="200">I</text>
<text x="445" y="275">II</text>
<text x="465" y="360">III</text>
<text x="445" y="445">IV</text>
<text x="387" y="510">V</text>
<text x="300" y="535">VI</text>
<text x="213" y="510">VII</text>
<text x="155" y="445">VIII</text>
<text x="135" y="360">IX</text>
<text x="155" y="275">X</text>
<text x="213" y="200">XI</text>
</g>

<!-- Sub-dials -->
<!-- Power Reserve at 12 o'clock -->
<g id="power-reserve">
<circle cx="300" cy="180" r="25" fill="#f5f5dc" stroke="#888" stroke-width="1" />
<path d="M 300 180 L 300 155 A 25 25 0 0 1 325 180 Z" fill="#d4af37" opacity="0.6" />
<text x="300" y="185" font-family="sans-serif" font-size="8" fill="#333" text-anchor="middle">POWER</text>
</g>

<!-- Small Seconds at 6 o'clock -->
<g id="small-seconds">
<circle cx="300" cy="420" r="30" fill="#f5f5dc" stroke="#888" stroke-width="1" />
<g id="small-seconds-ticks" stroke="#333" stroke-width="1">
<line x1="300" y1="390" x2="300" y2="395" transform="rotate(0 300 420)" />
<line x1="300" y1="390" x2="300" y2="395" transform="rotate(90 300 420)" />
<line x1="300" y1="390" x2="300" y2="395" transform="rotate(180 300 420)" />
<line x1="300" y1="390" x2="300" y2="395" transform="rotate(270 300 420)" />
</g>
<line x1="300" y1="420" x2="300" y2="395" stroke="#333" stroke-width="1" transform="rotate(45 300 420)" />
<circle cx="300" cy="420" r="2" fill="#333" />
</g>

<!-- Hands -->
<!-- Hour Hand (near 10 o'clock) -->
<g id="hour-hand">
<polygon points="300,300 290,200 300,190 310,200" fill="#333" stroke="#111" stroke-width="1" />
</g>
<!-- Minute Hand (near 2 o'clock) -->
<g id="minute-hand">
<polygon points="300,300 295,150 300,140 305,150" fill="#333" stroke="#111" stroke-width="1" />
</g>
<!-- Second Hand (near 7 o'clock) -->
<g id="second-hand">
<line x1="300" y1="300" x2="220" y2="430" stroke="#b22222" stroke-width="1.5" />
<circle cx="300" cy="300" r="3" fill="#b22222" />
</g>

<!-- Center Pin -->
<circle cx="300" cy="300" r="5" fill="#d4af37" stroke="#886600" stroke-width="1" />
</g>

<!-- Movement (Visible through cutaway at bottom) -->
<g id="movement" opacity="0.9">
<!-- Cutaway background -->
<path d="M 150 350 Q 300 450 450 350 L 450 500 L 150 500 Z" fill="#222" stroke="#555" stroke-width="2" />

<!-- Gears -->
<!-- Large Gear -->
<g transform="translate(250, 420)">
<circle cx="0" cy="0" r="40" fill="none" stroke="#d4af37" stroke-width="8" stroke-dasharray="6 4" />
<circle cx="0" cy="0" r="30" fill="#aa7c11" />
<circle cx="0" cy="0" r="10" fill="#d4af37" />
</g>
<!-- Medium Gear -->
<g transform="translate(350, 400)">
<circle cx="0" cy="0" r="25" fill="none" stroke="#d4af37" stroke-width="6" stroke-dasharray="4 3" />
<circle cx="0" cy="0" r="18" fill="#aa7c11" />
<circle cx="0" cy="0" r="6" fill="#d4af37" />
</g>
<!-- Small Gear -->
<g transform="translate(300, 460)">
<circle cx="0" cy="0" r="15" fill="none" stroke="#d4af37" stroke-width="4" stroke-dasharray="3 2" />
<circle cx="0" cy="0" r="10" fill="#aa7c11" />
<circle cx="0" cy="0" r="4" fill="#d4af37" />
</g>

<!-- Balance Wheel (Bottom Right) -->
<g transform="translate(400, 450)">
<circle cx="0" cy="0" r="20" fill="none" stroke="#d4af37" stroke-width="2" />
<circle cx="0" cy="0" r="18" fill="none" stroke="#aa7c11" stroke-width="1" />
<line x1="-20" y1="0" x2="20" y2="0" stroke="#d4af37" stroke-width="1" />
<line x1="0" y1="-20" x2="0" y2="20" stroke="#d4af37" stroke-width="1" />
</g>
</g>

</svg>

## Iteration history
- iter 0: Draw the complete mechanical pocket watch including the brass case, crown, detailed dial with Roman numerals and hands, sub-dials, visible movement gears, and chain. → Initial full SVG generation of the pocket watch.
