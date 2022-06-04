from itertools import combinations

n, s = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0

for i in range(1, n + 1):
    com = combinations(num, i)

    for c in com:
        if sum(c) == s:
            cnt += 1

print(cnt)