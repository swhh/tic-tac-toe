import string


class Board:
    def __init__(self):
        self.player_one_turn = True
        self.player_one = "X"
        self.player_two = "O"
        self.board = list(string.digits[:9])

    def make_move(self, position):
        if type(position) != int:
            return print("Please select a number")
        elif position > len(self.board) or position < 0:
            return print("Please pick a number between 0 and 9")
        elif self.board[position] in [self.player_one, self.player_two]:
            return print("That position is occupied")
        else:
            if self.player_one_turn:
                self.board[position] = self.player_one
            else:
                self.board[position] = self.player_two
        self.player_one_turn = not self.player_one_turn

    def is_game_over(self):
        for i in range(3):
            col = self.board[i::3]
            if col.count(col[0]) == len(col):
                return True
            row = self.board[i*3:i*3 + 3]
            if row.count(row[0]) == len(row):
                return True
        centre = self.board[5]
        if self.board[0] == centre and self.board[8] == centre:
            return True
        if self.board[2] == centre and self.board[6] == centre:
            return True

    def __str__(self):
        board = ""
        for i, position in enumerate(self.board):
            if i % 3 != 0:
                board += "|"
            board += position
            if i == 2 or i == 5:
                board += "\n"
                board += ("-" * 5)
                board += "\n"
        return board


new_board = Board()
print("Let's play tic tac toe!\n")
while True:
    player = "one" if new_board.player_one_turn else "two"
    move = int(input(f"Player {player}, please make your move"))
    new_board.make_move(move)
    print(new_board)
    if new_board.is_game_over():
        print(f"Player {player}, you have won!\n")
        print("Let's play tik tak toe again!\n")
        new_board = Board()




