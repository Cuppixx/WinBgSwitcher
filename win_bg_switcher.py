# pylint: skip-file
# pylint: disable=C0103
"""My background switcher script for windows using python."""

from configparser import ConfigParser
from ctypes import windll
from keyboard import add_hotkey, unhook_all, wait # type: ignore
from os import getenv, listdir, path, remove
from random import choice
from shutil import copy
from sys import executable

config_object = ConfigParser()
with open("config.ini", "r") as file_object:
    config_object.read_file(file_object)

folder_1_path = config_object.get("Folders", "folder1")
folder_2_path = config_object.get("Folders", "folder2")
selected_path = config_object.get("Debug", "current_folder")


def clean_exit():
    """Unhook all hotkeys and exit the program cleanly."""
    unhook_all()
    exit()


def save_selected_path():
    """Save the current folder path to the config file."""
    config_object.set("Debug", "current_folder", selected_path)
    with open("config.ini", "w") as file_object:
        config_object.write(file_object)


def save_auto_start_state(state):
    """Save the current auto start state to the config file.
    Only for debug purposes."""
    config_object.set("Debug", "exe_auto_start", state)
    with open("config.ini", "w") as file_object:
        config_object.write(file_object)


def get_image_from_folder(folder_path):
    """Return a random image file path from the specified folder."""
    global selected_path
    selected_path = folder_path
    image_files = [f for f in listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not image_files:
        return None
    return path.join(folder_path, choice(image_files))


def set_wallpaper(image_path):
    """Sets the desktop background to the given image."""
    UINTuiAction_SPI_SETDESKWALLPAPER = 20
    UINTuiParam = 0
    PVOIDpvParam_IMAGE_PATH = image_path
    UINTfWinIni_SPIF_UPDATEINIFILE_SPIF_SENDCHANGE_COMBINED = 3

    windll.user32.SystemParametersInfoW(
        UINTuiAction_SPI_SETDESKWALLPAPER,
        UINTuiParam,
        PVOIDpvParam_IMAGE_PATH,
        UINTfWinIni_SPIF_UPDATEINIFILE_SPIF_SENDCHANGE_COMBINED
    )


def toggle_wallpaper():
    """Toggle between random images from two folders."""
    if selected_path == folder_1_path:
        new_image = get_image_from_folder(folder_2_path)
    else:
        new_image = get_image_from_folder(folder_1_path)

    if new_image:
        set_wallpaper(new_image)
        save_selected_path()


def toggle_auto_start():
    """Toggle the auto start."""
    try:
        startup_folder = path.join(getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        exe_path = executable
        startup_exe_path = path.join(startup_folder, path.basename(exe_path))

        if not path.exists(startup_exe_path):
            copy(exe_path, startup_exe_path)
            save_auto_start_state('True')
        else:
            remove(startup_exe_path)
            save_auto_start_state('False')
            
    except Exception as e:
         print(f'Exception thrown ...\n{e}')


try:
    add_hotkey(config_object.get("Keybinds", "switch"), toggle_wallpaper)
    add_hotkey(config_object.get("Keybinds", "auto_start"), toggle_auto_start)
    wait(config_object.get("Keybinds", "exit"))
except Exception as e:
    print(f'Exception thrown ...\n{e}')
    clean_exit()
finally:
    clean_exit()
