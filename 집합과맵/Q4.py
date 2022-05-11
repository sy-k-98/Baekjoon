from collections import Counter
import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().rstrip().split()))

num_cnt = Counter(num)

for i in range(m):
    if card[i] in num_cnt:
        print(num_cnt[card[i]], end=' ')
    else:
        print(0, end=' ')
