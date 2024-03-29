# deffinições pra tela
WIDTH = 480
HEIGHT = 600
FPS = 60


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