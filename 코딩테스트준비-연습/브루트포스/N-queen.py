def check(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[x] - board[i]) == x - i:
            return False
    return True


def dfs(x):
    global cnt

    if x == n:
        cnt += 1
        return

    for i in range(n):
        board[x] = i
        if check(x):
            dfs(x + 1)


n = int(input())
board = [0] * n
cnt = 0
dfs(0)

print(cnt)