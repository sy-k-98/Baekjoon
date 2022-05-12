def DFS():
    if len(s) == m:
        print(*s)
        return

    for i in range(1, n+1):
        if visited[i]:
            continue

        visited[i] = True
        s.append(i)
        DFS()
        s.pop()
        visited[i] = False


n, m = map(int, input().split())
visited = [False] * (n + 1)
s = []
DFS()


