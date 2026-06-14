"""LC 54 - Spiral Matrix"""
def spiral_order(matrix):
    result = []
    l, r = 0, len(matrix[0])
    t, b = 0, len(matrix)
    while l < r and t < b:
        for c in range(l, r): result.append(matrix[t][c])  # top row
        t += 1
        for row in range(t, b): result.append(matrix[row][r-1])  # right col
        r -= 1
        if not (l < r and t < b): break
        for c in range(r-1, l-1, -1): result.append(matrix[b-1][c])  # bottom row
        b -= 1
        for row in range(b-1, t-1, -1): result.append(matrix[row][l])  # left col
        l += 1
    return result

def generate_spiral_matrix(n):
    """LC 59 - Generate spiral matrix filled with 1..n²"""
    matrix = [[0]*n for _ in range(n)]
    l, r, t, b = 0, n-1, 0, n-1
    num = 1
    while l <= r and t <= b:
        for c in range(l, r+1): matrix[t][c]=num; num+=1
        t+=1
        for row in range(t, b+1): matrix[row][r]=num; num+=1
        r-=1
        for c in range(r, l-1, -1): matrix[b][c]=num; num+=1
        b-=1
        for row in range(b, t-1, -1): matrix[row][l]=num; num+=1
        l+=1
    return matrix

if __name__ == "__main__":
    m = [[1,2,3],[4,5,6],[7,8,9]]
    print("Spiral order:", spiral_order(m))
    print("Generate 3x3 spiral:")
    for row in generate_spiral_matrix(3): print(" ", row)
