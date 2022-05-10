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
        self.powerup_status = 0
        self.font_name = pg.font.match_font(FONT_NAME)
        self.player1_score = 0
        self.player2_score = 0

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.players = pg.sprite.Group()
        self.ball_sprite = pg.sprite.Group()
        self.powerups = pg.sprite.Group()

        self.backLine = BackgroundLine()
        self.player1 = Player()
        self.player2 = Player2()
        self.players.add(self.player1, self.player2)

        self.all_sprites.add(self.backLine, self.player1, self.player2)
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
        hit1 = pg.sprite.spritecollide(self.player2, self.ball_sprite, False)
        if hit1:
            self.ball.dx = -(abs(self.ball.dx))
            self.ball.dy += self.player2.vel.y
            self.ball.speed += 0.05
            if self.powerup_status == -1:
                self.player2.shrink()
                self.ball.grow()
            elif self.powerup_status == 1:
                self.player2.grow()
                self.ball.shrink()
        hit2 = pg.sprite.spritecollide(self.player1, self.ball_sprite, False)
        if hit2:
            self.ball.dx = abs(self.ball.dx)
            self.ball.dy += self.player1.vel.y
            self.ball.speed += 0.05
            if self.powerup_status == -1:
                self.player1.shrink()
                self.ball.grow()
            elif self.powerup_status == 1:
                self.player1.grow()
                self.ball.shrink()

        # If ball hits shrink or grow powerups
        hits = pg.sprite.groupcollide(self.powerups, self.ball_sprite, True, False)
        if hits:
            for hit in hits:
                if hit.rect.y < HEIGHT/2:
                    self.ball.shrink()
                    self.shrink_spawned = False
                if hit.rect.y > HEIGHT/2:
                    self.ball.grow()
                    self.grow_spawned = False
                hit.kill()

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
                        self.powerup_status = 0
                        self.ball = Ball(random.randrange(-5, 6, 10), random.randrange(-10, 11), self)
                        self.ball_sprite.add(self.ball)
                        if self.shrink_spawned == False:
                            self.shrink = Shrink()
                            self.shrink_spawned = True
                        if self.grow_spawned == False:
                            self.grow = Grow()
                            self.grow_spawned = True
                        self.powerups.add(self.shrink, self.grow)
                        self.all_sprites.add(self.ball, self.shrink, self.grow)

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.draw_text(str(self.player1_score), 50, WHITE, WIDTH/4, 50)
        self.draw_text(str(self.player2_score), 50, WHITE, WIDTH*(3/4), 50)
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