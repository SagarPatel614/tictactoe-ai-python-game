import sys
import pygame
from src.constants import *
from src.game import Game


# PYGAME Setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe AI')
screen.fill(BG_COLOR)


# Main Game Loop
def main():
    # Game object
    game = Game(screen)

    while True:
        for event in pygame.event.get():
            # Exit Game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


main()
