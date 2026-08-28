"""Build a self-contained Windows installer for the game."""

from pathlib import Path
import shutil
import subprocess
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ASSETS_DIR = PROJECT_ROOT / "assets"
ICON_ICO = ASSETS_DIR / "Boilerplate-Icon.ico"
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
DIST_DIR = ARTIFACTS_DIR / "dist"
INSTALLER_DIR = ARTIFACTS_DIR / "installer"


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=PROJECT_ROOT, check=True)


def find_iscc() -> str | None:
    iscc = shutil.which("iscc")
    if iscc is not None:
        return iscc

    per_user_install = Path.home() / "AppData" / "Local" / "Programs" / "Inno Setup 6" / "ISCC.exe"
    if per_user_install.is_file():
        return str(per_user_install)

    return None


def main() -> None:
    if not ICON_ICO.is_file():
        raise FileNotFoundError(f"Required icon was not found: {ICON_ICO}")

    run([sys.executable, "-m", "pip", "install", "pygame", "PyInstaller"])

    run([
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconfirm",
        "--clean",
        "--windowed",
        "--name",
        "Pygame Boilerplate",
        "--workpath",
        str(ARTIFACTS_DIR / "build"),
        "--distpath",
        str(DIST_DIR),
        "--specpath",
        str(ARTIFACTS_DIR / "spec"),
        "--icon",
        str(ICON_ICO),
        "--add-data",
        f"{ASSETS_DIR};assets",
        "main.py",
    ])

    iscc = find_iscc()
    if iscc is None:
        raise RuntimeError(
            "Inno Setup is required to create the installer. Install it with: "
            "winget install --id JRSoftware.InnoSetup -e"
        )

    run([iscc, "tools/installer/installer.iss"])
    installer = INSTALLER_DIR / "Pygame-Boilerplate-Setup.exe"
    print(f"Installer created: {installer}")


if __name__ == "__main__":
    main()