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

    def calc_winner(self, player):
        for i in range(len(self.board)):     # Use zip in for loop to get vertical solution.
            if all(self.board[i]) == True and self.board[i] != ' ': # horizonal check
                print(f'{player} is the winner!!')
        else:
            print('check')
            # elif self.board[i]
            # print(i) #sub)
            

board = Board()
board.move(0, 0, 'X')
board.move(0, 1, 'X')
board.move(0, 2, 'X')
print(board)
print(board.calc_winner('X'))