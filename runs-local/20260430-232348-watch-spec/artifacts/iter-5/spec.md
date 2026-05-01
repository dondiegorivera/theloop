---
adapter: svg
max_iters: 10
score_threshold: 0.95
no_improvement_for: 7
---

# Mechanical Pocket Watch
Draw a detailed mechanical pocket watch, viewed from the front, centered in a 600×600 viewBox. The watch must include ALL of the following:

## Case & Crown
- A circular outer case (radius ~200) with a metallic gradient fill
- A crown (winder knob) at the top (12 o'clock position) attached to a short stem that extends visibly into the case
- A subtle bezel ring around the outer edge

## Dial
- A white or cream-colored dial face (radius ~170)
- 12 hour markers: thick lines at 12, 3, 6, 9 o'clock; thinner lines at the other hours. **Ensure the 6 o'clock marker is clearly visible and distinct from the sub-dial.**
- Roman numerals (I through XII) positioned just inside the hour markers. **Ensure "XII" is visible at the 12 o'clock position, integrated with or around the power reserve sub-dial.**
- Minute tick marks around the outer edge of the dial (60 ticks, every 6°)

## Hands
- An hour hand (shorter, thicker) pointing near the 10 o'clock position
- A minute hand (longer, thinner) pointing near the 2 o'clock position
- A thin second hand (red or dark) pointing near the 7 o'clock position
- All three hands originating from the exact center of the dial

## Sub-dials
- A small seconds sub-dial at the 6 o'clock position (radius ~30) with its own tiny hand
- A power reserve indicator sub-dial at the 12 o'clock position (radius ~25) with a needle and an arc clearly showing approximately 60% charge (216 degrees), resembling a standard mechanical gauge

## Movement (visible through caseback or cutaway)
- At least 3 visible gears of distinctly different sizes (large, medium, small) with teeth, positioned below the dial area (bottom half of the watch)
- The gears should overlap realistically and show different sizes
- A balance wheel visible near the bottom-right of the movement area

## Chain
- A short chain (3-4 links) attached to the crown, curving upward and outward from the top of the watch. **The chain must consist of physically interlocking oval links that are connected to each other and anchored to the crown stem.** Draw the links as overlapping ellipses forming a continuous curve, ensuring no gaps between links and a solid connection to the stem.

## Style
- Metallic/brass color palette for the case and gears
- Clean line art with subtle shading
- The entire composition must be centered and balanced
- The SVG must parse as valid XML

The result should look like a realistic, detailed illustration of a vintage mechanical pocket watch — not a cartoon or simplified icon.

## Iteration history
- iter 0: Draw a detailed mechanical pocket watch, front view, centered in 600x600, including case, dial, hands, sub-dials, movement, and chain. → First credible attempt at the subject.
- iter 1: Replace Arabic numerals with Roman numerals I-XII and add a distinct balance wheel near the bottom-right of the movement area. → Improved accuracy of dial markings and movement details.
- iter 2: Replace floating circles with a connected chain attached to the crown and clarify power reserve and gear size requirements. → Fix missing chain element and refine partial elements.
- iter 3: Redesign power reserve sub-dial with needle and 216-degree arc to clearly show 60% charge. → Fix partial power reserve indicator.
- iter 4: Redraw chain as interlocking links anchored to crown; update power reserve to show 216-degree arc; ensure 6 o'clock marker is visible. → Fix chain connection, power reserve arc, and missing 6 o'clock marker.
- iter 5: Refine chain geometry to ensure continuous interlocking links anchored to the stem and replace floating ovals. → Fix missing chain element by enforcing connectivity and overlap.

## Previous critique
The chain is classified as MISSING because the artifact contains only disconnected floating ovals rather than the required physically interlocking links anchored to the crown. This is a hard constraint failure for a named subject element. The single most impactful next change is to replace the floating ovals with a continuous path or properly overlapping ellipses that visually connect to the crown stem and each other.

## Previous element-by-element description
## Required elements
- **Circular outer case**: PRESENT — A large circular brass-colored ring (radius ~200px) encloses the dial, centered in the 600x600 viewBox.
- **Metallic gradient fill**: PRESENT — The case and gears exhibit a gold/brass linear gradient with shading to simulate metallic reflection.
- **Crown at 12 o'clock**: PRESENT — A golden knob is positioned at the top center (12 o'clock), attached to a stem extending into the case.
- **Stem extending visibly**: PARTIAL — The stem connects the crown to the dial, but it appears to terminate abruptly at the dial surface without clearly penetrating "into" the case depth.
- **Subtle bezel ring**: PRESENT — A distinct inner rim separates the outer case from the dial face.
- **White/cream-colored dial**: PRESENT — The background of the dial is a cream/off-white radial gradient.
- **12 hour markers (thick at 12,3,6,9)**: PARTIAL — Markers are present at all hours. However, the 12 o'clock marker is visually obscured by the power reserve sub-dial, and the 6 o'clock marker is partially occluded by the small seconds sub-dial.
- **Roman numerals (I-XII)**: PRESENT — Roman numerals are visible around the dial perimeter. "XII" is present but sits directly behind/under the power reserve sub-dial.
- **Minute tick marks**: PRESENT — A ring of 60 fine ticks is visible along the outer edge of the dial.
- **Hour hand (near 10)**: PRESENT — The short, thick black hand points clearly to the 10 o'clock position.
- **Minute hand (near 2)**: PRESENT — The longer, thinner black hand points clearly to the 2 o'clock position.
- **Second hand (near 7)**: PRESENT — A thin red hand points towards the 7 o'clock position.
- **Hands originating from center**: PRESENT — All three hands pivot from the exact geometric center of the dial.
- **Small seconds sub-dial at 6**: PRESENT — A small circular dial is located at the bottom (6 o'clock) with its own hand.
- **Power reserve sub-dial at 12**: PRESENT — A sub-dial is located at the top (12 o'clock).
- **Power reserve arc (~60%)**: PARTIAL — The sub-dial shows a red arc, but it appears to cover roughly 90 degrees (25% charge) rather than the required 216 degrees (60%).
- **Movement gears (3+ visible)**: PRESENT — Three distinct gears of varying sizes are visible in the bottom half of the watch.
- **Balance wheel**: PARTIAL — A gear-like structure is visible at the bottom right, but it lacks the distinctive large rim and spokes of a traditional balance wheel; it looks more like a standard gear.
- **Chain (3-4 links)**: MISSING — The artifact shows three small floating ovals above the crown that do not connect to each other or the stem. There is no interlocking chain structure.

## Other observations
The overall composition is visually striking and resembles a high-quality illustration of a "Huntress" style pocket watch. However, there are significant structural deviations from the spec: the power reserve indicator shows a quarter charge instead of 60%, and the chain is represented by disconnected floating shapes rather than interlocking links. The movement gears are visible but lack the specific detail of a balance wheel.
