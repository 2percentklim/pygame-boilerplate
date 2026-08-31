
from abc import ABC, abstractmethod

import pygame

from constants import (
    DEFAULT_COLOR,
    DESIGN_HEIGHT,
    DESIGN_WIDTH,
    GRID_COLOR,
    GRID_LABEL_COLOR,
    GRID_SIZE,
)


class SceneBuilder(ABC):
    def __init__(self, screen, show_grid=False):
        self.screen = screen
        self.show_grid = show_grid
        self.canvas = pygame.Surface((DESIGN_WIDTH, DESIGN_HEIGHT))
        self.canvas_width, self.canvas_height = self.canvas.get_size()
        self.grid_font = pygame.font.Font(None, 10)
        self.update_screen_metrics()

    def update_screen_metrics(self):
        self.screen_width, self.screen_height = self.screen.get_size()
        self.display_scale = min(
            self.screen_width / DESIGN_WIDTH,
            self.screen_height / DESIGN_HEIGHT,
        )
        self.viewport_size = (
            round(DESIGN_WIDTH * self.display_scale),
            round(DESIGN_HEIGHT * self.display_scale),
        )
        self.viewport = pygame.Rect((0, 0), self.viewport_size)
        self.viewport.center = (self.screen_width // 2, self.screen_height // 2)

    @abstractmethod
    def update_layout(self):
        """Update scene-specific layout after a display resize."""

    def draw(self):
        if self.screen.get_size() != (self.screen_width, self.screen_height):
            self.update_screen_metrics()
            self.update_layout()

        self.canvas.fill(DEFAULT_COLOR)
        self.draw_content()
        if self.show_grid:
            self.draw_grid()
        self.screen.fill((0, 0, 0))
        scaled_canvas = pygame.transform.scale(self.canvas, self.viewport_size)
        self.screen.blit(scaled_canvas, self.viewport)

    def draw_grid(self):
        column_count = self.canvas_width // GRID_SIZE
        row_count = self.canvas_height // GRID_SIZE
        grid_width = column_count * GRID_SIZE
        grid_height = row_count * GRID_SIZE
        grid_left = (self.canvas_width - grid_width) // 2
        grid_top = (self.canvas_height - grid_height) // 2
        grid_right = min(grid_left + grid_width, self.canvas_width - 1)
        grid_bottom = min(grid_top + grid_height, self.canvas_height - 1)

        for column in range(column_count + 1):
            x_position = min(grid_left + column * GRID_SIZE, grid_right)
            pygame.draw.line(
                self.canvas,
                GRID_COLOR,
                (x_position, grid_top),
                (x_position, grid_bottom),
            )

        for row in range(row_count + 1):
            y_position = min(grid_top + row * GRID_SIZE, grid_bottom)
            pygame.draw.line(
                self.canvas,
                GRID_COLOR,
                (grid_left, y_position),
                (grid_right, y_position),
            )

        for column in range(column_count):
            label_surface = self.grid_font.render(
                chr(ord("A") + column),
                False,
                GRID_LABEL_COLOR,
            )
            label_rect = label_surface.get_rect(
                midtop=(
                    grid_left + column * GRID_SIZE + GRID_SIZE // 2,
                    grid_top + 2,
                )
            )
            self.canvas.blit(
                label_surface,
                label_rect,
            )

        for row in range(row_count):
            label_surface = self.grid_font.render(
                str(row + 1),
                False,
                GRID_LABEL_COLOR,
            )
            label_rect = label_surface.get_rect(
                midleft=(
                    grid_left + 2,
                    grid_top + row * GRID_SIZE + GRID_SIZE // 2,
                )
            )
            self.canvas.blit(
                label_surface,
                label_rect,
            )

    def get_logical_mouse_position(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return (
            int((mouse_x - self.viewport.left) / self.display_scale),
            int((mouse_y - self.viewport.top) / self.display_scale),
        )


    @abstractmethod
    def draw_content(self):
        """Draw scene-specific content to the display."""

