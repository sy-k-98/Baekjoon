n = int(input())
w = list(map(int, input().split()))
answer = 0

def dfs(w, total):
    global answer
    if len(w) == 2:
        answer = max(answer, total)
        return

    for i in range(1, len(w) - 1):
        dfs(w[:i] + w[i+1:], total + (w[i-1] * w[i+1]))


dfs(w, answer)
print(answer)