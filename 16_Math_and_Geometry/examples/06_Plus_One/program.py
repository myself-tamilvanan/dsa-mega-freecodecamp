"""LC 66 - Plus One"""
def plus_one(digits):
    for i in range(len(digits)-1,-1,-1):
        if digits[i]<9:
            digits[i]+=1
            return digits
        digits[i]=0
    return [1]+digits  # all nines case
if __name__=="__main__":
    cases=[[1,2,3],[4,3,2,1],[9],[9,9,9],[1,9,9]]
    for d in cases:
        print(f"{d} -> {plus_one(d[:])}")
