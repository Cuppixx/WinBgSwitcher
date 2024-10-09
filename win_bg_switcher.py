"""My background switcher script for windows using python."""

import ctypes
import keyboard

IMAGE_1_PATH = r'path/to/my/image.jpg' # Set your actual image path
IMAGE_2_PATH = r'path/to/my/image.png' # Set your actual image path

current_image = None


def set_wallpaper(image_path):
    """Sets the desktop background to the given image."""
    global current_image
    current_image = image_path

    UINTuiAction_SPI_SETDESKWALLPAPER = 20
    UINTuiParam = 0
    PVOIDpvParam_IMAGE_PATH = image_path
    UINTfWinIni_SPIF_UPDATEINIFILE_SPIF_SENDCHANGE_COMBINED = 3

    ctypes.windll.user32.SystemParametersInfoW(
        UINTuiAction_SPI_SETDESKWALLPAPER,
        UINTuiParam,
        PVOIDpvParam_IMAGE_PATH,
        UINTfWinIni_SPIF_UPDATEINIFILE_SPIF_SENDCHANGE_COMBINED
    )
    print(f"Background switched to: {image_path}")


def toggle_wallpaper():
    """Toggle between the images."""
    if current_image == IMAGE_1_PATH:
        set_wallpaper(IMAGE_2_PATH)
    else:
        set_wallpaper(IMAGE_1_PATH)


keyboard.add_hotkey('ctrl+alt+b', toggle_wallpaper)
keyboard.wait('ctrl+alt+c')
