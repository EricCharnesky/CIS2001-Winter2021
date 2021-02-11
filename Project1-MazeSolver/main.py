from MazeSolver import MazeSolver

maze = [
    ['S', 'W', ' ', ' ', ' '],
    [' ', 'W', ' ', 'W', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', 'W', ' ', 'W', ' '],
    [' ', 'W', ' ', ' ', 'E'],
]

maze_solver = MazeSolver(maze)
maze_solver.solve()

print(maze_solver.shortest_path())

