"""LC 130 - Surrounded Regions"""
def solve(board):
    rows,cols=len(board),len(board[0])
    def dfs(r,c):
        if r<0 or r>=rows or c<0 or c>=cols or board[r][c]!='O': return
        board[r][c]='S'
        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]: dfs(r+dr,c+dc)
    for r in range(rows): dfs(r,0);dfs(r,cols-1)
    for c in range(cols): dfs(0,c);dfs(rows-1,c)
    for r in range(rows):
        for c in range(cols):
            if board[r][c]=='O': board[r][c]='X'
            elif board[r][c]=='S': board[r][c]='O'
    return board
if __name__=="__main__":
    import copy
    board=[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    print("Input:"); [print(r) for r in board]
    print("Output:"); [print(r) for r in solve(copy.deepcopy(board))]
