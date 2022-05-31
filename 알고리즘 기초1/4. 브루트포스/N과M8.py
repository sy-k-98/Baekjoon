def DFS(start):
    if len(result) == m:
        print(*result)
        return

    for i in range(start, n):
        result.append(num[i])
        DFS(i)
        result.pop()


n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
result = []

DFS(0)