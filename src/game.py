import pygame
from src.constants import *
from src.board import Board
from src.ai import AI


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.board = Board()
        self.player = 1  # 1 - X, -1 - O
        self.ai = AI()
        self.game_mode = 'ai'  # 'pvp' | 'ai
        self.running = True

        self.show_lines()

    def show_lines(self):
        # bg
        self.screen.fill(BG_COLOR)
        # Vertical lines
        pygame.draw.line(self.screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)

        # Horizontal lines
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)

    def next_turn(self):
        self.player = self.player * -1

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
        elif self.player == -1:
            # draw O
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(self.screen, CIRCLE_COLOR, center, RADIUS, CIRCLE_WIDTH)

    def play_move(self, row, col):
        self.board.mark_square(row, col, self.player)
        self.draw_fig(row, col)
        self.next_turn()

    def change_game_mode(self):
        self.game_mode = 'pvp' if self.game_mode == 'ai' else 'ai'

    def reset(self):
        self.__init__(self.screen)

    def is_over(self):
        return self.board.final_state() != 0 or self.board.is_full()

    def show_end(self):
        color = CIRCLE_COLOR if self.board.win_player == -1 else CROSS_COLOR
        if self.board.win_line == 'v':
            row, col = self.board.win_pos
            i_pos = (col * SQSIZE + SQSIZE // 2, 20)
            f_pos = (col * SQSIZE + SQSIZE // 2, HEIGHT - 20)
            pygame.draw.line(self.screen, color, i_pos, f_pos, LINE_WIDTH)
        elif self.board.win_line == 'h':
            row, col = self.board.win_pos
            i_pos = (20, row * SQSIZE + SQSIZE // 2)
            f_pos = (WIDTH - 20, row * SQSIZE + SQSIZE // 2)
            pygame.draw.line(self.screen, color, i_pos, f_pos, LINE_WIDTH)
        elif self.board.win_line == 'desc':
            i_pos = (20, 20)
            f_pos = (WIDTH - 20, HEIGHT - 20)
            pygame.draw.line(self.screen, color, i_pos, f_pos, LINE_WIDTH)
        elif self.board.win_line == 'asc':
            i_pos = (20, HEIGHT - 20)
            f_pos = (WIDTH - 20, 20)
            pygame.draw.line(self.screen, color, i_pos, f_pos, LINE_WIDTH)

