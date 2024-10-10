def fibonacci(n, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

def printFibonacciSeries(n):
    memo = {}
    for i in range(n):
        print(fibonacci(i, memo), end=" ")

n = int(input("Enter the number of terms in Fibonacci series: "))
print(f"Fibonacci series up to {n} terms:")
printFibonacciSeries(n)
