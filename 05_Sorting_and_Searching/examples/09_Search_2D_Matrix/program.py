"""LC 74 - Search a 2D Matrix"""
def search_matrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    l, r = 0, m*n - 1
    while l <= r:
        mid = (l+r)//2
        val = matrix[mid//n][mid%n]
        if val == target: return True
        elif val < target: l = mid+1
        else: r = mid-1
    return False

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    for target in [3,13,0,60]:
        print(f"target={target} -> {search_matrix(matrix, target)}")
