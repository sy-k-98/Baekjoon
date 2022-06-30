from sys import stdin
from collections import deque
input = stdin.readline

def bfs():
    q = deque()
    q.append([0, 0, 0, 1])
    visited[0][0][0] = 1
    day = True
    while q:
        p = len(q)
        for _ in range(p):
            x, y, w, d = q.popleft()
            if x == n - 1 and y == m - 1:
                return d
            for dx, dy in (-1, 0), (1, 0), (0, 1), (0, -1):
                nx, ny, nw, nd = x + dx, y + dy, w + 1, d + 1
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if arr[nx][ny] == '1' and w < k and visited[nx][ny][nw] == 0:
                    if day:
                        q.append((nx, ny, nw, nd))
                        visited[nx][ny][nw] = 1
                    else:
                        q.append((x, y, w, nd))
                if arr[nx][ny] == '0' and visited[nx][ny][w] == 0:
                    q.append((nx, ny, w, nd))
                    visited[nx][ny][w] = 1
        day = not day
    return -1


n, m, k = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]

print(bfs())
