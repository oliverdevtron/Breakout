# Breakout — Neon Arcade

A modern Breakout game built with HTML5 Canvas and vanilla JavaScript. Features a neon/synthwave aesthetic, particle effects, power-ups, procedural audio, and 5 unique level layouts.

## How to Run

1. Clone the repository
2. Open `index.html` in any modern browser
3. No build tools, dependencies, or servers required

Alternatively, serve with any static file server:
```bash
python3 -m http.server 8000
# Then open http://localhost:8000
```

## Controls

| Input | Action |
|-------|--------|
| Arrow Keys / A,D | Move paddle left/right |
| Mouse | Move paddle (follows cursor) |
| P / Escape | Pause / Resume |
| Click / Space / Enter | Start game, advance menus |

Touch controls are supported for mobile devices.

## Features

### Gameplay
- **5 unique level layouts**: Classic, Diamond, Fortress, Zigzag, and Pyramid — cycling with increasing difficulty
- **Power-up system**: Multi-Ball, Wide Paddle, Slow Ball, Extra Life — dropping randomly from broken bricks
- **Combo scoring**: Hit multiple bricks without the ball touching the paddle to build a score multiplier
- **3 lives** with visual heart indicators
- **Pause/resume** functionality

### Audio
- Fully procedural sound effects via Web Audio API — no external audio files
- Unique sounds for brick breaks, paddle hits, wall bounces, power-ups, combos, level complete, and game over

### Visuals
- Neon/synthwave color palette with glow effects
- Gradient bricks with hit-point indicators for multi-hit bricks
- Particle explosions on brick destruction
- Ball trail effects and spark particles on bounces
- Animated starfield background with parallax layers
- Screen shake on impacts
- Smooth state transitions (countdown, level complete, game over)
- Custom font (Orbitron from Google Fonts)

### Technical
- Fixed-timestep game loop (60Hz physics) with accumulator pattern
- Object-pooled particle system (600 particles)
- AABB collision detection with side determination
- Paddle hit position affects ball angle
- Clean separation: Constants, Audio Engine, Particle System, Game Objects, Level Definitions, Input Handler, Game Engine, Renderer
- Pure vanilla JavaScript — no frameworks, no build tools, no npm
- Single HTML file — fully self-contained

## Screenshots

To take a screenshot:
1. Open the game in your browser
2. Use your OS screenshot tool (or browser DevTools > Capture screenshot)
3. Save as `screenshot.png` in the project root

## File Structure

```
├── index.html         # Complete game (HTML + CSS + JS)
├── Breakout_v1.0.py   # Original Pygame prototype
├── CODE_REVIEW.md     # Detailed code review and feature documentation
├── README.md          # This file
└── CLAUDE.md          # Agent instructions
```

## Credits

Original game design by Oliver (oliver@devtron.pro).
Rewritten as HTML5 Canvas with modern features and neon arcade aesthetic.
