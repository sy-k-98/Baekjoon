def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


n, s = map(int, input().split())
A = list(map(int, input().split()))
ans = abs(s - A[0])

if s == 1:
    print(ans)
else:
    for i in range(1, n):
        ans = gcd(ans, abs(s - A[i]))

    print(ans)