# Pygame Boilerplate

A small starting point for making a game with pygame-ce.

## Setup

1. Fork or download this project.
2. Install Python and pip:

   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

   This installs Python and its package installer.

3. Open a terminal in the project folder and upgrade pip:

   ```bash
   python3 -m pip install --user --upgrade pip
   ```

   This updates Python's package installer before you add pygame-ce.

4. Install pygame-ce:

   ```bash
   python3 -m pip install --user pygame-ce
   ```

   This installs the community-maintained library the game uses for its window, graphics, and input.

5. Run the game:

   ```bash
   python3 main.py
   ```

   This starts the game from its `main.py` entry point.

Start changing [main.py](main.py) to make the game yours. Shared settings such as the window size, title, and background color are in [constants.py](constants.py).

## Project Structure

- `main.py`: Game entry point and main loop.
- `constants.py`: Window size, title, and other shared settings.
- `setup.py`: Pygame display and window icon setup.
- `assets/`: Images, sounds, and other game resources.
- `tools/installer/`: Scripts used to create the Windows installer.
