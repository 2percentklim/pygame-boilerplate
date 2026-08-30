import pygame

from constants import (
    DEFAULT_BUTTON_COLOR,
    DEFAULT_BUTTON_FONT_NAME,
    DEFAULT_BUTTON_FONT_SIZE,
    DEFAULT_HOVER_COLOR,
    DEFAULT_TEXT_COLOR,
    DEFAULT_TITLE_FONT_NAME,
    DEFAULT_TITLE_FONT_SIZE,
    GAME_TITLE,
)
from scenes.SceneBuilder import SceneBuilder


class StartMenuBuilder(SceneBuilder):
    def __init__(self, screen):
        super().__init__(screen)
        self.title_text = GAME_TITLE
        self.button_color = DEFAULT_BUTTON_COLOR
        self.button_color_hover = DEFAULT_HOVER_COLOR
        self.update_layout()

    def update_layout(self):
        self.title_font = pygame.font.SysFont(
            DEFAULT_TITLE_FONT_NAME,
            round(DEFAULT_TITLE_FONT_SIZE * self.scale),
        )
        self.button_font = pygame.font.SysFont(
            DEFAULT_BUTTON_FONT_NAME,
            round(DEFAULT_BUTTON_FONT_SIZE * self.scale),
        )

        button_size = (round(200 * self.scale), round(50 * self.scale))
        self.new_game_button = pygame.Rect((0, 0), button_size)
        self.load_game_button = pygame.Rect((0, 0), button_size)
        self.settings_button = pygame.Rect((0, 0), button_size)

        self.new_game_button.center = (self.screen_width // 2, self.screen_height // 2)
        self.load_game_button.center = (
            self.screen_width // 2,
            self.screen_height // 2 + round(85 * self.scale),
        )
        self.settings_button.center = (
            self.screen_width - round(115 * self.scale),
            self.screen_height - round(40 * self.scale),
        )

    def draw_content(self):
        self.draw_title()
        self.draw_buttons()

    def draw_title(self):
        title_surface = self.title_font.render(
            self.title_text,
            True,
            DEFAULT_TEXT_COLOR,
        )
        title_rect = title_surface.get_rect(
            center=(
                self.screen_width // 2,
                self.screen_height // 2 - round(130 * self.scale),
            )
        )
        self.screen.blit(title_surface, title_rect)

    def draw_buttons(self):
        mouse_position = pygame.mouse.get_pos()

        for button, label in (
            (self.new_game_button, "New Game"),
            (self.load_game_button, "Load Game"),
            (self.settings_button, "Settings"),
        ):
            color = (
                self.button_color_hover
                if button.collidepoint(mouse_position)
                else self.button_color
            )
            pygame.draw.rect(
                self.screen,
                color,
                button,
                border_radius=round(6 * self.scale),
            )

            label_surface = self.button_font.render(label, True, DEFAULT_TEXT_COLOR)
            label_rect = label_surface.get_rect(center=button.center)
            self.screen.blit(label_surface, label_rect)