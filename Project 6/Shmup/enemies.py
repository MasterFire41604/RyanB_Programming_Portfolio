import pygame as pg
from settings import *


class Mob(pg.sprite.Sprite):
    def __init__(self, sprite):
        super(Mob, self).__init__()
        self.image_orig = sprite
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        # self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.radius = (self.rect.width * 0.85) / 2
        # Centering in the middle of our screen
        self.rect.centerx = random.randint(20, WIDTH-20)
        self.rect.bottom = random.randint(-100, -20)
        # creating direction for movement
        self.speed_x = random.randint(-3, 3)
        self.speed_y = random.randint(2 , 18)
        self.rot = 0
        self.rot_speed = random.randint(-8, 8)
        self.last_update = pg.time.get_ticks()

    def rotate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed)%360
            new_img = pg.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_img
            self.rect = self.image.get_rect()
            self.rect.center = old_center


    def update(self):
        self.rotate()
        self.rect.centerx += self.speed_x
        self.rect.centery += self.speed_y

        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = WIDTH

        if self.rect.top > HEIGHT + random.randint(3, 20):
            self.rect.centerx = random.randint(20, WIDTH - 20)
            self.rect.bottom = random.randint(-100, -20)
            # creating direction for movement
            self.speed_x = random.randint(-3, 3)
            self.speed_y = random.randint(4, 18)
