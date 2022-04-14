import pygame as pg

# game options/settings
TITLE = "Game"
WIDTH = 1024  # 16*64 or 32*32 or 64*16
HEIGHT = 768  # 16*48 or 32*24 or 64*2
FPS = 60

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_SPEED = 0.3
PLAYER_ROT_SPEED = 0.5
PLAYER_IMG = "manBlue_gun.png"
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)