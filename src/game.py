import pygame
from src.constants import *
from src.board import Board


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.show_lines()
        self.board = Board()
        self.player = 1  # 1 - X, 2 - O

    def show_lines(self):
        # Vertical lines
        pygame.draw.line(self.screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)

        # Horizontal lines
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)

    def next_turn(self):
        self.player = self.player % 2 + 1

    def draw_fig(self, row, col):
        if self.player == 1:
            # draw X
            # descending line
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(self.screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)

            # ascending line
            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(self.screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
        elif self.player == 2:
            # draw O
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(self.screen, CIRCLE_COLOR, center, RADIUS, CIRCLE_WIDTH)

