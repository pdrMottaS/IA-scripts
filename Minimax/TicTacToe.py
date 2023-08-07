import numpy as np

class TicTacToe():
    def __init__(self):
        self.board = np.zeros((3,3))
        self.players = ['X','O']
        self.player = 0
        self.winner = None
        self.game_over = None

    def reset(self): 
        self.board = np.zeros((3,3))
        self.player = 0
        self.winner = None
        self.game_over = None
    
    def available_moves(self):
        moves = []
        for c in range(3):
            for l in range(3):
                if self.board[c][l] == 0:
                    moves.append((c,l))
        return moves
    
    def make_move(self,move):
        if self.board[move[0]][move[1]] != 0:
            return False
        self.board[move[0]][move[1]] = self.player+1
        self.change_player()
        return True
    
    def undo_move(self,move):
        self.board[move[0]][move[1]] = 0
        self.change_player()
    
    def change_player(self):
        if self.player == 0:
            self.player = 1
        else:
            self.player = 0
    
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                self.winner = self.player+1
                self.game_over = True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                self.winner = self.player+1
                self.game_over = True
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != 0) or (self.board[0][2] == self.board[1][1] == self.board[2][0] != 0):
            self.winner = self.player+1
            self.game_over = True
    
    def print_board(self):
        print("-------------")
        for i in range(3):
            print("|", end=' ')
            for j in range(3):
                print(self.players[int(self.board[i][j] - 1)] if self.board[i][j] != 0 else " ", end=' | ')
            print()
            print("------------")