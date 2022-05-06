from collections import Counter
import sys

n = int(sys.stdin.readline())

num = []

for _ in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()

print(round(sum(num) / len(num)))

print(num[len(num) // 2])

cnt = Counter(num).most_common(2)

if len(num) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(num[-1] - num[0])