from itertools import combinations
import sys

input = sys.stdin.readline().rstrip

def solve():
    global answer
    global diff

    for a in range(1, int((n / 2) + 1)):
        member_divided = combinations(member, a)

        for b in member_divided:
            start = link = 0
            start_member = list(b)
            link_member = list(set(member) - set(start_member))

            for i in range(n-1):
                for j in range(n-1):
                    try:
                        start_num = s[start_member[i]][start_member[j]]
                    except:
                        start_num = 0
                    try:
                        link_num = s[link_member[i]][link_member[j]]
                    except:
                        link_num = 0
                    start += start_num
                    link += link_num

            diff = min(diff, abs(start - link))
        answer = min(answer, diff)


print()

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
member = list(range(n))
answer, diff = int(1e9), int(1e9)
solve()
print(answer)

