def dfs(x, y, c):
    global answer

    color[x][y] = c
    answer = max(answer, 1)

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < n and 0 <= ny < n):
            continue

        if board[nx][ny] != 'X':
            continue

        if color[nx][ny] == -1:
            dfs(nx, ny, 1 - c)
            answer = max(answer, 2)

        if color[nx][ny] == c:
            answer = max(answer, 3)


dx = [-1, -1, 0, 0, 1, 1]
dy = [0, 1, -1, 1, -1, 0]

n = int(input())
board = [[a for a in input().rstrip()] for _ in range(n)]
color = [[-1] * n for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 'X' and color[i][j] == -1:
            dfs(i, j, 0)

print(answer)
