from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

n = int(input())

for i in range(n):
    l = int(input())
    graph = []
    for i in range(l):
        graph.append([0] * l)
    queue = deque()
    x, y = map(int, input().split())
    w, z = map(int, input().split())
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        if x == w and y == z:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    print(graph[w][z])
