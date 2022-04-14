from settings import *
import pygame as pg

class Pow(pg.sprite.Sprite):
    def __init__(self, center, pow_img):
        super(Pow, self).__init__()
        self.pow_img = pow_img
        self.type = random.choice(pow_list)
        self.image = self.pow_img[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed_y = 6

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.y >= HEIGHT:
            self.kill()
