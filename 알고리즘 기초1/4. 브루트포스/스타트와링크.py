from itertools import combinations

def solve():
    global answer

    for start_member in list(combinations(member, n // 2)):
        start = link = 0
        link_member = list(set(member) - set(start_member))

        for i, j in list(combinations(start_member, 2)):
            start += s[i][j]
            start += s[j][i]

        for i, j in list(combinations(link_member, 2)):
            link += s[i][j]
            link += s[j][i]

        answer = min(answer, abs(start - link))


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
member = list(range(n))
answer = int(1e9)
solve()
print(answer)

