def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    :param n: Non-negative integer
    :return: Factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
if __name__ == "__main__":
    number = int(input("Enter a non-negative integer: "))
    try:
        print(f"The factorial of {number} is {factorial(number)}")
    except ValueError as e:
        print(e)