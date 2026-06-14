"""LC 13 - Roman to Integer"""
def roman_to_int(s):
    values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = 0
    prev = 0
    for c in reversed(s):
        curr = values[c]
        if curr < prev:
            result -= curr
        else:
            result += curr
        prev = curr
    return result

if __name__ == "__main__":
    cases = [("III",3),("LVIII",58),("MCMXCIV",1994),("IV",4),("IX",9)]
    for s, expected in cases:
        result = roman_to_int(s)
        print(f"'{s}' -> {result} {'✓' if result==expected else f'✗ expected {expected}'}")
