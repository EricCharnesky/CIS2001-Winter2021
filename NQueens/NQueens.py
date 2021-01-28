class NQueens:

    def __init__(self, size):
        self.board = []
        for row in range(size):
            self.board.append([])
            for column in range(size):
                self.board[row].append(' ')

        self.number_of_queens_on_board = 0
        self.is_solved = False
        self.solution_count = 0
        self.size = size

    def solve(self):
        if self.number_of_queens_on_board == 23:
            print()
        #print(self)
        if self.number_of_queens_on_board == self.size:
            self.is_solved = True
            print(self)
            self.solution_count += 1
        if not self.is_solved:
            for row in range(len(self.board)):
                if self._can_put_queen(row):
                    self.board[row][self.number_of_queens_on_board] = 'Q'
                    self.number_of_queens_on_board += 1
                    self.solve()
                    self.number_of_queens_on_board -= 1
                    self.board[row][self.number_of_queens_on_board] = ' '

    def _can_put_queen(self, row):
        return self._row_is_clear(row) and \
            self._diagonal_up_is_clear(row) and \
            self._diagonal_down_is_clear(row)

    def _row_is_clear(self, row):
        return 'Q' not in self.board[row]

    def _diagonal_up_is_clear(self, row):
        current_row = row - 1
        current_column = self.number_of_queens_on_board - 1

        while current_column >= 0 and current_row >= 0:
            if self.board[current_row][current_column] == 'Q':
                return False
            current_row -= 1
            current_column -= 1

        return True

    def _diagonal_down_is_clear(self, row):
        current_row = row + 1
        current_column = self.number_of_queens_on_board - 1

        while current_column >= 0 and current_row < len(self.board):
            if self.board[current_row][current_column] == 'Q':
                return False
            current_row += 1
            current_column -= 1

        return True

    def __str__(self):
        result = ""
        for row in self.board:
            result += str(row) + '\n'
        result += '\n'
        return result

