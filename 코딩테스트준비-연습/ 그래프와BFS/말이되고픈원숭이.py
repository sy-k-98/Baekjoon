import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
hx, hy = [-2, -2, -1, 1, 2, 2, -1, 1], [-1, 1, -2, -2, -1, 1, 2, 2]


def bfs():
    q = deque()
    q.append((0, 0, K, 0))

    visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]
    visited[0][0][K] = True
    while q:
        i, j, k, cnt = q.popleft()

        if i == (H - 1) and j == (W - 1):
            return cnt

        if k > 0:
            for m in range(8):
                ni, nj = i + hx[m], j + hy[m]

                if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] == 0 and visited[ni][nj][k - 1] == False:
                    visited[ni][nj][k - 1] = True
                    q.append((ni, nj, k - 1, cnt + 1))

        for m in range(4):
            ni, nj = i + dx[m], j + dy[m]

            if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] == 0 and visited[ni][nj][k] == False:
                visited[ni][nj][k] = True
                q.append((ni, nj, k, cnt + 1))

    return -1


K = int(input())
W, H = map(int, input().split())
arr = tuple(tuple(map(int, input().split())) for _ in range(H))
print(bfs())
