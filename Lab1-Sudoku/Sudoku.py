class SudokuSolver:

    def __init__(self, board):
        self._board = board

    def __str__(self):
        return "\n".join(str(row) for row in self._board)

    def solve(self):
        row_index, column_index = self._next_open_position()
        for number in range(1, 10):
            if self._is_not_solved() and self._can_place_number(number, row_index, column_index):
                self._board[row_index][column_index] = number
                self.solve()
                if self._is_not_solved():
                    self._board[row_index][column_index] = ' '

    def _is_not_solved(self):
        for row in self._board:
            if ' ' in row:
                return True
        return False

    def _next_open_position(self):
        for row_index in range(len(self._board)):
            for column_index in range(len(self._board)):
                if self._board[row_index][column_index] == ' ':
                    return row_index, column_index
        return -1, -1

    def _can_place_number(self, number, row_index, column_index):
        return self._can_place_number_in_row(number, row_index) and \
            self._can_place_number_in_column(number, column_index) and \
            self._can_place_number_in_3_by_3(number, row_index, column_index)

    def _can_place_number_in_row(self, number, row_index):
        return number not in self._board[row_index]

    def _can_place_number_in_column(self, number, column_index):
        for row in self._board:
            if number == row[column_index]:
                return False
        return True

    def _can_place_number_in_3_by_3(self, number, row_index, column_index):
        row_index_start = (row_index // 3) * 3
        column_index_start = (column_index // 3) * 3

        for current_row_index in range(row_index_start, row_index_start+3):
            for current_column_index in range(column_index_start, column_index_start+3):
                if self._board[current_row_index][current_column_index] == number:
                    return False
        return True
