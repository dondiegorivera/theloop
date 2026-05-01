---
adapter: svg
max_iters: 8
score_threshold: 0.9
no_improvement_for: 5
---
# Mechanical Pocket Watch

Draw a detailed mechanical pocket watch, viewed from the front, centered in a 600×600 viewBox. The watch must include ALL of the following:

## Case & Crown
- A circular outer case (radius ~200) with a metallic gradient fill
- A crown (winder knob) at the top (12 o'clock position) attached to a short stem that extends into the case
- A subtle bezel ring around the outer edge

## Dial
- A white or cream-colored dial face (radius ~170)
- 12 hour markers: thick lines at 12, 3, 6, 9 o'clock; thinner lines at the other hours
- Roman numerals (I through XII) positioned just inside the hour markers
- 60 minute tick marks around the outer edge of the dial, spaced every 6°

## Hands
- An hour hand (shorter, thicker) rotated to exactly ~305° (10 o'clock position)
- A minute hand (longer, thinner) rotated to exactly ~60° (2 o'clock position)
- A thin second hand (red or dark) rotated to exactly ~210° (7 o'clock position)
- All three hands must originate from the exact center of the dial (300, 300) and be layered correctly (second on top)

## Sub-dials
- A power reserve indicator sub-dial at the 12 o'clock position (radius ~25) featuring a visible arc indicating approximately 60% charge
- A small seconds sub-dial at the 6 o'clock position (radius ~30) with its own tiny hand

## Movement (visible through caseback or cutaway)
- At least 3 visible gears of different sizes with teeth, strictly positioned in the bottom half of the watch below the dial area (y > 300)
- The gears should overlap realistically and show different sizes (large, medium, small)
- A balance wheel clearly visible near the bottom-right of the movement area

## Chain
- A short chain (3-4 links) attached to the crown, curving distinctly upward and outward from the top of the watch rather than hanging vertically

## Style
- Metallic/brass color palette for the case and gears
- Clean line art with subtle shading
- The entire composition must be centered and balanced
- The SVG must parse as valid XML

The result should look like a realistic, detailed illustration of a vintage mechanical pocket watch — not a cartoon or simplified icon.

## Iteration history
- iter 0: Draft initial pocket watch spec with case, dial, hands, sub-dials, movement, chain, and style requirements → establish baseline for SVG generation.
- iter 1: Correct spatial layout and component positioning by repositioning gears to the bottom half, angling hands to ~10 and ~2 o'clock, adding the power reserve arc, and curving the chain upward → align composition with explicit spec requirements.
- iter 2: Enforce exact hand angles, confine movement components strictly to the bottom half, add minute tick marks, and correct sub-dial/chain positioning → resolve critical structural and positional failures identified in critique.