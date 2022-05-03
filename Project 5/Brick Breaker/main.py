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
        self.bricks_left = 0

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.ball_sprite = pg.sprite.Group()
        self.bricks = pg.sprite.Group()
        self.shrinks = pg.sprite.Group()
        self.grows = pg.sprite.Group()

        self.player = Player()
        for place in BRICK_PLACEMENT:
            brick = Bricks(*place)
            self.bricks_left += 1
            self.bricks.add(brick)
            self.all_sprites.add(brick)
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
        been_hit = []
        if self.ball_spawned:
            hit = pg.sprite.spritecollide(self.ball, self.bricks, False)
            if hit:
                bottom = False
                top = False
                right = False
                left = False
                for hits in hit:
                    if self.ball.dy < 0 or bottom:
                        if hits.rect.y+BRICK_HEIGHT/2 < self.ball.rect.y:
                            if hits.rect.x-BRICK_WIDTH < self.ball.rect.x < hits.rect.x+BRICK_WIDTH:
                                self.ball.dy = abs(self.ball.dy)
                                hits.kill()
                                if not top and not right and not left:
                                    self.bricks_left -= 1
                                bottom = True
                                # Chance for powerup to fall
                                if random.randrange(100) < POWERUP_SPAWN_CHANCE:
                                    randomNum = random.randint(0, 2)
                                    if randomNum == 0:
                                        self.shrink = Shrink(hits.rect.x+BRICK_WIDTH/2, hits.rect.y+BRICK_HEIGHT/2)
                                        self.shrinks.add(self.shrink)
                                        self.all_sprites.add(self.shrink)
                                    if randomNum == 1:
                                        self.grow = Grow(hits.rect.x+BRICK_WIDTH/2, hits.rect.y+BRICK_HEIGHT/2)
                                        self.grows.add(self.grow)
                                        self.all_sprites.add(self.grow)
                    elif self.ball.dy > 0 or top:
                        if hits.rect.y-BRICK_HEIGHT/2 > self.ball.rect.y:
                            if hits.rect.x-BRICK_WIDTH < self.ball.rect.x < hits.rect.x+BRICK_WIDTH:
                                self.ball.dy = -(abs(self.ball.dy))
                                hits.kill()
                                self.bricks_left -= 1
                                if not bottom and not right and not left:
                                    top = True
                                # Chance for powerup to fall
                                if random.randrange(100) < POWERUP_SPAWN_CHANCE:
                                    randomNum = random.randint(0, 2)
                                    if randomNum == 0:
                                        self.shrink = Shrink(hits.rect.x+BRICK_WIDTH/2, hits.rect.y+BRICK_HEIGHT/2)
                                        self.shrinks.add(self.shrink)
                                        self.all_sprites.add(self.shrink)
                                    if randomNum == 1:
                                        self.grow = Grow(hits.rect.x+BRICK_WIDTH/2, hits.rect.y+BRICK_HEIGHT/2)
                                        self.grows.add(self.grow)
                                        self.all_sprites.add(self.grow)
                    if self.ball.dx > 0 or left:
                        if hits.rect.x-BRICK_WIDTH/2 > self.ball.rect.x:
                            if hits.rect.y-BRICK_HEIGHT < self.ball.rect.y < hits.rect.y+BRICK_HEIGHT:
                                self.ball.dx = -(abs(self.ball.dx))
                                hits.kill()
                                if not top and not right and not bottom:
                                    self.bricks_left -= 1
                                left = True
                                # Chance for powerup to fall
                                if random.randrange(100) < POWERUP_SPAWN_CHANCE:
                                    randomNum = random.randint(0, 2)
                                    if randomNum == 0:
                                        self.shrink = Shrink(hits.rect.x + BRICK_WIDTH / 2,
                                                             hits.rect.y + BRICK_HEIGHT / 2)
                                        self.shrinks.add(self.shrink)
                                        self.all_sprites.add(self.shrink)
                                    if randomNum == 1:
                                        self.grow = Grow(hits.rect.x + BRICK_WIDTH / 2, hits.rect.y + BRICK_HEIGHT / 2)
                                        self.grows.add(self.grow)
                                        self.all_sprites.add(self.grow)
                    elif self.ball.dx < 0 or right:
                        if hits.rect.x+BRICK_WIDTH/2 < self.ball.rect.x:
                            if hits.rect.y-BRICK_HEIGHT < self.ball.rect.y < hits.rect.y+BRICK_HEIGHT:
                                self.ball.dx = abs(self.ball.dx)
                                hits.kill()
                                if not top and not bottom and not left:
                                    self.bricks_left -= 1
                                right = True
                                # Chance for powerup to fall
                                if random.randrange(100) < POWERUP_SPAWN_CHANCE:
                                    randomNum = random.randint(0, 2)
                                    if randomNum == 0:
                                        self.shrink = Shrink(hits.rect.x + BRICK_WIDTH / 2,
                                                             hits.rect.y + BRICK_HEIGHT / 2)
                                        self.shrinks.add(self.shrink)
                                        self.all_sprites.add(self.shrink)
                                    if randomNum == 1:
                                        self.grow = Grow(hits.rect.x + BRICK_WIDTH / 2, hits.rect.y + BRICK_HEIGHT / 2)
                                        self.grows.add(self.grow)
                                        self.all_sprites.add(self.grow)

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
        self.draw_text(str(self.bricks_left), 50, WHITE, WIDTH/2, HEIGHT/2)
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