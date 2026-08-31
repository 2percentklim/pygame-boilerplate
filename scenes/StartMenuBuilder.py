import pygame

from constants import (
    DEFAULT_BUTTON_COLOR,
    DEFAULT_BUTTON_FONT_PATH,
    DEFAULT_BUTTON_FONT_SIZE,
    DEFAULT_HOVER_COLOR,
    DEFAULT_TEXT_COLOR,
    DEFAULT_TITLE_FONT_PATH,
    DEFAULT_TITLE_FONT_SIZE,
    GAME_TITLE,
)
from scenes.SceneBuilder import SceneBuilder


class StartMenuBuilder(SceneBuilder):
    def __init__(self, screen, show_grid=False):
        super().__init__(screen, show_grid)
        self.title_text = GAME_TITLE
        self.button_color = DEFAULT_BUTTON_COLOR
        self.button_color_hover = DEFAULT_HOVER_COLOR
        self.update_layout()

    def update_layout(self):
        self.title_font = pygame.font.Font(
            DEFAULT_TITLE_FONT_PATH,
            DEFAULT_TITLE_FONT_SIZE,
        )
        self.button_font = pygame.font.Font(
            DEFAULT_BUTTON_FONT_PATH,
            DEFAULT_BUTTON_FONT_SIZE,
        )

        button_size = (100, 25)
        self.new_game_button = pygame.Rect((0, 0), button_size)
        self.load_game_button = pygame.Rect((0, 0), button_size)
        self.settings_button = pygame.Rect((0, 0), button_size)

        self.new_game_button.center = (
            self.canvas_width // 2,
            self.canvas_height // 2,
        )
        self.load_game_button.center = (
            self.canvas_width // 2,
            212,
        )
        self.settings_button.center = (
            320,
            244,
        )

    def draw_content(self):
        self.draw_title()
        self.draw_buttons()

    def draw_title(self):
        title_surface = self.title_font.render(
            self.title_text,
            False,
            DEFAULT_TEXT_COLOR,
        )
        title_rect = title_surface.get_rect(
            center=(
                self.canvas_width // 2,
                116,
            )
        )
        self.canvas.blit(title_surface, title_rect)

    def draw_buttons(self):
        mouse_position = self.get_logical_mouse_position()

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
                self.canvas,
                color,
                button,
                border_radius=3,
            )

            label_surface = self.button_font.render(label, False, DEFAULT_TEXT_COLOR)
            label_rect = label_surface.get_rect(center=button.center)
            self.canvas.blit(label_surface, label_rect)