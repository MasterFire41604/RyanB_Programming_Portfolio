import pygame as pg
vec = pg.math.Vector2

# game options/settings
TITLE = "Game"
WIDTH = 1024  # 16*64 or 32*32 or 64*16
HEIGHT = 768  # 16*48 or 32*24 or 64*2
FPS = 60

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = "tileGreen_39.png"

# Player settings
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = "manBlue_gun.png"
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)

# Gun settings
BULLET_IMG = "bullet.png"
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150
KICKBACK = 200
GUN_SPREAD = 10

# Mob settings
MOB_IMG = "zombie1_hold.png"
MOB_SPEED = 150
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)
