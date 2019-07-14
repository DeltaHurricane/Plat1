#classe principal jogo que roda a janela controla update  etc

from settings import *
import pygame as pg
from sprites import *
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
import random

class Game:

    def __init__(self):
        #inicializa a tela do jogo
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        player_img = pg.image.load(path.join(img_dir, "p1_front.png")).convert()
        atk_img = []
        for i  in range (8):
            atk_img.append( pg.image.load(path.join(img_dir, "icicle_{}.png".format(i))).convert())
        self.player_graf = {0:player_img, 1:atk_img}
        self.running = True


    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.plataforms = pg.sprite.Group()
        self.players = {}
        for i in range(PLAYER_QTD):
            player = (Player(self,PLAYER_KEYS[i],self.player_graf))
            self.players[i] = (player)
            self.all_sprites.add((player))
        for p1 in PLATAFORM_LIST:
            p = Plataform(*p1)
            self.all_sprites.add(p)
            self.plataforms.add(p)
        self.run()

    def run(self):
        #loop do jogo
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.eventes()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()
        #check if player hits plataform only if falling
        for player in self.players.values():
            if player.vel.y > 0:
                player.rect.y += 1
                hits = pg.sprite.spritecollide(player , self.plataforms, False)
                player.rect.y -= 1
                if hits and player.enable_colision:
                    player.vel.y = 0
                    player.pos.y = hits[0].rect.top

                if not hits:
                    player.enable_colision = 1

    def eventes(self):
        #game loop - events
        # process input(events)
        for event in pg.event.get():
            # checa pra ver se a janela fechou
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                for player in self.players.values():
                    if event.key in player.controls[4:]:
                        player.do(event.key)

    def draw(self):
        # draw / render
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        for player in self.players.values():
            player.atk_sprites.draw((self.screen))
        # depois de desenhar tudo da flip no display
        pg.display.flip()

    def show_start_screen(self):
        #mostra tela de inicio
        pass

    def show_go_screen(self):
        #game over screen
        pass