# WinBgSwitcher

A Windows desktop background switcher built with Python.

For further instructions, look below.

## Overview

The WindowsBackgroundSwitcher is a small program I designed in a few hours time to run in the background of my PC. It allows for users to switch the desktop background image with the press of a keybind.
It uses two folders to swap between images and can run on startup for ease of use.

The WinBgSwitcher has various aspects of how and why you might want to use it.

- I originally designed it to easily swap out my personal desktop images for ones I don't mind showing when screen sharing, whether using Discord, Zoom, or any other tool during my studies.
- You can also use it as a manually triggered desktop slideshow to change your background every other day or so. Just press a keybind whenever you want to switch things up.
- Annoyed by having bright images as a desktop background at night? Simply switch between a folder of bright images and a folder of dark images whenever you want.
- You might find even more uses for it. Feel free!

The executable works with a config.ini file, which allows you to set the two folders and customize the hotkeys to your liking.
Just make sure they **don’t conflict with any other hotkeys** from other software you use.

## Installation and Setup

### Installation

1. Download the project (Code -> Download as zip).
2. Unzip the project in your Downloads folder.
3. Locate and open the `dist` folder (inside are the files you need).
4. You can now move the `win_bg_switcher.exe` and `config.ini` files to whatever folder you want.
5. _Before you continue, delete the leftover files from your Downloads folder!_
6. **Before you execute the programm** open the config.ini and change the folder paths under `Folders` and the keybinds under `Keybinds` to your needs.
7. Run the executable manually. If you want the programm to start automatically with your windows pc you can now press the `auto_start` keybind.

### How to use (after the executable is running)

- If you want to close the program, press the **exit** keybind.
- Pressing the **switch** hotkey will select a random image from the second or first folder you defined, depending on which folder you last selected from. For example, when you switch to a random image from folder 2, your next switch will return a random image from folder 1.
  - _If you only have one image in each folder, it will simply switch between those two images back and forth._
- If you want to **add the executable to the startup menu** (e.g., have it automatically run in the background whenever your PC starts), you can press the auto-start keybind. **If the executable is already added to the startup menu**, it will be removed instead.
  - You can get further information on whether the executable is already added to the startup menu by opening the config.ini file and looking at the debug option: exe_auto_start = [True | False]. Alternatively, you can check your Task Manager or see if a link is added under `C:\Users\Admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`.
- If you want to **change your config.ini settings**, you will need to exit and relaunch the program after making the changes for them to take effect.
- If you have **further questions** or problems running the program, open the discussion tab on GitHub and leave a comment.

### Compile the executable yourself

The entire project is licensed under the MIT License. If you want, you can go ahead and compile the executable yourself. Just download or clone the project, ensure you have Python and all the required packages installed on your PC, and then compile it. I used the command `pyinstaller --onefile --windowed --icon=icon.ico win_bg_switcher.py`.

## Bibliography

[My Portfolio](https://cuppixx.github.io)

[RidiculousCodingCuppixxVersion](https://github.com/Cuppixx/RidiculousCodingCuppixxVersion/tree/main)

[KoalaTime_Take_A_Break](https://github.com/Cuppixx/KoalaTime_Take-A-Break)

[PandaTime_Take_A_Break](https://github.com/Cuppixx/PandaTime_Take-A-Break)

[TravelingSalesmanProblem_ClassProject](https://github.com/Cuppixx/TravelingSalesmanProblem_ClassProject)

[WinBgSwitcher](https://github.com/Cuppixx/WinBgSwitcher)

More fun links to come ....

### Reference and Template Sources

| Authors    | Resources   |
| ---------- | ----------- |
| None       | None        |
