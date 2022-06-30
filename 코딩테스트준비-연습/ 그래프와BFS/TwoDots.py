from sys import stdin
input = stdin.readline

def cycle(color, x, y, cnt, start_x, start_y):
    global ans

    if ans is True:
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if cnt >= 4 and nx == start_x and ny == start_y:
            ans = True
            return

        if board[nx][ny] == color and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            cycle(color, nx, ny, cnt + 1, start_x, start_y)
            visited[nx][ny] = 0


def game_start():
    for i in range(n):
        for j in range(m):
            start_x, start_y = i, j
            visited[start_x][start_y] = 1
            cycle(board[i][j], i, j, 1, start_x, start_y)
            if ans:
                return 'Yes'
    return 'No'


n, m = map(int, input().split())
board = [[a for a in input().rstrip()] for _ in range(n)]

visited = [[0] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

ans = False


print(game_start())