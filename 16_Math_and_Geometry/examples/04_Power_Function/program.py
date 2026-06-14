"""LC 50 - Pow(x, n)"""
def my_pow(x, n):
    if n < 0: x, n = 1/x, -n
    result = 1.0
    while n:
        if n % 2:  # odd: multiply x once more
            result *= x
        x *= x
        n //= 2
    return result

def my_pow_recursive(x, n):
    """Recursive version"""
    if n == 0: return 1
    if n < 0: return my_pow_recursive(1/x, -n)
    if n % 2 == 0:
        return my_pow_recursive(x*x, n//2)
    return x * my_pow_recursive(x*x, n//2)

if __name__ == "__main__":
    cases = [(2.0,10),(2.1,3),(2.0,-2),(0.00001,2147483647),(1.0,-2147483648)]
    for x,n in cases:
        result = my_pow(x,n)
        print(f"pow({x},{n}) = {result:.6f}")
