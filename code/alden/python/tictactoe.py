# Tik-tak-toe

class Player():
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Board():
    def __init__(self):
        self.board = [[' ' for r in range(3)] for r in range(3)]  # Creates a list of 3 lists with ' ' holder for the token later.
        # print(self.board)

    def __repr__(self):
        rows = ''
        for i, sub in enumerate(self.board): # Enumerates through list of list to space things into a grid.
            rows += '|'.join(sub)
            rows += '\n'
            if i < 2:
                rows += '- - -'
                rows += '\n'
        return rows

    def move(self, x, y, player):
        if self.board[x][y] != ' ':
            print('Space is taken.')
        else:
            self.board[x][y] = player
            return self.board

    def calc_winner(self, player): # Use zip in for loop to get vertical solution.
        for i in range(3):
            hori = self.board[i]        # horizonal check
            list = [s==hori[0] and s != ' ' for s in hori] # creates a list of booleans
            if all(list):           # Checks that list of booleans are all True.
                    return f'{hori[0]} wins!'
            
        else:
            print('check')
            # elif self.board[i]
            # print(i) #sub)
            

board = Board()
board.move(1, 0, 'X')
board.move(1, 1, 'X')
board.move(1, 2, 'X')
print(board)
print(board.calc_winner('X'))