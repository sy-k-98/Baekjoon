n = int(input())
num = []

for _ in range(n):
    x, y = map(int, input().split())
    num.append((x, y))

num.sort()

for i, j in num:
    print(i, j)