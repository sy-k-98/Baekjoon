from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solve(x, y, wall_break_left, visited, graph):
    q = deque()
    q.append((x, y, wall_break_left))
    visited[x][y][wall_break_left] = 1

    while q:
        x, y, wall_break_left = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][wall_break_left]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0 and visited[nx][ny][wall_break_left] == 0:
                q.append((nx, ny, wall_break_left))
                visited[nx][ny][wall_break_left] = visited[x][y][wall_break_left] + 1

            if graph[nx][ny] == 1 and wall_break_left == 1:
                q.append((nx, ny, wall_break_left - 1))
                visited[nx][ny][wall_break_left - 1] = visited[x][y][wall_break_left] + 1

    return -1


print(solve(0, 0, 1, visited, graph))