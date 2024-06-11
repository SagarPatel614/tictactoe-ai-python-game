import random


class AI:
    def __init__(self, level=0, player=2):
        self.level = level
        self.player = player

    @staticmethod
    def rnd(board):
        empty_sqrs = board.get_empty_sqrs()
        idx = random.randrange(0, len(empty_sqrs))
        return empty_sqrs[idx]

    def eval(self, main_board):
        if self.level == 0:
            # random choice
            move = self.rnd(main_board)
        else:
            # minimax algo choice
            pass
        return move
