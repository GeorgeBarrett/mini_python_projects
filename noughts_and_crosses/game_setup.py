import time
from player_setup import HumanPlayer, RandomComputerPlayer

class NoughtsAndCrosses:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # I will use a single list to rep a 3x3 board
        self.current_winner = None # to keep track of the champion

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: # getting rows
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        
        # I commented this code out as I can refactor it
        # moves = []
        # for (i, square) in enumerate(self.board):
        #     if square == ' ':
        #         moves.append(i)
        
        # return moves

        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_of_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check through a row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all ([spot == letter for spot in row]):
            return True 

        # check through a column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all ([spot == letter for spot in column]):
            return True

        # check through diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all ([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all ([spot == letter for spot in diagonal2]):
                return True
        
        return False

def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game or establishes a tie
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    while game.empty_squares():
        # get move from appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # defining a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' Makes a move to square {square}')
                game.print_board()
                print(' ')

            if game.current_winner:
                if print_game:
                    print(letter + ' Wins!')
                return letter

            # alternating letters
            letter = 'O' if letter == 'X' else 'X'

            # time break
            time.sleep(0.8)
        
    if print_game: 
        print('It\'s a tie')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    noughts_and_crosses = NoughtsAndCrosses()
    play(noughts_and_crosses, x_player, o_player, print_game=True)