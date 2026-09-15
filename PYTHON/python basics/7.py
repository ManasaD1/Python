
def fibonacci(n):
    """Generator that yields the first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


terms = 10

fib_sequence = list(fibonacci(terms))

print(f"First {terms} Fibonacci numbers: {fib_sequence}")

