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
- A crown (winder knob) at the top (12 o'clock position) attached to a short stem that extends into the case
- A subtle bezel ring around the outer edge

## Dial
- A white or cream-colored dial face (radius ~170)
- 12 hour markers: thick lines at 12, 3, 6, 9 o'clock; thinner lines at the other hours
- Roman numerals (I through XII) positioned just inside the hour markers
- Minute tick marks around the outer edge of the dial (60 ticks, every 6°) with increased visibility (opacity 0.8, stroke-width 1.5px) to ensure they are clearly distinct against the cream dial

## Hands
- An hour hand (shorter, thicker) pointing precisely near the 10 o'clock position (approx. 300° from vertical)
- A minute hand (longer, thinner) pointing precisely near the 2 o'clock position (approx. 60° from vertical)
- A thin second hand (red or dark) pointing near the 7 o'clock position
- All three hands originating from the exact center of the dial

## Sub-dials
- A small seconds sub-dial at the 6 o'clock position (radius ~30) featuring a proper seconds track (e.g., 5-second intervals) and its own tiny hand
- A power reserve indicator sub-dial at the 12 o'clock position (radius ~25) with a distinct graphical arc showing ~60% charge (must be a graphical arc, not text)

## Movement (visible through caseback or cutaway)
- At least 3 visible gears of different sizes with teeth, positioned below the dial area (bottom half of the watch, y > 400)
- The gears should overlap realistically and show different sizes (large, medium, small)
- A balance wheel visible near the bottom-right of the movement area (approx coordinates 550, 550), depicted as a large wheel with a hairspring
- **Crucial:** Gears must have high opacity (near 1.0) and be rendered *after* the dial layer so they are clearly visible in the bottom half, not obscured by the dial face.

## Chain
- A short chain (3-4 links) attached to the crown, curving upward and outward from the top of the watch

## Style
- Metallic/brass color palette for the case and gears
- Clean line art with subtle shading
- The entire composition must be centered and balanced
- The SVG must parse as valid XML

The result should look like a realistic, detailed illustration of a vintage mechanical pocket watch — not a cartoon or simplified icon.

## Iteration history
- iter 1: Discard generic logo and generate detailed pocket watch with case, dial, hands, gears, and chain.
- iter 2: Add distinct power reserve arc sub-dial at 12 o'clock and move movement gears to bottom half with high opacity and visible teeth.
- iter 3: Increase gear opacity to near 1.0 and ensure correct layering so gears are visible below the dial; replace brand text at 12 o'clock with a graphical arc sub-dial showing ~60% charge.
- iter 4: Correct hand positions to 10:00 and 2:00 angles and add the missing balance wheel assembly in the bottom-right movement area.
- iter 5: Increase minute tick mark visibility (opacity 0.8, stroke 1.5px) and replace non-standard numerals in the 6 o'clock sub-dial with a proper seconds track to match the specification.
- iter 6: Remove text from power reserve sub-dial to strictly enforce graphical-only constraint.