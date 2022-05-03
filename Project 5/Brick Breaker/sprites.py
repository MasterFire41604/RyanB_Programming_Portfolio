import random

import pygame as pg
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT - 40)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.width = PLAYER_WIDTH

    def update(self):
        self.acc = vec(0, 0)
        keys = pg.key.get_pressed()
        if not self.pos.x <= 0 + PLAYER_WIDTH/2:
            if keys[pg.K_a] or keys[pg.K_LEFT]:
                self.acc.x = -PLAYER_ACC
        if not self.pos.x >= WIDTH - PLAYER_WIDTH/2:
            if keys[pg.K_d] or keys[pg.K_RIGHT]:
                self.acc.x = PLAYER_ACC

        # apply friction
        self.acc += self.vel * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.center = self.pos

    def shrink(self):
        if self.rect.width > 5:
            self.width -= 25
            self.image = pg.Surface((self.width, PLAYER_HEIGHT))
            self.image.fill(WHITE)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos

    def grow(self):
        self.width += 25
        self.image = pg.Surface((self.width, PLAYER_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos


class Ball(pg.sprite.Sprite):
    def __init__(self, dx, dy, game, x, y):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.size = 25
        self.image = pg.Surface((self.size, self.size))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos = vec(x, y)
        self.dx = dx
        self.dy = dy
        self.speed = BALL_SPEED

    def update(self):
        self.pos.x += self.dx * self.speed
        self.pos.y += self.dy * self.speed

        # If touching top or bottom sides
        if self.pos.x >= WIDTH or self.pos.x <= 0:
            self.dx = -self.dx
        if self.pos.y <= 0:
            self.dy = -self.dy

        # If touching bottom side
        if self.pos.y >= HEIGHT:
            self.kill()
            self.game.ball_spawned = False

        self.rect.center = self.pos


class Bricks(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((BRICK_WIDTH, BRICK_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Shrink(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((20, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos = vec(x, y)
        self.speedY = 1

    def update(self):
        self.pos.y += self.speedY * POWERUP_SPEED

        self.rect.center = self.pos


class Grow(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos = vec(x, y)
        self.speedY = 1

    def update(self):
        self.pos.y += self.speedY * POWERUP_SPEED

        self.rect.center = self.pos