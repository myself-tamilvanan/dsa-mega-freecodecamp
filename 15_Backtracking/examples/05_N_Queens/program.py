"""LC 51 - N-Queens"""
def solve_n_queens(n):
    result = []
    cols = set(); pos_diag = set(); neg_diag = set()
    board = ['.' * n] * n
    def backtrack(row):
        if row == n:
            result.append(board[:]); return
        for col in range(n):
            if col in cols or (row+col) in pos_diag or (row-col) in neg_diag:
                continue
            cols.add(col); pos_diag.add(row+col); neg_diag.add(row-col)
            board[row] = '.'*col + 'Q' + '.'*(n-col-1)
            backtrack(row+1)
            cols.remove(col); pos_diag.remove(row+col); neg_diag.remove(row-col)
            board[row] = '.'*n
    backtrack(0)
    return result

if __name__ == "__main__":
    for n in [1, 4, 5, 6]:
        solutions = solve_n_queens(n)
        print(f"N={n}: {len(solutions)} solution(s)")
        if n == 4:
            for sol in solutions:
                print("  Solution:")
                for row in sol: print(f"    {row}")
