w, h, x, y, p = map(int, input().split())
cnt = 0

for _ in range(p):
    a, b = map(int, input().split())

    if (a - x) ** 2 + (b - (y + h/2)) ** 2 <= (h/2) ** 2 and a < x:
        cnt += 1

    elif x <= a <= x + w and y <= b <= y + h:
        cnt += 1

    elif (a - (x + w)) ** 2 + (b - (y + h/2)) ** 2 <= (h/2) ** 2 and a > x + w:
        cnt += 1

print(cnt)