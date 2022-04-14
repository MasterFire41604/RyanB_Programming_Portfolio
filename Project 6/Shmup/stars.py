import pygame as pg
import random
from settings import *

class Stars(pg.sprite.Sprite):
    def __init__(self):
        super(Stars, self).__init__()
        self.image = pg.Surface((2, 2))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        # Centering in the middle of our screen
        self.rect.centerx = random.randint(20, WIDTH - 20)
        self.rect.bottom = random.randint(-HEIGHT, HEIGHT)
        # creating direction for movement
        self.speed_x = 0
        self.speed_y = 15

    def update(self):
        self.rect.centerx += self.speed_x
        self.rect.centery += self.speed_y

        # if self.rect.left > WIDTH:
        #     self.rect.right = 0
        # if self.rect.right < 0:
        #     self.rect.left = WIDTH

        if self.rect.top > HEIGHT + random.randint(3, 20):
            self.rect.centerx = random.randint(20, WIDTH - 20)
            self.rect.bottom = random.randint(-100, -20)