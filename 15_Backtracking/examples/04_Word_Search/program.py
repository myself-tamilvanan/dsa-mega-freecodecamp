"""LC 79 - Word Search"""
def exist(board, word):
    rows, cols = len(board), len(board[0])
    def dfs(r, c, idx):
        if idx == len(word): return True
        if r<0 or r>=rows or c<0 or c>=cols or board[r][c]!=word[idx]: return False
        temp = board[r][c]; board[r][c] = '#'  # mark visited
        found = (dfs(r+1,c,idx+1) or dfs(r-1,c,idx+1) or
                 dfs(r,c+1,idx+1) or dfs(r,c-1,idx+1))
        board[r][c] = temp  # restore
        return found
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0): return True
    return False

if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    words = ["ABCCED", "SEE", "ABCB"]
    for word in words:
        import copy
        print(f"word='{word}' -> {exist(copy.deepcopy(board), word)}")
