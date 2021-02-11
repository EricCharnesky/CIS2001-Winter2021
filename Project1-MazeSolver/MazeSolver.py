import copy


class MazeSolver:

    def __init__(self, maze):
        self._maze = copy.deepcopy(maze)
        self._solution_step_counts = []
        self._current_row, self._current_column = self._find_start()
        self._current_steps = 0
        self._shortest_path = 1000000

    def _find_start(self):
        for row_index in range(len(self._maze)):
            for column_index in range(len(self._maze[row_index])):
                if self._maze[row_index][column_index] == 'S':
                    return row_index, column_index
        raise ValueError('no start found!')

    def _can_move(self, row_index, column_index):
        return 0 <= row_index < len(self._maze) and \
            0 <= column_index < len(self._maze[row_index]) and \
            (self._maze[row_index][column_index] == ' ' or
                self._maze[row_index][column_index] == 'E')

    def solve(self):

        if self._maze[self._current_row][self._current_column] == 'E':
            #print(self)

            # add step count to the list to find the min later
            self._solution_step_counts.append(self._current_steps)

            # or track this way
            if self._current_steps < self._shortest_path:
                self._shortest_path = self._current_steps

        else:

            # bread crumb
            self._maze[self._current_row][self._current_column] = 'v'
            self._current_steps += 1

            # up
            if self._can_move(self._current_row - 1, self._current_column):
                self._current_row -= 1
                self.solve()
                self._current_row += 1

            # down
            if self._can_move(self._current_row + 1, self._current_column):
                self._current_row += 1
                self.solve()
                self._current_row -= 1

            # left
            if self._can_move(self._current_row, self._current_column - 1):
                self._current_column -= 1
                self.solve()
                self._current_column += 1

            # right
            if self._can_move(self._current_row, self._current_column + 1):
                self._current_column += 1
                self.solve()
                self._current_column -= 1

            # undo breadcrumb
            self._maze[self._current_row][self._current_column] = ' '
            self._current_steps -= 1

    def shortest_path(self):
        return min(self._solution_step_counts)

    def __str__(self):
        return "\n".join(str(row) for row in self._maze) + "\n"

