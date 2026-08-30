
import pygame
import sys
from constants import DEFAULT_COLOR, DEFAULT_FPS
from setup import set_up_display, set_window_icon
from scenes.StartMenuBuilder import StartMenuBuilder

# Initialize Pygame
pygame.init()

# Set up display
screen = set_up_display()

# Set up clock
game_clock = pygame.time.Clock()

# Create StartMenuBuilder instance
start_menu = StartMenuBuilder(screen)

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
    start_menu.draw()
    pygame.display.flip()
    game_clock.tick(DEFAULT_FPS)  # Limit to 60 FPS

pygame.quit()
sys.exit()
