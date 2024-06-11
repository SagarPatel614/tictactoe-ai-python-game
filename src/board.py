import pygame
import numpy as np
from src.constants import *


class Board:
    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.empty_squares = self.squares
        self.marked_squares = 0

    def mark_square(self, row, col, player):
        self.squares[row][col] = player
        self.marked_squares += 1

    def is_empty_sqr(self, row, col):
        return self.squares[row][col] == 0

    def is_full(self):
        return self.marked_squares == 9

    def is_empty(self):
        return self.marked_squares == 0

    def get_empty_sqrs(self):
        empty_squares = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.is_empty_sqr(row, col):
                    empty_squares.append((row, col))
        return empty_squares

    def final_state(self):
        """

        :return:
            0 - if there is no win yet
            1 - if player 1 wins
            2 - if player 2 wins
        """
        # vertical wins
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                return self.squares[0][col]

        # horizontal wins
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                return self.squares[row][0]

        # diagonal wins
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            return self.squares[1][1]
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            return self.squares[1][1]

        # No wins yet
        return 0
