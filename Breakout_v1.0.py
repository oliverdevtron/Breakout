# Breakout v1.0 
# designed by:
#   ██████  ██       ██  ██    ██ ███████ ██████  
#  ██    ██ ██       ██  ██    ██ ██      ██   ██ 
#  ██    ██ ██       ██  ██    ██ █████   ██████  
#  ██    ██ ██       ██   ██  ██  ██      ██   ██ 
#   ██████  ███████  ██    ████   ███████ ██   ██ 
# (c) 2025 by oliver@devtron.pro
import pygame
import sys
import random
import time # Import time module for better countdown

# Pygame initialisieren
pygame.init()

# Bildschirmgröße & Display
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

# Farben
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)
YELLOW  = (255, 255, 0)
ORANGE  = (255, 165, 0)

# Schwierigkeitsgrade
difficulty_settings = {
    1: {"paddle_width": 120, "paddle_speed": 6, "ball_speed": 4, "brick_rows": 4},
    2: {"paddle_width": 100, "paddle_speed": 7, "ball_speed": 5, "brick_rows": 5},
    3: {"paddle_width": 80,  "paddle_speed": 8, "ball_speed": 6, "brick_rows": 6},
}
difficulty = 1

def apply_difficulty():
    """Setzt Parameter entsprechend dem gewählten Schwierigkeitsgrad."""
    global paddle_width, paddle_speed, brick_rows_base
    global ball_speed_x, ball_speed_y

    settings = difficulty_settings[difficulty]
    paddle_width = settings["paddle_width"]
    paddle_speed = settings["paddle_speed"]
    brick_rows_base = settings["brick_rows"]

    # Reset paddle size and position
    paddle_rect.width = paddle_width
    paddle_rect.centerx = WIDTH // 2
    paddle_rect.bottom = HEIGHT - 20

    base_speed = settings["ball_speed"]
    ball_speed_x = base_speed * random.choice([-1, 1])
    ball_speed_y = -base_speed

# Schriftart
try:
    font = pygame.font.Font(None, 36)
except pygame.error as e:
    print(f"Error loading default font: {e}")
    # Fallback or exit if font is crucial
    font = pygame.font.SysFont("Arial", 36) # Example fallback

# Clock
clock = pygame.time.Clock()

# Spielzustände: "difficulty" (Auswahl), "start" (Countdown), "playing" und "gameover"
state = "difficulty"
start_sequence = ["Prepare for liftoff in 3...", "Prepare for liftoff in 2...", "Prepare for liftoff in 1...", "BLAST OFF!"]
start_display_index = 0 # Index for the current message
start_time = 0 # Timestamp when the current message started

# Punktestand und Level
score = 0
level = 1

# Paddle-Spezifikationen
paddle_width, paddle_height = 100, 20
paddle_speed = 7
paddle_rect = pygame.Rect((WIDTH - paddle_width) // 2, HEIGHT - paddle_height - 20, paddle_width, paddle_height)

# Ball-Spezifikationen
ball_radius = 10
ball_x = WIDTH // 2
ball_y = paddle_rect.top - ball_radius - 1
ball_speed_x = 4
ball_speed_y = -4
ball_rect = pygame.Rect(0, 0, ball_radius * 2, ball_radius * 2) # Initialize ball_rect once

# Brick-Spezifikationen
brick_rows_base = 5
brick_columns = 8
brick_width = 60
brick_height = 20
brick_padding = 5
brick_offset_top = 50
brick_offset_left = (WIDTH - (brick_columns * brick_width + (brick_columns - 1) * brick_padding)) // 2
brick_colors = [RED, GREEN, BLUE, YELLOW, ORANGE]

# Store bricks and their rects separately for optimization
bricks = [] # List of (rect, color) tuples
brick_rects = [] # List of just the rects for collision detection

def create_bricks():
    """Erstellt die Bricks und füllt bricks und brick_rects."""
    global bricks, brick_rects
    bricks = []
    brick_rects = []
    rows = brick_rows_base + level - 1
    for row in range(rows):
        for col in range(brick_columns):
            x = brick_offset_left + col * (brick_width + brick_padding)
            y = brick_offset_top + row * (brick_height + brick_padding)
            rect = pygame.Rect(x, y, brick_width, brick_height)
            color = brick_colors[row % len(brick_colors)]
            bricks.append((rect, color))
            brick_rects.append(rect) # Add rect to the separate list

def reset_game():
    """Setzt alle spielrelevanten Variablen zurück."""
    global score, level, state, start_display_index, start_time
    global ball_x, ball_y, ball_speed_x, ball_speed_y

    score = 0
    level = 1
    state = "start"
    start_display_index = 0
    start_time = time.time() # Reset start timer

    apply_difficulty()
    ball_x = paddle_rect.centerx
    ball_y = paddle_rect.top - ball_radius - 1

    create_bricks()

# --- Initial Setup ---
apply_difficulty()

# --- Main Game Loop ---
running = True
while running:
    # Delta time for frame-independent movement (optional but good practice)
    dt = clock.tick(60) / 1000.0 # Time since last frame in seconds

    # --- Ereignisbehandlung ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Handle single-press actions here
            if state == "gameover":
                if event.key == pygame.K_r:
                    state = "difficulty"
                elif event.key == pygame.K_q:
                    running = False
            elif state == "difficulty":
                if event.key == pygame.K_1:
                    difficulty = 1
                    reset_game()
                elif event.key == pygame.K_2:
                    difficulty = 2
                    reset_game()
                elif event.key == pygame.K_3:
                    difficulty = 3
                    reset_game()
            # Add other keydown events if needed (e.g., pause)


    # --- Spiel-Logik basierend auf Zustand ---
    keys = pygame.key.get_pressed() # Get key states for continuous actions

    if state == "start":
        current_time = time.time()
        # Display each message for ~1 second
        if current_time - start_time > 1.0:
            start_display_index += 1
            start_time = current_time # Reset timer for the next message

        if start_display_index >= len(start_sequence):
            state = "playing"
            # Give ball initial push when starting
            ball_speed_x = 4 * random.choice([-1, 1])
            ball_speed_y = -4
        # else: still in countdown, logic handled below in drawing section

    elif state == "difficulty":
        pass
    elif state == "playing":
        # --- Paddle-Bewegung ---
        if keys[pygame.K_LEFT] and paddle_rect.left > 0:
            paddle_rect.x -= paddle_speed # Consider using dt: paddle_rect.x -= paddle_speed * dt * 60
        if keys[pygame.K_RIGHT] and paddle_rect.right < WIDTH:
            paddle_rect.x += paddle_speed # Consider using dt: paddle_rect.x += paddle_speed * dt * 60

        # --- Ballposition updaten ---
        # Use dt for frame-independent speed (optional but smoother)
        # ball_x += ball_speed_x * dt * 60 # Multiply by ~60 to keep similar speed scale
        # ball_y += ball_speed_y * dt * 60
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Update ball_rect position *once* per frame
        ball_rect.center = (int(ball_x), int(ball_y))

        # --- Kollision mit den Wänden ---
        if ball_rect.left <= 0:
            ball_rect.left = 0 # Prevent sticking
            ball_speed_x *= -1
            ball_x = ball_rect.centerx # Update logical position
        if ball_rect.right >= WIDTH:
            ball_rect.right = WIDTH # Prevent sticking
            ball_speed_x *= -1
            ball_x = ball_rect.centerx # Update logical position
        if ball_rect.top <= 0:
            ball_rect.top = 0 # Prevent sticking
            ball_speed_y *= -1
            ball_y = ball_rect.centery # Update logical position

        # --- Kollision mit dem Paddle ---
        if ball_rect.colliderect(paddle_rect) and ball_speed_y > 0:
            # More precise collision point handling (optional)
            # distance = ball_x - paddle_rect.centerx
            # percent_width = distance / (paddle_width / 2)
            # ball_speed_x = ball_speed_x + percent_width * 2 # Adjust angle based on hit location

            ball_speed_y = -abs(ball_speed_y) # Bounce up
            ball_y = paddle_rect.top - ball_radius # Place ball just above paddle
            ball_rect.bottom = paddle_rect.top # Update rect position immediately

            # Keep random element if desired
            # ball_speed_x += random.uniform(-1, 1)


        # --- Kollision mit den Bricks ---
        # Use the pre-calculated brick_rects list
        brick_collision_index = ball_rect.collidelist(brick_rects)
        if brick_collision_index != -1:
            hit_brick_rect = brick_rects.pop(brick_collision_index)
            # Find the corresponding (rect, color) tuple in the main bricks list to remove it for drawing
            # This is slightly less efficient but needed if you draw from 'bricks'
            # A dictionary mapping rects to colors might be better if many bricks
            for i, (brick, color) in enumerate(bricks):
                if brick == hit_brick_rect:
                    bricks.pop(i)
                    break # Found and removed

            # --- Simple bounce (improve this for better physics) ---
            # Check overlap to guess collision side (basic)
            # overlap = ball_rect.clip(hit_brick_rect)
            # if overlap.width > overlap.height: # Likely top/bottom hit
            #    ball_speed_y *= -1
            #    # Move ball out of collision
            #    if ball_rect.centery < hit_brick_rect.centery: # Hit from top
            #        ball_rect.bottom = hit_brick_rect.top
            #    else: # Hit from bottom
            #        ball_rect.top = hit_brick_rect.bottom
            # else: # Likely side hit
            #    ball_speed_x *= -1
            #    # Move ball out of collision
            #    if ball_rect.centerx < hit_brick_rect.centerx: # Hit from left
            #        ball_rect.right = hit_brick_rect.left
            #    else: # Hit from right
            #        ball_rect.left = hit_brick_rect.right

            # Original simple bounce:
            ball_speed_y *= -1

            # Update logical position after collision adjustment
            ball_x, ball_y = ball_rect.centerx, ball_rect.centery

            score += 10

        # --- Prüfen, ob der Ball den Bildschirm unten verlassen hat ---
        if ball_rect.top > HEIGHT: # Check top edge for consistency
            state = "gameover"

        # --- Level abgeschlossen: Alle Bricks zerstört ---
        if not brick_rects: # Check the rect list now
            level += 1
            # Ballgeschwindigkeit leicht erhöhen (ensure speed increases)
            speed_increase_factor = 1.1
            ball_speed_x = ball_speed_x * speed_increase_factor
            # Make sure y speed stays negative after increase if it was negative
            ball_speed_y = -abs(ball_speed_y * speed_increase_factor)

            # Paddle und Ball zurücksetzen
            paddle_rect.centerx = WIDTH // 2
            ball_x = paddle_rect.centerx
            ball_y = paddle_rect.top - ball_radius - 1
            # Reset speeds for the start of the level? Or keep increased speed?
            # If keeping increased speed, just reset position. If resetting speed:
            # base_speed = 4 * (1 + (level-1)*0.1) # Example: speed increases per level
            # ball_speed_x = base_speed * random.choice([-1, 1])
            # ball_speed_y = -base_speed

            create_bricks() # Create new bricks for the next level
            state = "start" # Go back to countdown for the new level
            start_display_index = 0
            start_time = time.time()


    # --- Zeichnen ---
    SCREEN.fill(BLACK) # Clear screen first

    if state == "difficulty":
        diff_text = font.render("Select difficulty: 1=Easy 2=Medium 3=Hard", True, WHITE)
        SCREEN.blit(diff_text, ((WIDTH - diff_text.get_width()) // 2,
                                (HEIGHT - diff_text.get_height()) // 2))

    elif state == "start":
        # Draw paddle and ball even during countdown
        pygame.draw.rect(SCREEN, WHITE, paddle_rect)
        # Use the updated ball_rect for drawing
        pygame.draw.circle(SCREEN, WHITE, ball_rect.center, ball_radius)
        # Draw bricks
        for brick, color in bricks:
            pygame.draw.rect(SCREEN, color, brick)

        # Display countdown message
        if start_display_index < len(start_sequence):
            text = start_sequence[start_display_index]
            rendered_text = font.render(text, True, WHITE)
            SCREEN.blit(rendered_text, ((WIDTH - rendered_text.get_width()) // 2,
                                        (HEIGHT - rendered_text.get_height()) // 2))

    elif state == "gameover":
        # Game Over-Bildschirm mit Restart-/Quit-Option
        game_over_text = font.render("Game Over!", True, WHITE)
        final_score_text = font.render(f"Final Score: {score}", True, WHITE)
        restart_text = font.render("Press R to restart or Q to quit", True, WHITE)

        text_y = HEIGHT // 2 - game_over_text.get_height() - 10 # Start position for text block
        SCREEN.blit(game_over_text, ((WIDTH - game_over_text.get_width()) // 2, text_y))
        text_y += game_over_text.get_height() + 5
        SCREEN.blit(final_score_text, ((WIDTH - final_score_text.get_width()) // 2, text_y))
        text_y += final_score_text.get_height() + 20
        SCREEN.blit(restart_text, ((WIDTH - restart_text.get_width()) // 2, text_y))

    elif state == "playing":
        # Zeichne Paddle, Ball & Bricks
        pygame.draw.rect(SCREEN, WHITE, paddle_rect)
        # Use the updated ball_rect for drawing
        pygame.draw.circle(SCREEN, WHITE, ball_rect.center, ball_radius)
        for brick, color in bricks:
            pygame.draw.rect(SCREEN, color, brick)

    # Draw UI (Score, Level) - always visible except maybe game over? Your choice.
    if state != "gameover": # Optionally hide during game over
        score_text = font.render(f"Score: {score}", True, WHITE)
        level_text = font.render(f"Level: {level}", True, WHITE)
        SCREEN.blit(score_text, (10, 10))
        SCREEN.blit(level_text, (WIDTH - level_text.get_width() - 10, 10))

    # --- Bildschirm aktualisieren ---
    pygame.display.flip()

# --- Spiel beenden ---
pygame.quit()
sys.exit()