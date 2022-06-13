from itertools import combinations

def startlink():
    global answer

    for start_member in list(combinations(member, n // 2)):
        start = 0
        link = 0
        link_member = list(set(member) - set(start_member))

        for i, j in list(combinations(start_member, 2)):
            start += power[i][j]
            start += power[j][i]

        for i, j in list(combinations(link_member, 2)):
            link += power[i][j]
            link += power[j][i]

        answer = min(answer, abs(start - link))


n = int(input())
power = [list(map(int, input().split())) for _ in range(n)]
member = list(range(n))
answer = int(1e9)
startlink()

print(answer)
