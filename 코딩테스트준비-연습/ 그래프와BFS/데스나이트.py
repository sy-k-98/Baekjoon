from collections import deque

def bfs():
    q = deque()
    q.append([r1, c1])
    visited[r1][c1] = 1

    while q:
        x, y = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])


n = int(input())
r1, c1, r2, c2 = map(int, input().split())

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

visited = [[0] * n for _ in range(n)]

bfs()

print(visited[r2][c2] - 1)