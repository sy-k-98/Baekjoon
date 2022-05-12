import sys
input = sys.stdin.readline

def check(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[x] - board[i]) == x - i:
            return False
    return True


def dfs(x):
    global cnt

    if x == N:
        cnt += 1
        return

    for i in range(N):
        if visited[i]:
            continue

        board[x] = i

        if check(x):
            visited[i] = True
            dfs(x + 1)
            visited[i] = False


N = int(input())
cnt = 0
board = [0] * N
visited = [False] * N
dfs(0)
print(cnt)
