import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.ball_spawned = False
        self.shrink_spawned = False
        self.grow_spawned = False
        self.font_name = pg.font.match_font(FONT_NAME)
        self.player1_score = 0
        self.player2_score = 0

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.ball_sprite = pg.sprite.Group()
        self.bricks = pg.sprite.Group()
        self.shrinks = pg.sprite.Group()
        self.grows = pg.sprite.Group()

        self.player = Player()
        bricks = []
        for i in range(3):
            self.brick = Bricks(BRICK_WIDTH*i, BRICK_HEIGHT)
            self.bricks.add(self.brick)
            self.all_sprites.add(self.brick)
            bricks.append(self.brick)
        self.all_sprites.add(self.player)
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

        # If ball hits paddles
        hit = pg.sprite.spritecollide(self.player, self.ball_sprite, False)
        if hit:
            self.ball.dy = -(abs(self.ball.dy))
            self.ball.speed += 0.05

        # If ball hits bricks
        hit = pg.sprite.groupcollide(self.ball_sprite, self.bricks, False, True)
        if hit:
            for hits in hit:
                if self.ball.dy < 0:
                    if hits.rect.bottom > self.ball.rect.top:
                        if hits.rect.left-0.01 < self.ball.rect.left and hits.rect.right+0.01 > self.ball.rect.right:
                            self.ball.dy = abs(self.ball.dy)
                else:
                    if hits.rect.top < self.ball.rect.bottom:
                        if hits.rect.left-0.01 < self.ball.rect.left and hits.rect.right+0.01 > self.ball.rect.right:
                            self.ball.dy = -(abs(self.ball.dy))

        # If player hits shrink powerdown
        hit = pg.sprite.spritecollide(self.player, self.shrinks, True)
        if hit:
            self.player.shrink()

        # If player hits shrink powerdown
        hits = pg.sprite.spritecollide(self.player, self.grows, True)
        if hits:
            self.player.grow()

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if self.ball_spawned == False:
                        self.ball_spawned = True
                        self.ball = Ball(random.randrange(-5, 6, 3), -5, self, self.player.pos.x, self.player.pos.y-20)
                        self.ball_sprite.add(self.ball)
                        self.all_sprites.add(self.ball)

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)

        # After drawing everything, flip the display
        pg.display.flip()

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

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
    g.show_go_screen()

pg.quit()