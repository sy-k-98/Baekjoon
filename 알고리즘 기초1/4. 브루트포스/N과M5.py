def DFS():
    if len(result) == m:
        print(*result)
        return

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        result.append(num[i])
        DFS()
        result.pop()
        visited[i] = False


n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
visited = [False] * (n + 1)
result = []

DFS()