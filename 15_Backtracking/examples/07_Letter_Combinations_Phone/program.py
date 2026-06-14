"""LC 17 - Letter Combinations of a Phone Number"""
def letter_combinations(digits):
    if not digits: return []
    phone={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    result=[]
    def bt(idx,path):
        if idx==len(digits): result.append(''.join(path));return
        for c in phone[digits[idx]]:
            path.append(c);bt(idx+1,path);path.pop()
    bt(0,[])
    return result
if __name__=="__main__":
    for d in ["23","79","2","","9"]:
        print(f"'{d}' -> {letter_combinations(d)}")
