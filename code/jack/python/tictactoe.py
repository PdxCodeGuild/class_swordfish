# Lab 10: tic tac toe
while True:
    try:
        tiles = int(input('Enter number of tiles (ex: enter 3 for 3x3 game): '))
        if 2 < tiles < 6:
            break
        else:
            print('Invalid entry: must be between 3 and 5')
    except:
        print('Invalid entry: must be integer')
    

class Game():
    def __init__(self):
        self.board = [[' ' for _ in range(tiles)] for _ in range(tiles)]

    def __repr__(self):
        board_string = f'  {" ".join((str(x + 1) for x in range(tiles)))}\n' # initiates string and adds horizontal index labels
        i = 1
        for y in self.board:
            board_string += str(i) + ' ' # adds vertical index labels
            i += 1
            board_string += '|'.join([str(y[x]) for x in range(len(y))])
            if not y is self.board[tiles - 1]: # adds new line if not last y
                board_string += f'\n  {"".join(["-" for x in range((tiles * 2) - 1)])}\n'
        return board_string

    def setup(self):
        print('Game started')
        print(self.__repr__())

    def move(self, player):
        while True: # takes spot and ensures entered spot is valid
            try:
                x = int(input(f'Enter x (1-{tiles}): ')) - 1
                y = int(input(f'Enter y (1-{tiles}): ')) - 1
                if self.board[y][x] == ' ':
                    break
                print('Invalid move')
            except:
                print('Invalid move')

        self.board[y][x] = player.token
        print(self.__repr__())
    
    def win_check(self, player): # creates lists representing current board state, then checks those lists to determine if game has been won
        win_cons = []
        # populate win_cons with lists of winning combinations to check if combos contain only player token
        for x in range(tiles):
            win_cons.append([self.board[y][x] for y in range(tiles)]) # vertical
            win_cons.append([self.board[x][y] for y in range(tiles)]) # horizontal
        win_cons.append([self.board[y][y] for y in range(tiles)]) # first diagonal
        win_cons.append([self.board[y][-y - 1] for y in range(tiles)]) # second diagonal

        if [player.token for _ in range(tiles)] in win_cons:
            return True


# allows for duplicate names, tokens - TBD if fix
class Player():
    def __init__(self, number, token):
        self.name = input(f'Enter player {number} name: ').capitalize()
        self.token = token

def main():
    print('\n\nWelcome to tic tac toe!')

    # game setup
    p1 = Player(1, 'X')
    while True:
        p2 = Player(2, 'O')
        if p2.name != p1.name:
            break
        else:
            print('Program does not support duplicate names')
    game = Game()
    game.setup()
    player = p1
    moves = 0
    
    # game REPL
    while True:
        print(f'{player.name}\'s turn')
        command = input('Enter a command (type \'help\' for options): ').lower()
        if command == 'exit':
            print('Game ended.')
            break
        if command == 'help':
            print('\'exit\' to end the game\n\'move\' to make a move\n')
        if command == 'move':
            game.move(player) # changes board state

            if game.win_check(player) == True: # checks if player won
                print(f'{player.name} wins!')
                break

            player = (p1, p2)[not (p1, p2).index(player)] # toggles players

            moves += 1
            if moves == 9:
                print('It\'s a tie!')
                break

main()
