from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    clothes = []
    for _ in range(n):
        a, b = input().split()
        clothes.append(b)
    num = 1
    cnt = Counter(clothes)
    for c in cnt:
        num *= cnt[c] + 1

    print(num - 1)