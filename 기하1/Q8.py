T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = list(map(int, input().split()))

    n = int(input())
    cnt = 0
    for _ in range(n):
        x, y, r = map(int, input().split())
        start = ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5
        end = ((x2 - x) ** 2 + (y2 - y) ** 2) ** 0.5

        if start < r and end < r:
            pass
        elif start < r:
            cnt += 1
        elif end < r:
            cnt += 1

    print(cnt)
