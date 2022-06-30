from collections import deque
from sys import stdin
input = stdin.readline

def bfs():
    q = deque()
    q.append([0, 0, k])
    visited[0][0][k] = 1
    while q:
        x, y, z = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and z > 0 and visited[nx][ny][z - 1] == 0:
                    visited[nx][ny][z - 1] = visited[x][y][z] + 1
                    q.append([nx, ny, z - 1])
                elif arr[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append([nx, ny, z])
    return -1


n, m, k = map(int, input().split())
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
arr = [list(map(int, input().strip())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

print(bfs())
