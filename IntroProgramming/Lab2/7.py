import random
import os

class Board:
    def __init__(self):
        self.EMPTY_SQUARE = " "
        self.PLAYER = "O"
        self.COMPUTER = "X"

        self.squares = {num: self.EMPTY_SQUARE for num in range(1, 10)}
        self.player_turn = True  # player starts first
        self.turn_counter = 0
        self.game_end = False

    def _get_rows(self) -> list[list]:
        sqrs = list(self.squares.values())

        list_of_squares = []

        # grab squares in batches of 3
        for i in range(0, len(sqrs), 3):
            list_of_squares.append(sqrs[i : i + 3])

        return list_of_squares

    def _set_square_value(self, square: int, value: str):
        # print(f"updating square {square}")
        self.squares[square] = value

    def _check_win(self, moves: list[str], current_player: str) -> bool:
        all_player_moves = [True if move == current_player else False for move in moves]
        if all(all_player_moves):
            self.display_board()
            if current_player == self.PLAYER:
                print("🔥 Congratulation! You won! 🔥")
            else:
                print("😭 You've lost this time. Try again! 😭")
            self.game_end = True
            return True

        return False

    def _check_end_game(self):
        current_player = self.PLAYER if self.player_turn else self.COMPUTER
        all_rows = self._get_rows()

        # row win
        for row in all_rows:
            if self._check_win(row, current_player=current_player):
                return

        # col win
        for col in range(3):
            checking_col = []

            # gather values for column
            for row in all_rows:
                checking_col.append(row[col])

            if self._check_win(checking_col, current_player=current_player):
                return

        # diag win
        all_moves = list(self.squares.values())
        left_right_diag = [all_moves[0], all_moves[4], all_moves[-1]]
        right_left_diag = [all_moves[2], all_moves[4], all_moves[6]]

        for diag in [left_right_diag, right_left_diag]:
            if self._check_win(diag, current_player=current_player):
                return

        # draw when all spaces filled
        if self.turn_counter == 9:
            self.display_board()
            print("DRAW!")
            self.game_end = True
            return

    def make_move(self, square: str) -> None:
        square = int(square)

        # square already filled
        if self.squares[square] != self.EMPTY_SQUARE:
            print("❌ Invalid move! That square is already filled.")
            return -1

        value = self.PLAYER if self.player_turn else self.COMPUTER

        self._set_square_value(square=square, value=value)

        # Increment turn counter
        self.turn_counter += 1

        # check win | lose | draw
        self._check_end_game()

        # swap turn state
        self.player_turn = not self.player_turn

    def _get_empty_squares(self) -> list[int]:
        empty_squares = []
        for square, value in self.squares.items():
            if value == self.EMPTY_SQUARE:
                empty_squares.append(square)

        return empty_squares

    def _get_computer_move(self) -> str:
        empty_squares = self._get_empty_squares()

        computer_choice = str(random.choice(empty_squares))

        return computer_choice

    def play(self, square: str) -> None:
        invalid_move = self.make_move(square=square) == -1
        if invalid_move:
            print("Try again")
            self.display_board()
            return

        # Player already wins, don't allow computer to play
        if self.game_end:
            return

        computer_choice = self._get_computer_move()
        self.make_move(computer_choice)

        if not self.game_end:
            self.display_board()

    def _render_row(self, row_num: int):
        row = self._get_rows()[row_num]
        stringified_row = " | ".join(row)

        print(stringified_row)

    def display_board(self) -> None:
        """Renders and prints the current board"""

        for row in range(3):
            self._render_row(row)

            # row separation line
            if row < 2:
                print("-" * 9)
            else:
                print("" * 9)


def solution_7():
    os.system('cls')
    board = Board()
    print("👋 Welcome to the Tic Tac Toe game!")
    print("Player [O] plays first against Computer [X]")
    board.display_board()
    while not board.game_end:
        player_move = input("🤔 Make your [O] move [1-9]: ")
        board.play(player_move)


solution_7()
