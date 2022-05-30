n = int(input())

for _ in range(n):
    M, N, x, y = map(int, input().split())
    f = -1
    while x <= M * N:
        if x % N == y % N:
            f = x
            break
        x += M

    print(f)