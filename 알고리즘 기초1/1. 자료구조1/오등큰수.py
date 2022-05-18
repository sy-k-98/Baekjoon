import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().strip().split()))
cnt = Counter(a)

answer = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and cnt[a[stack[-1]]] < cnt[a[i]]:
        answer[stack.pop()] = a[i]
    stack.append(i)

print(*answer)
