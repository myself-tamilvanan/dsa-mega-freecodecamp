"""LC 88 - Merge Sorted Array"""
def merge(nums1, m, nums2, n):
    p1, p2, p = m-1, n-1, m+n-1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]; p1 -= 1
        else:
            nums1[p] = nums2[p2]; p2 -= 1
        p -= 1
    # Remaining nums2 elements
    nums1[:p2+1] = nums2[:p2+1]
    return nums1

if __name__ == "__main__":
    cases = [([1,2,3,0,0,0],3,[2,5,6],3),([1],1,[],0),([0],0,[1],1)]
    for n1,m,n2,n in cases:
        print(f"nums1={n1[:m]}+zeros, nums2={n2} -> {merge(n1,m,n2,n)}")
