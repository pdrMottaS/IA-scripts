import numpy as np
from TicTacToe import TicTacToe

class MinimaxAgent:

    def minimax(self,state:TicTacToe):
        if state.winner == 1:
            return -1
        if state.winner == 2:
            return 1
        if len(state.available_moves()) == 0 and state.winner == None:
            return 0
        
        if state.player == 1:
            bestScore = -np.inf
            for move in state.available_moves():
                state.board[move[0]][move[1]] = state.player+1
                score = self.minimax(state)
                state.board[move[0]][move[1]] = 0
                bestScore = max(score,bestScore)
            return bestScore
        else:
            bestScore = -np.inf
            for move in state.available_moves():
                state.board[move[0]][move[1]] = state.player+1
                score = self.minimax(state)
                state.board[move[0]][move[1]] = 0
                bestScore = min(score,bestScore)
            return bestScore
        

    def find_best_move(self, state:TicTacToe):
        bestScore = -np.inf
        bestMove = None
        for move in state.available_moves():
            state.board[move[0]][move[1]] = state.player+1
            score = self.minimax(state)
            state.board[move[0]][move[1]] = 0
            if score > bestScore:
                bestScore = score
                bestMove = move
        return bestMove
