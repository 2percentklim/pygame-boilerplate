
from abc import ABC, abstractmethod

from constants import DESIGN_HEIGHT, DESIGN_WIDTH


class SceneBuilder(ABC):
    def __init__(self, screen):
        self.screen = screen
        self.update_screen_metrics()

    def update_screen_metrics(self):
        self.screen_width, self.screen_height = self.screen.get_size()
        self.scale = min(
            self.screen_width / DESIGN_WIDTH,
            self.screen_height / DESIGN_HEIGHT,
        )

    @abstractmethod
    def update_layout(self):
        """Update scene-specific layout after a display resize."""

    def draw(self):
        if self.screen.get_size() != (self.screen_width, self.screen_height):
            self.update_screen_metrics()
            self.update_layout()

        self.draw_content()

    @abstractmethod
    def draw_content(self):
        """Draw scene-specific content to the display."""

