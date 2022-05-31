def DFS(start):
    if len(result) == m:
        print(*result)
        return

    flag = 0
    for i in range(start, n):
        if visited[i] or flag == num[i]:
            continue

        visited[i] = True
        result.append(num[i])
        flag = num[i]
        DFS(i)
        result.pop()
        visited[i] = False


n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
visited = [False] * n
result = []


DFS(0)