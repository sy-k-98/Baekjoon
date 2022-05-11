n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(input())

cnt = 0
for _ in range(m):
    tmp = input()
    if tmp in arr:
        cnt += 1

print(cnt)