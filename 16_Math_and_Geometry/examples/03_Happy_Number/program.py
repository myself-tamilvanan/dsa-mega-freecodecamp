"""LC 202 - Happy Number"""
def is_happy(n):
    def sum_squares(x):
        total = 0
        while x: total += (x%10)**2; x //= 10
        return total
    slow, fast = n, sum_squares(n)
    while fast != 1 and slow != fast:
        slow = sum_squares(slow)
        fast = sum_squares(sum_squares(fast))
    return fast == 1

def happy_sequence(n, max_steps=20):
    """Show the sequence for understanding"""
    def ss(x): return sum(int(d)**2 for d in str(x))
    seq = [n]
    for _ in range(max_steps):
        next_n = ss(seq[-1])
        if next_n in seq or next_n == 1:
            seq.append(next_n); break
        seq.append(next_n)
    return seq

if __name__ == "__main__":
    for n in [19, 2, 7, 100, 1]:
        result = is_happy(n)
        seq = happy_sequence(n)
        print(f"n={n}: happy={result}, sequence={seq[:8]}{'...' if len(seq)>8 else ''}")
