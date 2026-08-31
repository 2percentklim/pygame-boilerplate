
import argparse
import sys

import pygame
from constants import DEFAULT_FPS
from setup import set_up_display, toggle_fullscreen
from scenes.StartMenuBuilder import StartMenuBuilder


argument_parser = argparse.ArgumentParser()
argument_parser.add_argument(
    "--grid",
    action="store_true",
    help="Show the 32px scene coordinate grid.",
)
arguments = argument_parser.parse_args()

# Initialize Pygame
pygame.init()

# Set up display
screen = set_up_display()

# Set up clock
game_clock = pygame.time.Clock()

# Create StartMenuBuilder instance
start_menu = StartMenuBuilder(screen, show_grid=arguments.grid)

# Main game loop
fullscreen = False

running = True
while running:
    for event in pygame.event.get():

        # Handle QUIT event
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            screen, fullscreen = toggle_fullscreen(screen, fullscreen)
            start_menu.screen = screen

    start_menu.draw()
    pygame.display.flip()
    game_clock.tick(DEFAULT_FPS)  # Limit to 60 FPS

pygame.quit()
sys.exit()
