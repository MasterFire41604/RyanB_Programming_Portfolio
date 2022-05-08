import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, "img")
        self.map = Map(path.join(game_folder, 'map.txt'))
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG))
        x, y = self.player_img.get_size()
        self.player_img = pg.transform.scale(self.player_img, (x // PLAYER_SCALE, y // PLAYER_SCALE))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    wall = Wall(self, col, row)
                    self.walls.add(wall)
                if tile == 'P':
                    self.player = Player(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
        hits = pg.sprite.spritecollide(self.player, self.walls, False)
        if hits:
            if self.player.rect.bottom >= hits[0].rect.top and self.player.vel.y > 0: #and not\
                    # (self.player.rect.centerx > hits[0].rect.centerx+hits[0].rect.width*1.5
                    #  or self.player.rect.centerx < hits[0].rect.centerx-hits[0].rect.width*1.5):
                self.player.pos.y = hits[0].rect.top - self.player.rect.height/2
                self.player.vel.y = 0
                print("top")
            if self.player.rect.top <= hits[0].rect.bottom and self.player.vel.y < 0: #and not\
                    # (self.player.rect.centerx > hits[0].rect.centerx+hits[0].rect.width*1.5
                    #  or self.player.rect.centerx < hits[0].rect.centerx-hits[0].rect.width*1.5):
                self.player.pos.y = hits[0].rect.bottom + self.player.rect.height/2
                self.player.vel.y = 0
                print("bottom")
            if self.player.rect.right <= hits[0].rect.centerx and self.player.vel.x > 0: #and not\
                    # (self.player.rect.centery > hits[0].rect.centery+hits[0].rect.height
                    #  or self.player.rect.centery < hits[0].rect.centery-hits[0].rect.height):
                self.player.pos.x = hits[0].rect.left - self.player.rect.width/2
                print("left")
                self.player.vel.x = 0
            if self.player.rect.left >= hits[0].rect.centerx and self.player.vel.x < 0: #and not\
                    # (self.player.rect.centery > hits[0].rect.centery+hits[0].rect.height
                    #  or self.player.rect.centery < hits[0].rect.centery-hits[0].rect.height):
                self.player.pos.x = hits[0].rect.right + self.player.rect.width/2
                self.player.vel.x = 0
                print("right")

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_UP:
                    self.player.jump()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()