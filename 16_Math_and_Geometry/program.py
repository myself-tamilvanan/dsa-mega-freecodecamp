"""Chapter 16: Math & Geometry"""

def rotate(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i+1,n): matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for row in matrix: row.reverse()
    return matrix

def spiral_order(matrix):
    res=[];l,r,t,b=0,len(matrix[0]),0,len(matrix)
    while l<r and t<b:
        for c in range(l,r): res.append(matrix[t][c])
        t+=1
        for row in range(t,b): res.append(matrix[row][r-1])
        r-=1
        if not(l<r and t<b): break
        for c in range(r-1,l-1,-1): res.append(matrix[b-1][c])
        b-=1
        for row in range(b-1,t-1,-1): res.append(matrix[row][l])
        l+=1
    return res

def is_happy(n):
    def ss(x): return sum(int(d)**2 for d in str(x))
    s,f=n,ss(n)
    while f!=1 and s!=f: s=ss(s);f=ss(ss(f))
    return f==1

def my_pow(x,n):
    if n<0: x,n=1/x,-n
    res=1
    while n:
        if n%2: res*=x
        x*=x;n//=2
    return res

def gcd(a,b):
    while b: a,b=b,a%b
    return a

def sieve(n):
    p=[True]*(n+1);p[0]=p[1]=False
    for i in range(2,int(n**.5)+1):
        if p[i]:
            for j in range(i*i,n+1,i): p[j]=False
    return [i for i in range(2,n+1) if p[i]]

if __name__=="__main__":
    print("Rotate:", rotate([[1,2,3],[4,5,6],[7,8,9]]))
    print("Spiral:", spiral_order([[1,2,3],[4,5,6],[7,8,9]]))
    print("Happy 19:", is_happy(19))
    print("Pow(2,10):", my_pow(2,10))
    print("GCD(48,18):", gcd(48,18))
    print("Primes≤30:", sieve(30))
