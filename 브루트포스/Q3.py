n = int(input())

h = []
rank = []

for _ in range(n):
    x, y = map(int, input().split())
    h.append((x, y))

for i in range(n):
    cnt = 1
    for j in range(n):
        if h[i][0] < h[j][0] and h[i][1] < h[j][1]:
            cnt += 1
    rank.append(cnt)

for i in rank:
    print(i, end=" ")
