import pygame as pg
import random
from settings import *
from sprites import *
from os import path

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.start = False
        self.load_data()

    def load_data(self):
        # Load high score
        self.dir = path.dirname(__file__)
        try:
            with open(path.join(self.dir, HS_FILE), "r") as f:
                self.highscore = int(f.read())
        except:
            with open(path.join(self.dir, HS_FILE), "w") as f:
                self.highscore = 0
                f.write("0")

    def new(self):
        # start a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.no_touch = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.ground = Platform(0, HEIGHT-30, WIDTH, 30)
        for pipe in START_PIPES:
            self.pipe = Pipe(*pipe)
            self.all_sprites.add(self.pipe)
            self.no_touch.add(self.pipe)
        self.all_sprites.add(self.ground)
        self.no_touch.add(self.ground)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # check if player hits a platform
        hits = pg.sprite.spritecollide(self.player, self.no_touch, False)
        if hits:
            # Die
            if hits[0] == self.ground:
                self.player.rect.bottom = self.ground.rect.top
            self.playing = False

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE or event.key == pg.K_UP:
                    self.player.jump()

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        if self.start == False:
            self.show_start_screen()
        if self.running == False:
            return
        self.draw_text(str(self.score), 100, WHITE, WIDTH/2, HEIGHT/2)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        self.start = True
        self.draw_text(TITLE, 80, WHITE, WIDTH/2, HEIGHT/4)
        self.draw_text("Highscore: " + str(self.highscore), 22, WHITE, WIDTH/2, HEIGHT/2)
        self.draw_text("Press Space or Up to play", 25, WHITE, WIDTH/2, HEIGHT*(3/4))
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        # game over/continue
        if not self.running:
            return
        self.draw_text("Game Over", 80, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score: ", 40, WHITE, WIDTH * (3/8), HEIGHT / 2)
        self.draw_text("Press Space or Up to play again", 25, WHITE, WIDTH / 2, HEIGHT * (3 / 4))
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("New Highscore!", 30, WHITE, WIDTH/2, HEIGHT/2 + 80)
            with open(path.join(self.dir, HS_FILE), "w") as f:
                f.write(str(self.score))
        else:
            self.draw_text("Highscore: " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT / 2 + 85)

        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS/2)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYDOWN:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

g = Game()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()