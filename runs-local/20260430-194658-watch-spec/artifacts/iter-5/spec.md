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
- A crown (winder knob) at the top (12 o'clock position) attached to a short stem that extends clearly into the case structure
- A subtle bezel ring around the outer edge

## Dial
- A white or cream-colored dial face (radius ~170)
- 12 hour markers: thick lines at 12, 3, 6, 9 o'clock; thinner lines at the other hours
- Roman numerals (I through XII) positioned just inside the hour markers, rendered as clean vector paths or crisp standard serif text (no rasterized or low-resolution text)
- **Minute tick marks: Render exactly 60 thin lines spaced at precise 6° intervals around the outer edge of the dial. These must be clearly visible, distinct, and form a complete unbroken ring of ticks. Do not omit any ticks.**

## Hands
- An hour hand (shorter, thicker) pointing near the 10 o'clock position
- A minute hand (longer, thinner) pointing near the 2 o'clock position
- A thin second hand (red or dark) pointing near the 7 o'clock position
- **All three hands must originate from the exact geometric center of the dial (300, 300), with perfectly aligned pivots sharing the same center point.**

## Sub-dials
- A small seconds sub-dial at the 6 o'clock position (radius ~30) with its own tiny hand
- **Power reserve indicator at the 12 o'clock position (radius ~25): Draw a filled arc clearly showing approximately 60% charge (roughly 216° filled). Do not use text labels to indicate charge; the arc itself must represent the level. Ensure the arc is distinct and clearly visible.**

## Movement (visible through caseback or cutaway)
- At least 3 visible gears of different sizes with clearly rendered teeth, positioned below the dial area (bottom half of the watch)
- The gears should overlap realistically and show different sizes (large, medium, small)
- A balance wheel: a distinct, large circular rim (radius ~40) positioned clearly in the bottom-right movement area
- **Hairspring: Draw a clearly visible, separate coiled hairspring spiral as a distinct, continuous expanding spiral path attached to the balance wheel center. Ensure it is unmistakably present, legible, and not obscured by other elements.**

## Chain
- A short chain (3-4 links) attached to the crown, curving upward and outward from the top of the watch

## Style
- Metallic/brass color palette for the case and gears
- Clean line art with subtle shading
- The entire composition must be centered and balanced
- The SVG must parse as valid XML

The result should look like a realistic, detailed illustration of a vintage mechanical pocket watch — not a cartoon or simplified icon.

## Iteration history
- iter 0: Establish complete, unambiguous visual specification for direct SVG generation → Ready for director to produce initial pocket watch illustration.
- iter 1: Explicitly define the missing balance wheel with hairspring, enforce exact center pivot alignment for all hands, and mandate precise 60-minute tick marks → Resolve MISSING balance wheel and PARTIAL alignment/ticks to meet core mechanical accuracy requirements.
- iter 2: Redraw the balance wheel and hairspring with a distinct circular rim and separate coiled spiral in the bottom-right movement area → Ensure the balance wheel assembly is unmistakably present and legible, resolving the PARTIAL classification.
- iter 3: Add the 60 minute tick marks, replace the power reserve label with an arc, and redraw the hairspring as a distinct spiral → Resolve PARTIAL Dial, Sub-dials, and Movement elements by adding missing ticks, correcting the power reserve visualization, and clarifying the hairspring.
- iter 4: Reinforce rendering of 60-minute tick marks, hairspring, and power reserve arc with explicit negative constraints against omission or text labels → Ensure critical mechanical details are drawn and visible.
- iter 5: Add the missing hairspring spiral, remove power reserve text labels, fix Roman numerals to clean vector style, and ensure perfect hand alignment → Resolve MISSING hairspring, PARTIAL power reserve/alignment/numerals defects.