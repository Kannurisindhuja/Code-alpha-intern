def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


num_terms: int = 10
fib_sequence = fibonacci(num_terms)
print(f"first {num_terms} terms of the fibonacci sequence:")
print(fib_sequence)
