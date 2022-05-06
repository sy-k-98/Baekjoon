import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

cnt = {}

xx = sorted(set(x))

for i in range(len(xx)):
    cnt[xx[i]] = i

for i in x:
    print(cnt[i], end = ' ')


