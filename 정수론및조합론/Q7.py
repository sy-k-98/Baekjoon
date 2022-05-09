def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


n, k = map(int, input().split())

result = factorial(n) / (factorial(n-k) * factorial(k))
print(int(result))
