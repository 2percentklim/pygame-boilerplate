import pygame
from constants import DEFAULT_TITLE_FONT_SIZE, DEFAULT_TITLE_FONT_NAME, DESIGN_WIDTH, DESIGN_HEIGHT, DEFAULT_TEXT_COLOR, GAME_TITLE, DEFAULT_BUTTON_COLOR, DEFAULT_HOVER_COLOR

def draw_start_menu(screen):
    screen_width, screen_height = screen.get_size()
    scale = min(screen_width / DESIGN_WIDTH, screen_height / DESIGN_HEIGHT)

    draw_title(screen, scale, screen_width, screen_height)
    draw_buttons(screen, screen_width, screen_height, scale)
    

def draw_title(screen, scale, screen_width, screen_height):
    title_font: pygame.font.Font = pygame.font.SysFont(
        DEFAULT_TITLE_FONT_NAME,
        round(DEFAULT_TITLE_FONT_SIZE * scale),
    )
    title_text: str = GAME_TITLE
    title_surface: pygame.Surface = title_font.render(title_text, True, DEFAULT_TEXT_COLOR)
    title_rect: pygame.Rect = title_surface.get_rect(
        center=(screen_width // 2, screen_height // 2 - round(130 * scale))
    )
    screen.blit(title_surface, title_rect)

def draw_buttons(screen, screen_width, screen_height, scale):
    screen_width, screen_height = screen.get_size()
    button_font: pygame.font.Font = pygame.font.SysFont(
            DEFAULT_TITLE_FONT_NAME,
            round(DEFAULT_TITLE_FONT_SIZE * 0.5 * scale),
        )
    
    new_game_button = pygame.Rect(0, 0, round(200 * scale), round(50 * scale))
    quit_button = pygame.Rect(0, 0, round(200 * scale), round(50 * scale))
    load_game_button = pygame.Rect(0, 0, round(200 * scale), round(50 * scale))
    settings_button = pygame.Rect(0, 0, round(200 * scale), round(50 * scale))

    new_game_button.center = (screen_width // 2, screen_height // 2)
    load_game_button.center = (screen_width // 2, screen_height // 2 + round(85 * scale))
    quit_button.center = (screen_width // 2, screen_height // 2 + round(170 * scale))
    settings_button.center = (
        screen_width - round(115 * scale),
        screen_height - round(40 * scale),
    )

    mouse_position = pygame.mouse.get_pos()

    for button, label in (
        (new_game_button, "New Game"),
        (load_game_button, "Load Game"),
        (settings_button, "Settings"),
    ):
        color = DEFAULT_HOVER_COLOR if button.collidepoint(mouse_position) else DEFAULT_BUTTON_COLOR
        pygame.draw.rect(screen, color, button, border_radius=round(6 * scale))

        label_surface = button_font.render(label, True, (255, 255, 255))
        label_rect = label_surface.get_rect(center=button.center)
        screen.blit(label_surface, label_rect)