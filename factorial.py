
def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python factorial.py <non-negative integer>")
    else:
        try:
            number = int(sys.argv[1])
            print(factorial(number))
        except ValueError as e:
            print(f"Error: {e}")

