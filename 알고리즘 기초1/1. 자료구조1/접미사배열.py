import sys
input = sys.stdin.readline

s = input().rstrip()
answer = []

for i in range(len(s)):
    answer.append(s[i:])

answer.sort()

for a in answer:
    print(a)

