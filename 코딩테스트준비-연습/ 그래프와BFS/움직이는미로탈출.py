from collections import deque
import sys
input = sys.stdin.readline

board, wall, answer = [input().rstrip() for _ in range(8)], set(), 0
# 벽 위치 추가
for i in range(8):
    for j in range(8):
        if board[i][j] == '#':
            wall.add((i, j))
# 9가지 방향 정의
steps = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
# 방문 표시 집합 생성
visited = set()
# 큐 정의
q = deque()
q.append((7, 0))

# 큐가 빌 때까지 반복
while q:
    for _ in range(len(q)):
        x, y = q.popleft()
        # 현재 위치에 벽이 있다면 건너뛰기
        if (x, y) in wall:
            continue
        # 현재 위치가 도착 지점이라면
        if x == 0 and y == 7:
            # 1이 정답
            answer = 1
            # 반복문 탈출
            break
        # 이동할 수 있는 모든 방향에 대하여
        for dx, dy in steps:
            nx = x + dx
            ny = y + dy
            # 조건을 만족한다면
            if 0 <= nx <= 7 and 0 <= ny <= 7 and not (nx, ny) in visited and not (nx, ny) in wall:
                # 방문 표시 추가
                visited.add((nx, ny))
                # 큐에 추가
                q.append((nx, ny))
    # 벽이 있다면 방문 표시 초기화
    if wall:
        visited = set()
    # 다음 위치에 있는 벽 집합 생성
    next_wall = set()
    # 다음 벽의 위치 추가
    for x, y in wall:
        if x < 7:
            next_wall.add((x+1, y))
    # 벽 위치를 업데이트
    wall = next_wall

print(answer)