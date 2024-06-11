import copy
import random


class AI:
    def __init__(self, level=1, player=-1):
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
            evaluation = 'random'
            move = self.rnd(main_board)
        else:
            # minimax algo choice
            evaluation, move = self.minimax(main_board, False)  # Here the AI is the minimizing player
        print(f'AI has chosen to mark the square in pos {move} with evaluation of {evaluation}')
        return move

    def minimax(self, board, maximizing):
        # terminal case
        case = board.final_state()
        # player 1/2 wins
        if case != 0:
            return case, None
        # draw
        elif board.is_full():
            return 0, None

        # main algo
        if maximizing:
            max_eval = -100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, 1)
                value = self.minimax(temp_board, False)[0]
                if value > max_eval:
                    max_eval = value
                    best_move = (row, col)
            return max_eval, best_move
        else:
            min_eval = 100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, self.player)
                value = self.minimax(temp_board, True)[0]
                if value < min_eval:
                    min_eval = value
                    best_move = (row, col)
            return min_eval, best_move

