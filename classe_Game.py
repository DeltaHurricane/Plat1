#classe principal jogo que roda a janela controla update  etc

from settings import *
import pygame as pg
from sprites import *
import random

class Game:

    def __init__(self):
        #inicializa a tela do jogo
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()

        self.running = True


    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.plataforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add((self.player))
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
        if self.player.vel.y > 0:
            self.player.rect.y += 1
            hits = pg.sprite.spritecollide(self.player , self.plataforms, False)
            self.player.rect.y -= 1
            if hits and self.player.enable_colision:
                self.player.vel.y = 0
                self.player.pos.y = hits[0].rect.top

            if not hits:
                self.player.enable_colision = 1

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
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        # draw / render
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # depois de desenhar tudo da flip no display
        pg.display.flip()

    def show_start_screen(self):
        #mostra tela de inicio
        pass

    def show_go_screen(self):
        #game over screen
        pass