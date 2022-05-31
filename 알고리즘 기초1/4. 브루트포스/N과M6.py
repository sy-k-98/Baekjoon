def DFS(start):
    if len(result) == m:
        print(*result)
        return

    for i in range(start, n):
        if visited[i]:
            continue

        visited[i] = True
        result.append(num[i])
        DFS(i)
        result.pop()
        visited[i] = False


n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
visited = [False] * (n + 1)
result = []

DFS(0)