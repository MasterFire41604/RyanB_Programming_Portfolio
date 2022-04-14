# Settings
import random
import os
import pygame as pg
import random

game_Folder = os.path.dirname(__file__)
assets_Folder = os.path.join(game_Folder, "assets")
img_Folder = os.path.join(assets_Folder, "imgs")
audio_Folder = os.path.join(assets_Folder, "audio")
music_folder = os.path.join(audio_Folder, "music")
ambient_folder = os.path.join(audio_Folder, "ambient")
fx_folder = os.path.join(audio_Folder, "fx")

# Game title
TITLE = "Template"

# Font
font_name = pg.font.match_font("Comic Sans MS")

# Screen size
WIDTH = 500
HEIGHT = 1000

# clock speed
FPS = 30

# Difficulty
diff = "Normal"

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
cfBLUE = (100, 149, 237)

pow_list = ["ammo", "ammo", "ammo", "bullets", "bullets", "shield", "shield", "shield", "health", "health", "lives"]
