import pygame as pg

# deffinições pra tela
WIDTH = 480
HEIGHT = 600
FPS = 60

#num de jogadores

PLAYER_QTD = 2
PLAYER_KEYS = {0:[pg.K_DOWN,pg.K_UP,pg.K_LEFT,pg.K_RIGHT,pg.K_SPACE,pg.K_n,pg.K_m]
               ,1:[pg.K_s,pg.K_w,pg.K_a,pg.K_d,pg.K_f,pg.K_g,pg.K_h]}


#player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_SIZE = (30, 40)


#starting plataforms
PLATAFORM_LIST = [(0,HEIGHT-40, WIDTH, 40),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                  (125,HEIGHT - 350, 100, 20),
                  (350, 200, 100, 20),
                  (175, 100, 50, 20)]

# define cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


TITLE = "RPG FIGHT"