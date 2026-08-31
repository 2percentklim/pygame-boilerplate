
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
ASSETS_DIR = PROJECT_ROOT / "assets"

# Logical screen dimensions. Render scenes here, then scale by whole numbers only.
DESIGN_WIDTH = 640
DESIGN_HEIGHT = 360
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
GRID_SIZE = 32
GRID_COLOR = (105, 145, 105)
GRID_LABEL_COLOR = (185, 220, 185)

GAME_TITLE = 'Pygame Boilerplate'

DEFAULT_COLOR = (30, 30, 30)  # Dark color for screen fill
DEFAULT_TEXT_COLOR = (255, 255, 255)  # White color for text
DEFAULT_BUTTON_COLOR = (60, 85, 130)  # Blue color for buttons
DEFAULT_HOVER_COLOR = (85, 125, 190)  # Lighter blue for hover effect

DEFAULT_FPS = 60  # Frames per second

#FONTS
DEFAULT_TITLE_FONT_SIZE = 30
DEFAULT_TITLE_FONT_PATH = ASSETS_DIR / "fonts" / "Tengoku.ttf"

#BUTTONS
DEFAULT_BUTTON_FONT_SIZE = 15
DEFAULT_BUTTON_FONT_PATH = ASSETS_DIR / "fonts" / "Tengoku.ttf"