import sys
input = sys.stdin.readline

while True:
    x = input().rstrip("\n")
    lower, upper, num, space = 0, 0, 0, 0

    if not x:
        break

    for i in x:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isdigit():
            num += 1
        elif i.isspace():
            space += 1

    print(lower, upper, num, space)





