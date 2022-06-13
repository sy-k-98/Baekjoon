from itertools import combinations

n = int(input())
s = list(map(int, input().split()))
num = [0] * 2000001
num[0] = 1
for i in range(1, n + 1):
    com = combinations(s, i)
    for c in com:
        num[sum(c)] = 1

print(num.index(0))
