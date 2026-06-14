"""LC 4 - Median of Two Sorted Arrays"""
def find_median_sorted_arrays(nums1, nums2):
    A, B = nums1, nums2
    if len(A) > len(B): A, B = B, A
    m, n = len(A), len(B)
    l, r = 0, m
    while l <= r:
        i = (l+r)//2  # partition A
        j = (m+n+1)//2 - i  # partition B
        maxL_A = A[i-1] if i>0 else float('-inf')
        minR_A = A[i] if i<m else float('inf')
        maxL_B = B[j-1] if j>0 else float('-inf')
        minR_B = B[j] if j<n else float('inf')
        if maxL_A<=minR_B and maxL_B<=minR_A:
            if (m+n)%2: return float(max(maxL_A,maxL_B))
            return (max(maxL_A,maxL_B)+min(minR_A,minR_B))/2
        elif maxL_A>minR_B: r=i-1
        else: l=i+1

if __name__=="__main__":
    cases=[([1,3],[2]),([1,2],[3,4]),([0,0],[0,0]),([],[1])]
    for a,b in cases:
        print(f"{a} + {b} -> median={find_median_sorted_arrays(a,b)}")
