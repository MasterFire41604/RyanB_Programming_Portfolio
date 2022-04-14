from settings import *
import pygame as pg

def draw_Text(surf, text, size, color, x, y):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, False, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_bar(surf, x, y, pct, pctMax, w, h, vert=False, color=GREEN):
    if pct < 0:
        pct = 0
    BAR_LENGTH = w
    BAR_HEIGHT = h

    if vert == False:
        fill = (pct / pctMax) * BAR_LENGTH
        outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    else:
        fill = (pct / pctMax) * BAR_HEIGHT
        outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        outline_rect.bottomleft = (x, y)
        fill_rect = pg.Rect(x, y, BAR_LENGTH, fill)
        fill_rect.bottomleft = (x, y)

    pg.draw.rect(surf, color, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect, 3)

def draw_life_img(surf, x, y, count, img):
    a = 0
    if count > 5:
        for i in range(count-5):
            a += 1
    for i in range(count-a):
        img_rect = img.get_rect()
        img_rect.x = x + (img.get_width()+5)*i
        img_rect.y = y
        surf.blit(img, img_rect)
