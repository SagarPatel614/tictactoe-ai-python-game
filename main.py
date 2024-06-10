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
    board = game.board

    # Main game loop
    while True:
        for event in pygame.event.get():
            # Exit Game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE
                if board.is_empty_sqr(row, col):
                    board.mark_square(row, col, game.player)
                    game.next_turn()

        pygame.display.update()


main()
