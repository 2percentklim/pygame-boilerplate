# Pygame Boilerplate

A small starting point for making a game with Pygame.

## Setup

1. Fork or download this project.
2. Install [Python](https://www.python.org/downloads/). On Windows, select **Add Python to PATH** during installation.
3. Open a terminal in the project folder and upgrade pip:

   ```powershell
   py -m pip install --upgrade pip
   ```

   This updates Python's package installer before you add pygame-ce.

4. Install pygame-ce:

   ```powershell
   py -m pip install pygame-ce
   ```

   This installs the community-maintained library the game uses for its window, graphics, and input.

5. Run the game:

   ```powershell
   py main.py
   ```

   This starts the game from its `main.py` entry point.

Start changing [main.py](main.py) to make the game yours. Shared settings such as the window size, title, and background color are in [constants.py](constants.py).

## Windows Installer

Build a self-contained installer with:

```powershell
py tools\installer\build_installer.py
```

The first build requires Inno Setup. Install it once with:

```powershell
winget install --id JRSoftware.InnoSetup -e
```

This installs the tool that turns your game into a Windows `Setup.exe`.

Build the installer after you are ready to share an update:

```powershell
py tools\installer\build_installer.py
```

This packages Python, Pygame, your game files, and the application icon. The finished installer is `artifacts\installer\Pygame-Boilerplate-Setup.exe`.

## Project Structure

- `main.py`: Game entry point, event loop, and start-menu rendering.
- `constants.py`: Shared display, layout, color, and font settings.
- `setup.py`: Pygame display and window-icon setup.
- `scenes/SceneBuilder.py`: Abstract base class for responsive scenes.
- `scenes/StartMenuBuilder.py`: Start menu with title and button rendering.
- `assets/`: Images, sounds, icons, and other game resources.
- `tools/installer/`: Scripts and Inno Setup configuration for the Windows installer.
- `artifacts/`: Generated executable build files and installer output.

For Ubuntu instructions, see [README_Ubuntu.md](README_Ubuntu.md).
