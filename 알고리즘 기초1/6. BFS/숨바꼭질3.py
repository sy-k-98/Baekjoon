from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break

        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= MAX and not visited[i]:
                if i == x * 2 and x != 0:
                    visited[i] = visited[x]
                    q.appendleft(i)
                else:
                    visited[i] = visited[x] + 1
                    q.append(i)


MAX = 10 ** 5
visited = [0] * (MAX + 1)
n, k = map(int, input().split())

bfs()