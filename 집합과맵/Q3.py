import sys

n, m = map(int, sys.stdin.readline().split())

pokemon = []
pokemon_num = {}
for i in range(n):
    po = sys.stdin.readline().rstrip()
    pokemon.append(po)
    pokemon_num[po] = i + 1

for _ in range(m):
    tmp = sys.stdin.readline().rstrip()
    if tmp.isdigit():
        print(pokemon[int(tmp) - 1])
    else:
        print(pokemon_num[tmp])

