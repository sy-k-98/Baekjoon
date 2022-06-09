from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            answer = []

            while x != n:
                answer.append(x)
                x = path[x]
            answer.append(n)
            answer.reverse()
            print(' '.join(map(str, answer)))
            return

        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= MAX and not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)
                path[i] = x


MAX = 10 ** 5
visited = [0] * (MAX + 1)
path = [0] * (MAX + 1)
n, k = map(int, input().split())

bfs()