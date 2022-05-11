import sys

n, m = map(int, input().split())
no_listen = []
no_see = []

for _ in range(n):
    no_listen.append(sys.stdin.readline().rstrip())

for _ in range(m):
    no_see.append(sys.stdin.readline().rstrip())

people = set(no_see) & set(no_listen)

no_see_listen = list(people)
no_see_listen.sort()

print(len(no_see_listen))
for i in no_see_listen:
    print(i)
