"""LC 131 - Palindrome Partitioning"""
def partition(s):
    result=[]
    def is_palindrome(sub): return sub==sub[::-1]
    def backtrack(start,path):
        if start==len(s): result.append(path[:]); return
        for end in range(start+1,len(s)+1):
            if is_palindrome(s[start:end]):
                path.append(s[start:end])
                backtrack(end,path)
                path.pop()
    backtrack(0,[])
    return result
if __name__=="__main__":
    for s in ["aab","a","aa","racecar"]:
        parts=partition(s)
        print(f"'{s}' -> {len(parts)} partitions: {parts}")
