def DFS(start):
    if len(s) == m:
        print(*s)
        return

    for i in range(start, n+1):
        if visited[i]:
            continue

        visited[i] = True
        s.append(i)
        DFS(i+1)
        s.pop()
        visited[i] = False


n, m = map(int, input().split())
visited = [False] * (n + 1)
s = []
DFS(1)