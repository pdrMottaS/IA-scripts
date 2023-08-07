from TicTacToe import TicTacToe
from MinimaxAgent import MinimaxAgent

game = TicTacToe()
agent = MinimaxAgent()

while True:
    if len(game.available_moves()) == 0:
        print("Draw!")
        break
    if game.winner != None:
        print(f'Player {game.players[game.player]} won!')
        break
    if game.player == 0:
        move = input("Enter move: ")
        move = move.split(',')
        move = (int(move[0]),int(move[1]))  
    else:
        move = agent.find_best_move(game)
    
    game.make_move(move)
    game.print_board()
    game.check_winner()