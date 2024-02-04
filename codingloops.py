def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]
# user input for the number of Fibonacci numbers to generate
n = int(input("Enter the number of Fibonacci numbers to generate: "))
# Generate and print Fibonacci numbers
fibonacci_series = fibonacci(n)
print(f"Fibonacci Series of {n} terms: {fibonacci_series}")
