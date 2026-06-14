"""LC 73 - Set Matrix Zeroes"""
def set_zeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    first_row = any(matrix[0][j]==0 for j in range(cols))
    first_col = any(matrix[i][0]==0 for i in range(rows))
    # Mark using first row/col
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j]==0: matrix[i][0]=0; matrix[0][j]=0
    # Zero out based on markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0]==0 or matrix[0][j]==0: matrix[i][j]=0
    if first_row:
        for j in range(cols): matrix[0][j]=0
    if first_col:
        for i in range(rows): matrix[i][0]=0
    return matrix

if __name__ == "__main__":
    import copy
    cases = [[[1,1,1],[1,0,1],[1,1,1]], [[0,1,2,0],[3,4,5,2],[1,3,1,5]]]
    for m in cases:
        orig = copy.deepcopy(m)
        print(f"Input:  {orig}")
        print(f"Output: {set_zeroes(m)}")
