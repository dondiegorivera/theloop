---
adapter: svg
max_iters: 4
score_threshold: 0.85
no_improvement_for: 3
---

# Pelican on a bicycle

Draw an SVG of a pelican riding a bicycle. The pelican should be
recognizable as a pelican (long beak, throat pouch, large body). The
bicycle should have two wheels of similar size, a frame, and handlebars.
The composition should suggest the pelican is actually pedaling — feet
near the pedals, posture leaning slightly forward.

Style is up to you. Flat colors, line art, or a mix all fine. Keep it on
a clean background. The SVG must parse as XML and render in any modern
browser.

## Strict Requirements
- Must contain exactly one pelican and one bicycle as the central subjects.
- No abstract shapes, concentric circles, arrows, or decorative filler unrelated to the scene.
- Canvas size: 800x600. Center the composition.
- Use explicit `<g>` tags with descriptive IDs for each major component (e.g., `<g id="bicycle-frame">`, `<g id="pelican-body">`).
- All elements must be properly closed and valid XML.

## Iteration history
- iter 0: Establish initial SVG structural scaffolding and layering guidelines to ensure valid XML and recognizable composition. → Provide a clear blueprint for the director to generate a parseable, well-proportioned SVG.
- iter 1: Add explicit subject checklist and strict anti-filler constraints to prevent off-topic abstract outputs. → Force the coder to render the exact requested scene with clear structural anchors.
