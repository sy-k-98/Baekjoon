from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = 1

    while q:
        x = q.popleft()

        for i in range(1, 7):
            move = x + i

            if move > 100:
                continue

            cnt = board[move]

            if visited[cnt] == 0:
                q.append(cnt)
                visited[cnt] = visited[x] + 1

                if cnt == 0:
                    return


n, m = map(int, input().split())
board = [i for i in range(101)]
visited = [0] * 101

for _ in range(n + m):
    x, y = map(int, input().split())
    board[x] = y

bfs(1)

print(visited[100] - 1)

