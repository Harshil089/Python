def fib (n,memo={}):
    if n in memo:
        return memo[n]
    if n<=2:
        return n
    memo[n]=fib(n-1,memo) + fib(n-2,memo)
    return memo[n]
n=199
print(f"The Fibonacci series for n={n} is: {fib(n)}")

# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
# n = 50
# print(f"Fibonacci number at position {n} is: {fibonacci(n)}")
