"""LC 953 - Verifying an Alien Dictionary"""
def is_alien_sorted(words, order):
    rank = {c: i for i, c in enumerate(order)}
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        for j in range(len(w1)):
            if j >= len(w2):
                return False  # w1 longer than w2 with same prefix
            if rank[w1[j]] < rank[w2[j]]:
                break  # this pair is fine
            if rank[w1[j]] > rank[w2[j]]:
                return False
    return True

if __name__ == "__main__":
    cases = [
        (["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
        (["word","world","row"], "worldabcefghijkmnpqstuvxyz", False),
        (["apple","app"], "abcdefghijklmnopqrstuvwxyz", False),
    ]
    for words, order, expected in cases:
        result = is_alien_sorted(words, order)
        print(f"{words} -> {result} {'✓' if result==expected else '✗'}")
