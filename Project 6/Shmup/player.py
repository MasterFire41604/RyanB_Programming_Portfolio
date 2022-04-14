# Imports
import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    # Constructor
    def __init__(self, sprite, bullet_img, all_sprites, bullet_group, shoot_sound):
        super(Player, self).__init__()
        self.image = sprite
        self.image = pg.transform.scale(self.image, (50, 40))
        self.image.set_colorkey(BLACK)
        # Making a "hitbox" for our player
        self.rect = self.image.get_rect()
        self.radius = (self.rect.width * 1.2)/2
        # Centering in the middle of our screen
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 20
        # creating direction for movement
        self.speed = 10
        self.speed_x = 0
        self.shield = 100
        self.health = 5
        self.ammo = 200
        self.shootDelay = 250
        self.lastShot = pg.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = 0
        self.power_level = 0
        self.bullet_img = bullet_img
        self.all_sprites = all_sprites
        self.bullet_group = bullet_group
        self.shoot_sound = shoot_sound

    def update(self):
        if self.hidden and pg.time.get_ticks()-self.hide_timer > 1500:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 20
        self.speed_x = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.speed_x = -self.speed
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.speed_x = self.speed
        if keystate[pg.K_SPACE]:
            if self.ammo >= 1:
                self.shoot(self.all_sprites, self.bullet_group, self.bullet_img, self.shoot_sound)

        if self.rect.right < 0:
            self.rect.left = WIDTH
        if self.rect.left > WIDTH:
            self.rect.right = 0

        self.rect.centerx += self.speed_x

    def shoot(self, all_sprites, bullet_group, bullet_img, shoot_sound):
        now = pg.time.get_ticks()
        if (now - self.lastShot) > self.shootDelay:
            shoot_sound.play()
            self.lastShot = now
            if self.power_level == 0:
                self.ammo -= 1
                bullet = Bullet(self.rect.centerx, self.rect.top-1, bullet_img, all_sprites, bullet_group)
            elif self.power_level == 1:
                self.ammo -= 1
                bullet = Bullet(self.rect.centerx, self.rect.top - 1, bullet_img, all_sprites, bullet_group)
                self.shootDelay = 200
            elif self.power_level == 2:
                self.ammo -= 1
                bullet = Bullet(self.rect.right, self.rect.top - 1, bullet_img, all_sprites, bullet_group)
                bullet = Bullet(self.rect.left, self.rect.top - 1, bullet_img, all_sprites, bullet_group)
            elif self.power_level == 3:
                self.ammo -= 1
                bullet = Bullet(self.rect.right, self.rect.top - 1, bullet_img, all_sprites, bullet_group)
                bullet = Bullet(self.rect.left, self.rect.top - 1, bullet_img, all_sprites, bullet_group)
                bullet = Bullet(self.rect.centerx, self.rect.top - 1, bullet_img, all_sprites, bullet_group)
            elif self.power_level == 4:
                self.ammo -= 1
                bullet = Bullet(self.rect.right, self.rect.top - 1, bullet_img, all_sprites, bullet_group, 2)
                bullet = Bullet(self.rect.left, self.rect.top - 1, bullet_img, all_sprites, bullet_group, -2)
                bullet = Bullet(self.rect.centerx, self.rect.top - 1, bullet_img, all_sprites, bullet_group)
            elif (self.power_level >= 5) and (self.power_level < 10):
                self.ammo -= 1
                bullet = Bullet(self.rect.right, self.rect.top - 1, bullet_img, all_sprites, bullet_group, 2)
                bullet = Bullet(self.rect.left, self.rect.top - 1, bullet_img, all_sprites, bullet_group, -2)
                bullet = Bullet(self.rect.centerx, self.rect.top - 1, bullet_img, all_sprites, bullet_group)
                bullet = Bullet(self.rect.right, self.rect.top - 1, bullet_img, all_sprites, bullet_group, 4)
                bullet = Bullet(self.rect.left, self.rect.top - 1, bullet_img, all_sprites, bullet_group, -4)
            elif (self.power_level >= 10) and (self.power_level < 20):
                self.ammo -= 1
                bullet = Bullet(self.rect.right, self.rect.top - 1, bullet_img, all_sprites, bullet_group, 2)
                bullet = Bullet(self.rect.left, self.rect.top - 1, bullet_img, all_sprites, bullet_group, -2)
                bullet = Bullet(self.rect.centerx, self.rect.top - 1, bullet_img, all_sprites, bullet_group)
                bullet = Bullet(self.rect.right, self.rect.top - 1, bullet_img, all_sprites, bullet_group, 4)
                bullet = Bullet(self.rect.left, self.rect.top - 1, bullet_img, all_sprites, bullet_group, -4)
                bullet = Bullet(self.rect.right, self.rect.top - 1, bullet_img, all_sprites, bullet_group, 6)
                bullet = Bullet(self.rect.left, self.rect.top - 1, bullet_img, all_sprites, bullet_group, -6)
            elif self.power_level == 20:
                self.ammo -= 1
                bullet = Bullet(self.rect.right, self.rect.top - 1, bullet_img, all_sprites, bullet_group, 2)
                bullet = Bullet(self.rect.left, self.rect.top - 1, bullet_img, all_sprites, bullet_group, -2)
                bullet = Bullet(self.rect.centerx, self.rect.top - 1, bullet_img, all_sprites, bullet_group)
                bullet = Bullet(self.rect.right, self.rect.top - 1, bullet_img, all_sprites, bullet_group, 4)
                bullet = Bullet(self.rect.left, self.rect.top - 1, bullet_img, all_sprites, bullet_group, -4)
                bullet = Bullet(self.rect.right, self.rect.top - 1, bullet_img, all_sprites, bullet_group, 6)
                bullet = Bullet(self.rect.left, self.rect.top - 1, bullet_img, all_sprites, bullet_group, -6)
                bullet = Bullet(self.rect.right, self.rect.top - 1, bullet_img, all_sprites, bullet_group, 8)
                bullet = Bullet(self.rect.left, self.rect.top - 1, bullet_img, all_sprites, bullet_group, -8)

    def loseLife(self):
        self.lives -= 1
        self.hide()
        self.shield = 100
        self.health = 5
        self.ammo = 200

    def hide(self):
        self.hidden = True
        self.hide_timer = pg.time.get_ticks()
        self.rect.center = (WIDTH/2, HEIGHT+1000)

    def takeDamage(self, hit):
        self.shield -= hit.radius * 2
        if self.shield <= 0:
            self.loseHealth()
            if self.health >= 1:
                self.shield = 100

    def loseHealth(self):
        self.health -= 1

    def add_shield(self, num):
        self.shield += num
        if self.shield > 100:
            self.shield = 100

    def add_ammo(self, num):
        self.ammo += num
        if self.ammo > 200:
            self.ammo = 200

    def add_health(self, num):
        self.health += num
        if self.health > 5:
            self.health = 5

    def add_life(self, num):
        self.lives += num

    def gun_up(self):
        self.power_level += 1
        if self.power_level > 20:
            self.power_level = 20

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, sprite, all_sprites, bullet_group, speed_x=0):
        super(Bullet, self).__init__()
        self.image = sprite
        self.image = pg.transform.scale(self.image, (10, 20))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        # Centering in the middle of our screen
        self.rect.centerx = x
        self.rect.bottom = y
        # creating direction for movement
        self.speed = 20
        self.speed_y = -self.speed
        self.speed_x = speed_x
        all_sprites.add(self)
        bullet_group.add(self)

    def update(self):
        self.rect.centery += self.speed_y
        self.rect.centerx += self.speed_x
        if self.rect.bottom < -5:
            self.kill()