"""Chapter 04: Strings"""

def fizz_buzz(n):
    return ["FizzBuzz" if i%15==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else str(i) for i in range(1,n+1)]

def longest_common_prefix(strs):
    if not strs: return ""
    p=strs[0]
    for s in strs[1:]:
        while not s.startswith(p): p=p[:-1]
        if not p: return ""
    return p

def encode(strs): return ''.join(f"{len(s)}#{s}" for s in strs)
def decode(s):
    res=[]; i=0
    while i<len(s):
        j=s.index('#',i); l=int(s[i:j]); res.append(s[j+1:j+1+l]); i=j+1+l
    return res

def count_substrings(s):
    n=len(s); cnt=0
    def expand(l,r):
        nonlocal cnt
        while l>=0 and r<n and s[l]==s[r]: cnt+=1;l-=1;r+=1
    for i in range(n): expand(i,i); expand(i,i+1)
    return cnt

def longest_palindrome(s):
    st=mx=0; n=len(s)
    def expand(l,r):
        nonlocal st,mx
        while l>=0 and r<n and s[l]==s[r]:
            if r-l+1>mx: mx=r-l+1;st=l
            l-=1;r+=1
    for i in range(n): expand(i,i); expand(i,i+1)
    return s[st:st+mx]

if __name__=="__main__":
    print("FizzBuzz 15:", fizz_buzz(15))
    print("LCP:", longest_common_prefix(["flower","flow","flight"]))
    enc=encode(["hello","world"]); print("Encode:", enc, "Decode:", decode(enc))
    print("Palindromic Substrings 'aaa':", count_substrings("aaa"))
    print("Longest Palindrome 'babad':", longest_palindrome("babad"))
