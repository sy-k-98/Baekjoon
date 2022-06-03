from itertools import combinations

l, c = map(int, input().split())
alphabet = sorted(input().split())
com = list(combinations(alphabet, l))

for i in com:
    cnt_a = 0
    cnt_b = 0
    for j in i:
        if j in "aeiou":
            cnt_a += 1
        else:
            cnt_b += 1

    if cnt_a >= 1 and cnt_b >= 2:
        print("".join(i))


