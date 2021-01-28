from NQueens import NQueens

for n in range(4, 40):
    puzzle = NQueens(n)
    puzzle.solve()