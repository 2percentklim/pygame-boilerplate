import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def set_up_display():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Pygame Boilerplate')
    return screen

# Initialize Pygame
pygame.init()

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
        
        # Handle fullscreen toggle
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            fullscreen = not fullscreen
            if fullscreen:
                screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            else:
                screen = pygame.display.set_mode((0, 0))
                screen = set_up_display()

    screen.fill((30, 30, 30))  # Fill the screen with a dark color

    # Draw everything here

    pygame.display.flip()
    game_clock.tick(60)  # Limit to 60 FPS

pygame.quit()
sys.exit()
