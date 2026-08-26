
import pygame
import sys
from constants import DEFAULT_COLOR
from setup import set_up_display, set_window_icon

# Initialize Pygame
pygame.init()

# Set window icon
# Pass None to use the default icon path, or specify a path to your custom icon image
set_window_icon(None)

# Set up display
screen = set_up_display()

# Set up clock
game_clock = pygame.time.Clock()

# Main game loop
fullscreen = False

running = True
while running:
    for event in pygame.event.get():

        # Handle QUIT event
        if event.type == pygame.QUIT:
            running = False

    screen.fill(DEFAULT_COLOR)  # Fill the screen with a dark color

    # Draw everything here

    pygame.display.flip()
    game_clock.tick(60)  # Limit to 60 FPS

pygame.quit()
sys.exit()
