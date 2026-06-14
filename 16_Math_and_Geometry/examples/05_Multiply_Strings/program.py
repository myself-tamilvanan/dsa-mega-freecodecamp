"""LC 43 - Multiply Strings"""
def multiply(num1,num2):
    m,n=len(num1),len(num2)
    res=[0]*(m+n)
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            mul=int(num1[i])*int(num2[j])
            p1,p2=i+j,i+j+1
            total=mul+res[p2]
            res[p2]=total%10
            res[p1]+=total//10
    result=''.join(map(str,res)).lstrip('0')
    return result or '0'
if __name__=="__main__":
    cases=[("2","3","6"),("123","456","56088"),("0","52","0"),("999","999","998001")]
    for n1,n2,expected in cases:
        result=multiply(n1,n2)
        print(f"{n1}×{n2}={result} {'✓' if result==expected else '✗'}")
