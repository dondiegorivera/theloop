---
adapter: svg
max_iters: 10
score_threshold: 0.9
no_improvement_for: 5
---

# Mechanical Pocket Watch

Draw a detailed mechanical pocket watch, viewed from the front, centered in a 600×600 viewBox.
The watch must include ALL of the following:

## Case & Crown
- A circular outer case (radius ~200) with a metallic gradient fill
- A crown (winder knob) at the top (12 o'clock position) attached to a short stem that extends clearly into the case
- A subtle bezel ring around the outer edge

## Dial
- A white or cream-colored dial face (radius ~170)
- 12 hour markers: thick lines at 12, 3, 6, 9 o'clock; thinner lines at the other hours
- **Roman numerals (I through XII)** positioned just inside the hour markers around the entire perimeter. Use bold, serif-style numerals. Do not use brand names or other text in this area.
- Minute tick marks around the outer edge of the dial (60 ticks, every 6°)

## Hands
- An hour hand (shorter, thicker) pointing near the 10 o'clock position
- A minute hand (longer, thinner) pointing near the 2 o'clock position
- A thin second hand (red or dark) pointing near the 7 o'clock position
- All three hands originating from the exact center of the dial

## Sub-dials
- A small seconds sub-dial at the 6 o'clock position (radius ~30) with its own tiny hand
- A power reserve indicator sub-dial at the 12 o'clock position (radius ~25) with a distinct arc showing ~60% charge

## Movement
- The lower portion of the watch face is open/skeletonized to reveal the movement gears beneath the dial area
- At least 3 visible gears of different sizes with teeth, positioned in the bottom half of the watch
- The gears should overlap realistically and show different sizes (large, medium, small)
- A balance wheel visible near the bottom-right of the movement area

## Chain
- A **detailed gold chain** consisting of 3-4 distinct links attached to the crown, curving upward and outward from the top of the watch.

## Style
- Metallic/brass color palette for the case and gears
- Clean line art with subtle shading
- The entire composition must be centered and balanced
- The SVG must parse as valid XML

The result should look like a realistic, detailed illustration of a vintage mechanical pocket watch — not a cartoon or simplified icon.

## Iteration history
- iter 0: Clarified movement visibility for front view and cleaned formatting → executable spec ready for first drawing
- iter 1: Add missing Chain, Roman Numerals, and Power Reserve indicator; complete hour markers → artifact with all named elements present
- iter 2: Add missing chain and Roman numerals → artifact with complete named elements
- iter 3: Add missing Chain and Roman numerals → artifact with complete named elements
- iter 4: Refine requirements for Roman numerals and chain to prevent omission → artifact with complete named elements