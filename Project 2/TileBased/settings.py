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
PLAYER_HEALTH = 100
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = "manBlue_gun.png"
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)

# Weapon settings
BULLET_IMG = "bullet.png"
WEAPONS = {}
WEAPONS["pistol"] = {"bullet_speed": 500,
                        "bullet_lifetime": 1000,
                        "rate": 250,
                        "kickback": 200,
                        "spread": 5,
                        "damage": 10,
                        "bullet_size": "lg",
                        "bullet_count": 1}
WEAPONS["shotgun"] = {"bullet_speed": 400,
                         "bullet_lifetime": 500,
                         "rate": 900,
                         "kickback": 300,
                         "spread": 20,
                         "damage": 5,
                         "bullet_size": "sm",
                         "bullet_count": 12}

# Mob settings
MOB_IMG = "zombie1_hold.png"
MOB_SPEEDS = [150, 100, 75, 125]
MOB_HEALTH = 100
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50
DETECT_RADIUS = 400

# Effects
MUZZLE_FLASHES = ["whitePuff15.png", "whitePuff16.png", "whitePuff17.png", "whitePuff18.png"]
FLASH_DURATION = 40
SPLAT = "splat green.png"
DAMAGE_ALPHA = [i for i in range(0, 255, 25)]

# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
EFFECTS_LAYER = 4
ITEMS_LAYER = 1

# Items
ITEM_IMAGES = {"Health": "health_pack.png",
               "shotgun": "obj_shotgun.png"}
HEALTH_PACK_AMOUNT = 20
BOB_RANGE = 15
BOB_SPEED = 0.3

# Sounds
BG_MUSIC = "espionage.ogg"
PLAYER_HIT_SOUNDS = ["pain_8.wav", "pain_9.wav", "pain_10.wav", "pain_11.wav"]
ZOMBIE_MOAN_SOUNDS = ["brains2.wav", "brains3.wav", "zombie-roar-1.wav", "zombie-roar-2.wav", "zombie-roar-3.wav",
                      "zombie-roar-5.wav", "zombie-roar-6.wav", "zombie-roar-7.wav"]
ZOMBIE_HIT_SOUNDS = ["splat-15.wav"]
WEAPON_SOUNDS = {"pistol": ["pistol.wav"],
                 "shotgun": ["shotgun.wav"]}
EFFECTS_SOUNDS = {"level_start": "level_start.wav",
                  "health_up": "health_pack.wav",
                  "gun_pickup": "gun_pickup.wav"}

# Volume
ZOMBIE_MOAN_SOUNDS_VOL = 0.1
ZOMBIE_HIT_SOUNDS_VOL = 0.3
WEAPON_SOUNDS_VOL = 0.1
EFFECTS_SOUNDS_VOL = 0.3

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)
