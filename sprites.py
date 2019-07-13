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
        self.direcion = 1
        self.atk_sprites = pg.sprite.Group()
        self.ranged_sprites = pg.sprite.Group()
        self.melee_sprites = pg.sprite.Group()

    def jump(self):
        #pula se estiver em plataforma ou no canto
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self,self.game.plataforms,False)
        self.rect.y -=1
        keys = pg.key.get_pressed()
        if not hits and keys [pg.K_DOWN]:
            self.vel.y = 15
        elif hits:
            if keys [pg.K_DOWN]:
                self.enable_colision = 0
            else:
                self.vel.y = -15


    def AtkRanged(self):
        self.atkranged = AtkRanged(self)
        self.atk_sprites.add((self.atkranged))
        self.ranged_sprites.add((self.atkranged))

    def AtkMelee(self):
        self.atkmelee = AtkMelee(self)
        self.atk_sprites.add((self.atkmelee))
        self.melee_sprites.add((self.atkmelee))

    def direcao(self):
        dir = vec(self.direcion,0)
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            dir.y = -1
        if keys[pg.K_DOWN]:
            dir.y = 1
        return dir

    def update(self):
        #acelera o player pra baixo e checa se ele ta indo pra esquerda ou direita
        self.acc = vec(0, 0.50)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
            self.direcion =-1
        elif keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
            self.direcion = 1

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

        self.atk_sprites.update()


class Plataform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#classe atkranged pra sprite de atk ranged
class AtkRanged (pg.sprite.Sprite):
    def __init__(self, player):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((5, 5))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.vel = player.direcao()
        self.rect.center = (player.rect.center[0]+ PLAYER_SIZE[0]/2*self.vel.x , player.rect.center[1] + PLAYER_SIZE[1]/2*self.vel.y)

    def update(self):
        self.rect.center += self.vel *5
        pos = vec(self.rect.center)
        if pos.x > WIDTH+200 or pos.x < -200 or pos.y > HEIGHT+200 or pos.y < -200:
            self.kill()


#classe atk pra sprite de atk melee
class AtkMelee (pg.sprite.Sprite):
    def __init__(self, player):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30,10))
        self.image.fill(RED)
        self.player = player
        self.rect = self.image.get_rect()
        self.vel = player.direcao()
        self.rect.center = (player.rect.center[0]+ PLAYER_SIZE[0]/2*self.vel.x,player.rect.center[1])
        self.cont = 0

    def update(self):
        self.cont +=1
        self.rect.center = (self.player.rect.center[0]+ PLAYER_SIZE[0]*self.vel.x,self.player.rect.center[1])
        if self.cont == 15:
            self.kill()
