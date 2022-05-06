n = int(input())
num = []

for _ in range(n):
    x, y = map(int, input().split())
    num.append((x, y))

sort_num = sorted(num, key = lambda x : (x[1], x[0]))

for i, j in sort_num:
    print(i, j)