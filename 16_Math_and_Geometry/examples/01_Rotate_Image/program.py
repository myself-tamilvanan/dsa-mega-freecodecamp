"""LC 48 - Rotate Image"""
def rotate(matrix):
    n = len(matrix)
    # Transpose
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for row in matrix: row.reverse()
    return matrix

def rotate_ccw(matrix):
    """Rotate 90° counter-clockwise: transpose then reverse columns"""
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n//2):
        matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]
    return matrix

if __name__ == "__main__":
    m1 = [[1,2,3],[4,5,6],[7,8,9]]
    m2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    import copy
    for m in [m1, m2]:
        print(f"Original: {m}")
        print(f"Rotated CW: {rotate(copy.deepcopy(m))}")
