import sys

n = int(input())
num = []

for _ in range(n):
    num.append(int(sys.stdin.readline()))

for i in sorted(num):
    print(i)