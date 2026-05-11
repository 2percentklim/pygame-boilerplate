import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE

def set_up_display():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)
    return screen

def set_window_icon(icon_path=None):
    if icon_path is None:
        icon_path = './assets/Boilerplate-Icon-32.png'  # Path to your icon image
    icon_surface = pygame.image.load(icon_path)
    pygame.display.set_icon(icon_surface)