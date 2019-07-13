# sprite classes for the game
from settings import *
import pygame as pg

vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self , game):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface(PLAYER_SIZE)
        self.game = game
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = (WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.enable_colision = 1

    def jump(self):
        #pula se estiver em plataforma ou no canto
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self,self.game.plataforms,False)
        self.rect.y -=1
        keys = pg.key.get_pressed()
        if not hits and keys [pg.K_DOWN]:
            self.vel.y = 20
        elif hits:
            if keys [pg.K_DOWN]:
                self.enable_colision = 0
            else:
                self.vel.y = -15

    def update(self):
        #acelera o player pra baixo e checa se ele ta indo pra esquerda ou direita
        self.acc = vec(0, 0.50)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
                self.acc.x = -PLAYER_ACC
        elif keys[pg.K_RIGHT]:
                self.acc.x = PLAYER_ACC

        #apply friction
        self.acc.x += self.vel.x *  PLAYER_FRICTION

        #equation of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

        #stop arround the corners of the screen
        if self.pos.x >= WIDTH - PLAYER_SIZE[0]/2:
            self.pos.x = WIDTH - PLAYER_SIZE[0]/2
            self.vel.x = 0
        if self.pos.x < 0 + PLAYER_SIZE[0]/2:
            self.pos.x = 0 + PLAYER_SIZE[0]/2
            self.vel.x = 0

class Plataform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Atk (pg.sprite.Sprite):
    def __init__(self, x, y, vec):
        pg.sprite.Sprite.__init__(self)
        self.self.image = pg.Surface(PLAYER_SIZE)


