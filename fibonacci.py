def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence[:n]

# Test the function
n_terms = int(input("Enter the number of terms for Fibonacci sequence: "))
fib_sequence = fibonacci(n_terms)
print("Fibonacci sequence:")
print(fib_sequence)