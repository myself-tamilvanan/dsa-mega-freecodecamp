"""Chapter 15: Backtracking"""

def subsets(nums):
    res=[]
    def bt(i,path):
        res.append(path[:])
        for j in range(i,len(nums)): path.append(nums[j]);bt(j+1,path);path.pop()
    bt(0,[]);return res

def permutations(nums):
    res=[]
    def bt(path,rem):
        if not rem: res.append(path[:]);return
        for i in range(len(rem)): path.append(rem[i]);bt(path,rem[:i]+rem[i+1:]);path.pop()
    bt([],nums);return res

def combination_sum(candidates,target):
    res=[]
    def bt(i,path,rem):
        if rem==0: res.append(path[:]);return
        if rem<0: return
        for j in range(i,len(candidates)): path.append(candidates[j]);bt(j,path,rem-candidates[j]);path.pop()
    bt(0,[],target);return res

def solve_n_queens(n):
    res=[];cols=set();pos=set();neg=set();board=['.'*n]*n
    def bt(r):
        if r==n: res.append(board[:]);return
        for c in range(n):
            if c in cols or r+c in pos or r-c in neg: continue
            cols.add(c);pos.add(r+c);neg.add(r-c)
            board[r]='.'*c+'Q'+'.'*(n-c-1);bt(r+1)
            cols.remove(c);pos.remove(r+c);neg.remove(r-c);board[r]='.'*n
    bt(0);return res

if __name__=="__main__":
    print("Subsets [1,2,3]:", subsets([1,2,3]))
    print("Permutations [1,2,3]:", permutations([1,2,3]))
    print("Combination Sum [2,3,6,7],7:", combination_sum([2,3,6,7],7))
    print("N-Queens(4) count:", len(solve_n_queens(4)))
