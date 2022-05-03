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
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(40, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.height = PLAYER_HEIGHT

    def update(self):
        self.acc = vec(0, 0)
        keys = pg.key.get_pressed()
        if not self.pos.y <= 0 + PLAYER_HEIGHT/2:
            if keys[pg.K_w]:
                self.acc.y = -PLAYER_ACC
        if not self.pos.y >= HEIGHT - PLAYER_HEIGHT/2:
            if keys[pg.K_s]:
                self.acc.y = PLAYER_ACC

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
        if self.rect.height > 5:
            self.height -= 25
            self.image = pg.Surface((PLAYER_WIDTH, self.height))
            self.image.fill(WHITE)
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH / 2, HEIGHT / 2)
            self.pos = vec(40, self.pos.y)

    def grow(self):
        self.height += 25
        self.image = pg.Surface((PLAYER_WIDTH, self.height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(40, self.pos.y)


class Player2(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH-40, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.height = PLAYER_HEIGHT

    def update(self):
        self.acc = vec(0, 0)
        keys = pg.key.get_pressed()
        if not self.pos.y <= 0 + PLAYER_HEIGHT/2:
            if keys[pg.K_UP]:
                self.acc.y = -PLAYER_ACC
        if not self.pos.y >= HEIGHT - PLAYER_HEIGHT/2:
            if keys[pg.K_DOWN]:
                self.acc.y = PLAYER_ACC

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
        if self.rect.height > 5:
            self.height -= 25
            self.image = pg.Surface((PLAYER_WIDTH, self.height))
            self.image.fill(WHITE)
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH / 2, HEIGHT / 2)
            self.pos = vec(WIDTH - 40, self.pos.y)

    def grow(self):
        self.height += 25
        self.image = pg.Surface((PLAYER_WIDTH, self.height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH - 40, self.pos.y)


class BackgroundLine(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((BACKLINE_WIDTH, HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)


class Ball(pg.sprite.Sprite):
    def __init__(self, dx, dy, game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.size = 25
        self.image = pg.Surface((self.size, self.size))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.dx = dx
        self.dy = dy
        self.speed = BALL_SPEED

    def update(self):
        if self.dy == 0:
            self.dy = random.randrange(-10, 11)
        self.pos.x += self.dx * self.speed
        self.pos.y += self.dy * self.speed

        # If touching top or bottom sides
        if self.pos.y >= HEIGHT or self.pos.y <= 0:
            self.dy = -self.dy

        # If touching left or right sides
        if self.pos.x >= WIDTH or self.pos.x <= 0:
            self.kill()
            self.game.ball_spawned = False
            if (self.pos.x >= WIDTH):
                self.game.player1_score += 1
                if self.game.powerup_status == -1:
                    self.game.player2_score -= 1
                elif self.game.powerup_status == 1:
                    self.game.player1_score += 1
            else:
                self.game.player2_score += 1
                if self.game.powerup_status == -1:
                    self.game.player1_score -= 1
                elif self.game.powerup_status == 1:
                    self.game.player2_score += 1

        self.rect.center = self.pos

    def shrink(self):
        if self.size == 25:
            self.size = 13.5
            self.image = pg.Surface((self.size, self.size))
            self.image.fill(RED)
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH / 2, HEIGHT / 2)
            self.game.powerup_status = -1
        else:
            self.size = 25
            self.image = pg.Surface((25, 25))
            self.image.fill(WHITE)
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH / 2, HEIGHT / 2)
            self.game.powerup_status = 0

    def grow(self):
        if self.size == 25:
            self.size = 50
            self.image = pg.Surface((self.size, self.size))
            self.image.fill(GREEN)
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH / 2, HEIGHT / 2)
            self.game.powerup_status = 1
        else:
            self.size = 25
            self.image = pg.Surface((25, 25))
            self.image.fill(WHITE)
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH / 2, HEIGHT / 2)
            self.game.powerup_status = 0


class Shrink(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 80))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/4)
        self.pos = vec(WIDTH/2, HEIGHT/2)


class Grow(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 80))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT*(3/4))
        self.pos = vec(WIDTH/2, HEIGHT/2)