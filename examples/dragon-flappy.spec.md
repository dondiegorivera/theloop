---
adapter: web
max_iters: 6
score_threshold: 0.85
no_improvement_for: 3
---

# Dragon flappy-bird in three.js

Build a 3D flappy-bird-style game with a dragon as the player character,
using three.js (the global `THREE` is already loaded from CDN in the
scaffold). Mechanics:

- Tap or press space to flap. The dragon gains upward velocity per flap;
  gravity pulls it down between flaps.
- Procedural pipe-like obstacles spawn on the right and scroll left at a
  steady pace; gaps between top and bottom segments are randomized.
- Score counter at the top-left, incremented when the dragon clears a
  pipe pair.
- A game-over screen with a "restart" button (or a key hint to restart)
  appears when the dragon collides with a pipe or the ground.

Visual:
- Camera looks at the dragon from a slight 3D angle (not pure side-view);
  z-depth must be visible. Distinct sky background, ground plane.
- The dragon should be recognizable as a dragon at a glance — wings,
  body, tail. Stylized geometry is fine; photorealism is not the goal.

Technical:
- Set `window.__ready = true` inside the first `renderer.render()` call,
  so theloop's screenshot captures an actual rendered frame.
- No uncaught console errors during normal play.
