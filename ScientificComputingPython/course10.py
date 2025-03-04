from typing import List, Optional, Tuple

class Board:
    def __init__(self, board: List[List[int]]):
        """
        Initialize the board with a 2D list.
        :param board: 2D list representing the Sudoku board.
        """
        self.board = board

    def __str__(self) -> str:
        """
        Return a string representation of the board.
        :return: String representation of the board.
        """
        board_str = ''
        for row in self.board:
            row_str = [str(i) if i else '*' for i in row]
            board_str += ' '.join(row_str) + '\n'
        return board_str

    def find_empty_cell(self) -> Optional[Tuple[int, int]]:
        """
        Find the next empty cell in the board.
        :return: Tuple of row and column indices of the empty cell, or None if no empty cell is found.
        """
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row: int, num: int) -> bool:
        return num not in self.board[row]

    def valid_in_col(self, col: int, num: int) -> bool:
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row: int, col: int, num: int) -> bool:
        """
        Check if a number is valid in the 3x3 square containing the given cell.
        """
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty: Tuple[int, int], num: int) -> bool:
        """
        Check if a number is valid in the given cell.
        :param empty: Tuple of row and column indices of the cell.
        :param num: Number to check.
        :return: True if the number is valid in the cell, False otherwise.
        """
        row, col = empty
        return all([
            self.valid_in_row(row, num),
            self.valid_in_col(col, num),
            self.valid_in_square(row, col, num)
        ])

    def solver(self) -> bool:
        """
        Solve the Sudoku puzzle using backtracking.
        :return: True if the puzzle is solved, False otherwise.
        """
        if (next_empty := self.find_empty_cell()) is None:
            return True
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess
                # call solver recursively for the board with the new guess
                if self.solver():
                    return True
                # created unsolvable puzzle - take one step back
                self.board[row][col] = 0
        return False

def solve_sudoku(board: List[List[int]]) -> Board:
    """
    Solve the given Sudoku puzzle and print the result.
    :param board: 2D list representing the Sudoku board.
    :return: Board object representing the solved puzzle.
    """
    gameboard = Board(board)
    print(f'Puzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('The provided puzzle is unsolvable.')
    return gameboard

puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

solve_sudoku(puzzle)
