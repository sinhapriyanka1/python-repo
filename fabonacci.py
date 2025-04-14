def fibonacci(n):
    """Generate the Fibonacci sequence up to the nth number."""
    print("---")
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage
if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    print("Fibonacci sequence:", fibonacci(n))