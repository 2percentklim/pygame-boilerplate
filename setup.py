
from pathlib import Path

import pygame
from constants import DESIGN_WIDTH, DESIGN_HEIGHT, GAME_TITLE

def set_window_icon(icon_path=None):
    if icon_path is None:
        icon_path = Path(__file__).resolve().parent / 'assets' / 'Boilerplate-Icon-32.png'
    icon_surface = pygame.transform.scale(pygame.image.load(icon_path), (32, 32))
    pygame.display.set_icon(icon_surface)

def set_up_display(icon_path=None):
    set_window_icon(icon_path)
    pygame.display.set_caption(GAME_TITLE)
    screen = pygame.display.set_mode(
        (int(DESIGN_WIDTH), int(DESIGN_HEIGHT)),
        pygame.RESIZABLE,
    )   
    return screen

# This works but is "janky" when returning to windowed mode
def toggle_fullscreen(screen, fullscreen):
    fullscreen = not fullscreen
    if fullscreen:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(
            (int(DESIGN_WIDTH), int(DESIGN_HEIGHT)),
            pygame.RESIZABLE,
        )
    return screen, fullscreen

