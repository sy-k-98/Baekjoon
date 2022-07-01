from collections import deque

def bfs(v):
    q = deque([v])

    while q:
        num, result = q.popleft()

        if num == t:
            return result

        for op in ('*', '+', '/'):
            if op == '*':
                n = num * num
            elif op == '+':
                n = num + num
            else:
                n = 1

            if 0 <= n <= t and n not in visited:
                visited.add(n)
                q.append([n, result + op])

    return -1


s, t = map(int, input().split())
visited = set()

if s == t:
    print(0)
else:
    visited.add(s)
    print(bfs([s, '']))