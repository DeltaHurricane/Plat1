# Jogo em pygame teste inicial e possívelmente versão demo futura


import pygame
from settings import *
import random



def main():
    # inicializa pygame e cria a tela
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    # Game loop
    running = True
    while running:
        # manter na velocidade correta
        clock.tick(FPS)
        # process input(events)
        for event in pygame.event.get():
            # checa pra ver se a janela fechou
            if event.type == pygame.QUIT:
                running = False

        # update

        # draw / render
        screen.fill(BLACK)
        # depois de desenhar tudo da flip no display
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()

