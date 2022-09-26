# Tik-tak-toe

class Player():
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __repr__(self):
        return self.token

    def player_2(self):
        if player_1 == 'O':
            player_2 == 'x'
        else:
            player_2 == 'O'

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

    def calc_winner(self): # Use zip in for loop to get vertical solution.
        vert = list(zip(*self.board))
        for i in range(3):
            vert_check = vert[i]
            check = [s==vert_check[0] and s != ' ' for s in vert_check]
            if all(check):
                return f'{vert_check[0]} wins!'
        
        for i in range(3):
            hori = self.board[i]        # horizonal check
            row = [s==hori[0] and s != ' ' for s in hori] # creates a list of booleans
            if all(row):           # Checks that list of booleans are all True.
                    return f'{hori[0]} wins!'

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board != ' ':
            return f'{self.board[0][0]} wins!'

        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board != ' ':
            return f'{self.board[0][2]} wins!'
        else:
            pass

    def is_full(self):
        for i in self.board:
            if any(posi == ' ' for posi in i):
                return False
        else:
            True
            
    def is_game_over(self):
        if self.is_full() == True:
            return f'Tied game'
        else:
            return self.calc_winner()

board = Board()
player_1 = Player('Alden', 'X')
player_2 = Player('Joe', 'O')
round = 1
print(player_1)
print(player_2)
while True:
    p1_move = Board.move(input('Input x coordinate: '), input('Input y coordinate: '), player_1) # Keep getting error "TypeError: Board.move() missing 1 required positional argument: 'player'"
    p2_move = Board.move(input('Input x coordinate: '), input('Input y coordinate: '), player_2)
    round += 1

    if round >= 3:
        Board.is_game_over()

    if Board.is_game_over() == True:
        print(board)
        break



# board.move(0, 0, 'X')
# board.move(1, 0, 'X')
# board.move(2, 0, 'X')
# print(board)
# print(board.is_full())