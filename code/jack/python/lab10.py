# Lab 10: tic tac toe

tiles = 3

class Game():
    def __init__(self):
        self.board = [[' ' for _ in range(tiles)] for _ in range(tiles)]
    

    def __repr__(self):
        board_string = ''
        
        for y in self.board:
            
            for x in range(len(y)):
                board_string += str(y[x])
                if not x + 1 == len(y): # adds | if not last x
                    board_string += '|'

            if not y is self.board[tiles - 1]: # adds new line if not last y
                board_string += '\n'

        return board_string
    

    def setup(self):
        print('Game started')
        print(self.__repr__())


    def move(self, x, y, player):
        self.board[y][x] = player.token
        print(self.__repr__())
        


# allows for duplicate names, tokens - TBD if fix
class Player():
    def __init__(self, number, token):
        self.name = input(f'Enter player {number} name: ').capitalize()
        self.token = token



def main():
    print('\n\n')

    # game setup
    p1 = Player(1, 'X')
    p2 = Player(2, 'O')
    game = Game()
    game.setup()
    player_1_move = True # used to toggle between player 1 move (True) and player 2 move (False)
    
    # game REPL
    while True:
        command = input('Enter a command. Type \'options\' for help.\n>').lower()

        if command == 'exit':
            print('Game ended.')
            break
        if command == 'help':
            print('\'exit\' to end the game\n\'move\' to make a move\n')
        
        if command == 'move':
            if player_1_move == True:
                print('Player 1 move')
                player = p1
            else:
                print('Player 2 move')
                player = p2

            while True: # ensures desired spot not already taken
                move_x = int(input('Enter x (1-3): ')) - 1
                move_y = int(input('Enter y (1-3): ')) - 1 # inverted - need to fix
                if game.board[move_y][move_x] == ' ':
                    break
                print('Invalid move')
            
            game.move(move_x, move_y, player)

            player_1_move = not player_1_move # changes turns



main()