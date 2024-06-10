import pygame
import numpy as np
from src.constants import *


class Board:
    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))

    def mark_square(self, row, col, player):
        self.squares[row][col] = player


