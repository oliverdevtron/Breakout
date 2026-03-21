# Neon Breakout

A modern Breakout game with neon synthwave aesthetics, built with pure HTML5 Canvas and vanilla JavaScript. No dependencies, no build tools - just open and play.

**Original concept**: Breakout v1.0 by [oliver@devtron.pro](mailto:oliver@devtron.pro)

## Features

- **5 unique levels** with distinct brick layouts and increasing difficulty
- **Multi-HP bricks** that take multiple hits to destroy
- **Power-up system**: Multi-Ball, Wide Paddle, Speed Ball, Extra Life
- **Combo scoring**: Consecutive brick hits without paddle touches build a score multiplier
- **Particle effects**: Brick explosions, ball trails, paddle sparks
- **Procedural audio**: All sound effects generated with Web Audio API (no files needed)
- **3 lives** with visual heart indicators
- **Pause/resume** with P or Escape
- **High score tracking** (in-memory, per session)
- **Neon/synthwave aesthetic** with glow effects, animated starfield, and grid background
- **Responsive input**: Keyboard, mouse, and touch support
- **Fixed-timestep physics** at 120Hz for consistent gameplay

## How to Run

Open `index.html` in any modern browser. That's it.

```bash
# Option 1: Just open the file
open index.html
# or double-click index.html in your file manager

# Option 2: Local server (if you prefer)
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Controls

| Input | Action |
|---|---|
| Arrow Keys (← →) | Move paddle |
| A / D | Move paddle (alternative) |
| Mouse / Touch | Move paddle to cursor position |
| P / Escape | Pause / Resume |
| Click / Space / Enter | Start game, navigate menus |

## Game Rules

1. **Break all bricks** to advance to the next level.
2. **Don't let the ball fall** below the paddle - you lose a life.
3. **Catch power-ups** that drop from broken bricks for bonuses.
4. **Build combos** by hitting bricks consecutively without the ball touching the paddle. Every 3 hits increases the score multiplier by 0.5x.
5. **Complete all 5 levels** to win.

## Levels

1. **INITIATION** - Classic rows, warm-up level
2. **DIAMOND** - Diamond formation with reinforced center
3. **FORTRESS** - Walled structure requiring precision
4. **CHECKMATE** - Checkerboard with tough intersections
5. **GAUNTLET** - Dense 8-row endurance test

## Power-Ups

| Icon | Name | Effect |
|---|---|---|
| **M** | Multi-Ball | Spawns 2 extra balls |
| **W** | Wide Paddle | 50% wider paddle for 10 seconds |
| **S** | Speed Ball | 40% faster ball for 10 seconds |
| **+** | Extra Life | Adds one life (max 5) |

## Tech Stack

- HTML5 Canvas for rendering
- Vanilla JavaScript (ES6+, strict mode)
- Web Audio API for procedural sound
- Google Fonts (Orbitron, Rajdhani)
- Fixed-timestep game loop with requestAnimationFrame
- Object-pooled particle system (500 particles)

## File Structure

```
├── index.html          # Complete game (single file)
├── Breakout_v1.0.py    # Original Python/Pygame version
├── CODE_REVIEW.md      # Detailed code review and changelog
└── README.md           # This file
```

## Browser Support

Works in all modern browsers (Chrome, Firefox, Safari, Edge). Requires JavaScript enabled and Web Audio API support.
