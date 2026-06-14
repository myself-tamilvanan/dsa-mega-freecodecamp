"""LC 271 - Encode and Decode Strings"""
def encode(strs):
    return ''.join(f"{len(s)}#{s}" for s in strs)

def decode(s):
    result = []
    i = 0
    while i < len(s):
        j = s.index('#', i)
        length = int(s[i:j])
        result.append(s[j+1:j+1+length])
        i = j+1+length
    return result

if __name__=="__main__":
    test_cases = [["hello","world"],[""],["#","#hello#"],["with spaces","and\nnewlines"]]
    for strs in test_cases:
        enc = encode(strs)
        dec = decode(enc)
        print(f"Original: {strs}")
        print(f"Encoded:  '{enc}'")
        print(f"Decoded:  {dec}")
        print(f"Match: {strs == dec}\n")
