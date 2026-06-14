"""LC 695 - Max Area of Island"""
def max_area_of_island(grid):
    rows, cols = len(grid), len(grid[0])
    def dfs(r, c):
        if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]!=1: return 0
        grid[r][c] = 0  # mark visited
        return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
    return max((dfs(r,c) for r in range(rows) for c in range(cols) if grid[r][c]==1), default=0)

if __name__ == "__main__":
    import copy
    cases = [
        [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0]],
        [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]],
        [[0,0,0,0,0]],
    ]
    for grid in cases:
        print(f"Max area: {max_area_of_island(copy.deepcopy(grid))}")
