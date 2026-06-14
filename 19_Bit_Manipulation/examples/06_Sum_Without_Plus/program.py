"""LC 371 - Sum of Two Integers Without + or -"""
def get_sum(a,b):
    mask=0xFFFFFFFF
    while b&mask:
        carry=(a&b)<<1
        a=a^b
        b=carry
    return (a&mask) if b>0 else a
if __name__=="__main__":
    cases=[(1,2,3),(2,3,5),(-1,1,0),(-2,-3,-5),(100,200,300)]
    for a,b,expected in cases:
        result=get_sum(a,b)
        print(f"{a}+{b}={result} {'✓' if result==expected else '✗'}")
