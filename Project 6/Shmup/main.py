# Thanks for the artwork Kenny!

# Main Game File

# Installations_______________________
# install pygame with 'pip install pygame'

# Imports
from settings import *
import pygame as pg
from player import *
from enemies import *
from stars import *
from animations import *
from hud_functions import *
from powerups import *


# Setup pygame
pg.init()
pg.mixer.init()
running = True

def show_gameOver_screen(screen, background, background_rect, clock):
    global running
    screen.blit(background, background_rect)
    draw_Text(screen, TITLE, 64, RED, WIDTH/2, HEIGHT/4)
    draw_Text(screen, "Arrows move, Space to shoot", 30, WHITE, WIDTH / 2, HEIGHT/2)
    draw_Text(screen, "Press any key to start", 30, RED, WIDTH/2, HEIGHT*(3/4))
    pg.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
            if event.type == pg.KEYUP:
                waiting = False

# Setup main function
def main():
    global running
    game_over = True
    score = 0
    ammoPiercing = 0

    # Create game objects
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption(TITLE)
    clock = pg.time.Clock()

    # Load assets
    background = pg.image.load(os.path.join(img_Folder, "starfield.png")).convert()
    background = pg.transform.scale(background, (WIDTH, HEIGHT))
    bg_rect = background.get_rect()

    player_img = pg.image.load(os.path.join(img_Folder, "playerShip.png")).convert()
    player_mini_img = pg.transform.scale(player_img, (40, 30))
    player_mini_img.set_colorkey(BLACK)

    bullet_img = pg.image.load(os.path.join(img_Folder, "laserRed.png")).convert()

    health_img = pg.image.load(os.path.join(img_Folder, "health.png")).convert()
    health_img.set_colorkey(WHITE)
    health = pg.transform.scale(health_img, (25, 25))

    meteor_img_list = []
    meteor_list = ["meteorBrown_big1.png", "meteorBrown_med1.png", "meteorBrown_small1.png", "meteorBrown_tiny1.png",
                   "meteorBrown_big2.png", "meteorBrown_med3.png", "meteorBrown_small2.png", "meteorBrown_tiny2.png",
                   "meteorBrown_big3.png", "meteorBrown_big4.png", "meteorGrey_big1.png", "meteorGrey_big2.png",
                   "meteorGrey_big3.png", "meteorGrey_big4.png", "meteorGrey_med1.png", "meteorGrey_med2.png",
                   "meteorGrey_small1.png", "meteorGrey_small2.png", "meteorGrey_tiny1.png", "meteorGrey_tiny2.png"]
    for img in meteor_list:
        meteor_img_list.append(pg.image.load(os.path.join(img_Folder, img)).convert())

    explosion_anim = {}
    explosion_anim["lg"] = []
    explosion_anim["sm"] = []
    explosion_anim["playerExpl"] = []
    for i in range(9):
        filename = "regularExplosion0{}.png".format(i)
        img = pg.image.load(os.path.join(img_Folder, filename)).convert()
        img.set_colorkey(BLACK)
        lg_img = pg.transform.scale(img, (75, 75))
        explosion_anim["lg"].append(lg_img)
        sm_img = pg.transform.scale(img, (25, 25))
        explosion_anim["sm"].append(sm_img)
        filename = "sonicExplosion0{}.png".format(i)
        image = pg.image.load(os.path.join(img_Folder, filename)).convert()
        image.set_colorkey(BLACK)
        explosion_anim["playerExpl"].append(image)

    pow_img = {}
    pow_img[pow_list[0]] = pg.transform.scale(bullet_img, (7, 14))
    pow_img[pow_list[3]] = pg.image.load(os.path.join(img_Folder, "bolt_gold.png")).convert()
    pow_img[pow_list[5]] = pg.image.load(os.path.join(img_Folder, "shield_gold.png")).convert()
    pow_img[pow_list[8]] = health
    pow_img[pow_list[10]] = pg.transform.scale(player_img, (20, 20))

    #Load sounds
    shoot_sound = pg.mixer.Sound(os.path.join(fx_folder, "Shoot1.wav"))
    pickup_sound = pg.mixer.Sound(os.path.join(fx_folder, "pickup.wav"))
    explosion_sounds = ["Explosion1.wav", "Explosion2.wav", "Explosion3.wav"]
    explosion_sound = []
    for sound in explosion_sounds:
        explosion_sound.append(pg.mixer.Sound(os.path.join(fx_folder, sound)))

    music = pg.mixer.music.load(os.path.join(music_folder, "MattOglseby - 8.ogg"))
    pg.mixer.music.set_volume(0.5)

    # Start game loop
    pg.mixer.music.play(loops=-1)
    while running:
        if game_over:
            show_gameOver_screen(screen, background, bg_rect, clock)
            game_over = False
            all_sprites = pg.sprite.Group()
            enemy_group = pg.sprite.Group()
            bullet_group = pg.sprite.Group()
            powerup_group = pg.sprite.Group()
            player = Player(player_img, bullet_img, all_sprites, bullet_group, shoot_sound)
            all_sprites.add(player)
            for i in range(100):
                stars = Stars()
                all_sprites.add(stars)
            for i in range(20):
                enemy = Mob(random.choice(meteor_img_list))
                all_sprites.add(enemy)
                enemy_group.add(enemy)

        # Update Clock
        clock.tick(FPS)
        # Process events
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
            if event.type == pg.QUIT:
                running = False

        # Collision between player sprite and enemy group
        hits = pg.sprite.spritecollide(player, enemy_group, True, pg.sprite.collide_circle)
        if hits:
            for hit in hits:
                random.choice(explosion_sound).play()
                player.takeDamage(hit)
                size = ""
                if hit.radius < 30:
                    size = "sm"
                else:
                    size = "lg"
                expl = Explosion(hit.rect.center, size, explosion_anim)
                all_sprites.add(expl)
                enemy = Mob(random.choice(meteor_img_list))
                all_sprites.add(enemy)
                enemy_group.add(enemy)
            if player.health <= 0:
                expl = Explosion(player.rect.center, "playerExpl", explosion_anim)
                all_sprites.add(expl)
                player.loseLife()


        if player.lives <= 0 and not expl.alive():
            game_over = True

            # Take damage
            # Play sound
            # Play animation
        # Collision between bullet_group and enemy_group
        hits = pg.sprite.groupcollide(enemy_group, bullet_group, True, True)

        for hit in hits:
            random.choice(explosion_sound).play()
            score += 100 - int(hit.radius)
            enemy = Mob(random.choice(meteor_img_list))
            size = ""
            if hit.radius < 30:
                size = "sm"
            else:
                size = "lg"
            expl = Explosion(hit.rect.center, size, explosion_anim)
            all_sprites.add(expl)
            all_sprites.add(enemy)
            enemy_group.add(enemy)
            if random.random() > 0.95:
                powerup = Pow(hit.rect.center, pow_img)
                powerup_group.add(powerup)
                all_sprites.add(powerup)

        # if player hits powerup
        hits = pg.sprite.spritecollide(player, powerup_group, True)
        if hits:
            for hit in hits:
                pickup_sound.play()
                if hit.type == pow_list[0]:
                    player.add_ammo(random.randint(25, 100))
                if hit.type == pow_list[3]:
                    player.gun_up()
                if hit.type == pow_list[5]:
                    player.add_shield(random.randint(25, 75))
                if hit.type == pow_list[8]:
                    player.add_health(1)
                if hit.type == pow_list[10]:
                    player.add_life(1)

        # Update_______________________
        all_sprites.update()

        # Draw_________________________
        # Things that are drawn first are the farthest back

        # Background color
        # screen.fill(cfBLUE)
        screen.blit(background, bg_rect)

        # Draw all sprites
        all_sprites.draw(screen)
        draw_Text(screen, str(score), 25, WHITE, WIDTH/2, 25)
        draw_bar(screen, 5, 20, player.shield, 100, 200, 25)
        draw_Text(screen, "Shield", 20, BLUE, 100, 17)
        draw_bar(screen, 5, 60, player.health, 5, 200, 25)
        draw_Text(screen, "Health", 20, RED, 100, 57)
        draw_bar(screen, 5, HEIGHT - 150, player.ammo, 200, 25, 200, True, RED)
        draw_Text(screen, "Bullets", 20, RED, 30, 620)
        draw_life_img(screen, WIDTH-230, 40, player.lives, player_mini_img)

        # Must be the last thing called in the draw section
        pg.display.flip()


main()