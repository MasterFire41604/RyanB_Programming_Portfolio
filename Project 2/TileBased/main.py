import pygame as pg
import random
from settings import *
from sprites import *
from tileMap import *
import sys
from os import path

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.running = True
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, "img")
        self.map = Map(path.join(game_folder, "map2.txt"))
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert()
        self.bullet_img = pg.image.load(path.join(img_folder, BULLET_IMG)).convert()
        self.bullet_img = pg.transform.scale(self.bullet_img, (10, 10))
        self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert()
        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert()
        self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE, TILESIZE))

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == "1":
                    Wall(self, col, row)
                if tile == "M":
                    Mob(self, col, row)
                if tile == "P":
                    self.player = Player(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000.0
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        self.camera.update(self.player)
        # Bullets hit mobs
        hits = pg.sprite.groupcollide(self.mobs, self.bullets, False, True)
        for hit in hits:
            hit.kill()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, WHITE, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, WHITE, (0, y), (WIDTH, y))

    def draw(self):
        pg.display.set_caption("{:.2f}".format((self.clock.get_fps())))
        # Game Loop - draw
        self.screen.fill(BROWN)
        # self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        # pg .draw.rect(self.screen, WHITE, self.player.hit_rect, 2)
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.run()
    g.show_go_screen()

pg.quit()