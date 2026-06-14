"""LC 125 - Valid Palindrome"""
def is_palindrome(s):
    l, r = 0, len(s)-1
    while l < r:
        while l<r and not s[l].isalnum(): l+=1
        while l<r and not s[r].isalnum(): r-=1
        if s[l].lower() != s[r].lower(): return False
        l+=1; r-=1
    return True

if __name__=="__main__":
    cases = ["A man, a plan, a canal: Panama", "race a car", " ", "0P"]
    for s in cases:
        print(f"'{s}' -> {is_palindrome(s)}")
