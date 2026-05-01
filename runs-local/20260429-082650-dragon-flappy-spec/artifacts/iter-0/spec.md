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

## Implementation Plan
- **Scene & Camera:** Initialize THREE.Scene, PerspectiveCamera, and WebGLRenderer. Set up lighting (ambient + directional) and a skybox/background color.
- **Player Controller:** Create a group for the dragon (body, wings, tail using basic geometries). Implement physics: velocity, gravity, flap impulse, and ground collision.
- **Obstacle Manager:** Spawn pipe pairs at intervals, move them left by a fixed delta each frame, and remove them when off-screen.
- **Game State & UI:** Manage score, game-over state, and restart logic. Render HTML overlay for score and restart button.
- **Main Loop:** Use requestAnimationFrame to update physics, move obstacles, check collisions, and render. Set `window.__ready = true` on the first frame.

## Iteration history
- iter 0: Initial structural sketch → scaffolding for scene, player physics, obstacle spawning, and game loop to enable a functional first pass.