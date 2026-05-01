---
adapter: svg
max_iters: 10
score_threshold: 0.9
no_improvement_for: 5
---

# Mechanical Pocket Watch

Draw a detailed mechanical pocket watch, viewed from the front, centered in a 600×600 viewBox. The watch must include ALL of the following:

## Case & Crown
- A circular outer case (radius ~200) with a metallic gradient fill
- A crown (winder knob) at the top (12 o'clock position) attached to a short stem that extends visibly into the case
- A subtle bezel ring around the outer edge

## Dial
- A white or cream-colored dial face (radius ~170)
- 12 hour markers: thick lines at 12, 3, 6, 9 o'clock; thinner lines at the other hours
- Roman numerals (I through XII) positioned just inside the hour markers
- Minute tick marks around the outer edge of the dial (60 distinct ticks, every 6°)

## Hands
- An hour hand (shorter, thicker) pointing near the 10 o'clock position
- A minute hand (longer, thinner) pointing near the 2 o'clock position
- A thin second hand (red or dark) pointing near the 7 o'clock position
- All three hands originating from the exact center of the dial

## Sub-dials
- A small seconds sub-dial at the 6 o'clock position (radius ~30) with its own tiny hand
- A power reserve indicator sub-dial at the 12 o'clock position (radius ~25) featuring a visible semi-circular arc track with a needle pointing to the 60% mark

## Movement (visible through caseback or cutaway)
- At least 3 visible gears of different sizes with teeth, positioned below the dial area (bottom half of the watch)
- The gears should overlap realistically and show different sizes (large, medium, small)
- A balance wheel clearly positioned in the bottom-right quadrant (x > 350, y > 400) with a visible hairspring

## Chain
- A short chain (3-4 distinct links) attached to the crown, curving upward and outward from the top of the watch. Each link must be clearly separated and defined.

## Style
- Metallic/brass color palette for the case and gears
- Clean line art with subtle shading
- The entire composition must be centered and balanced
- Output raw SVG code only; do not output images or markdown code fences around the SVG.
- The SVG must parse as valid XML.

The result should look like a realistic, detailed illustration of a vintage mechanical pocket watch — not a cartoon or simplified icon.

## Iteration history
- iter 0: Draw a detailed, realistic mechanical pocket watch in SVG format, centered in a 600x600 viewBox with all specified components. → A complete, valid SVG illustration meeting all case, dial, hands, sub-dials, movement, chain, and style requirements.
- iter 1: Fix hands to ~10:10, add 6 o'clock sub-dial, move gears below dial. → Hands at correct angles, complete sub-dials, gears in movement area.
- iter 2: Move balance wheel to bottom-right, add arc to power reserve, and define chain links. → Balance wheel in correct quadrant, visible arc scale, distinct chain links.