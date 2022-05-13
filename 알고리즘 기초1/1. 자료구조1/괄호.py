import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    test = input().rstrip()
    stack = []
    for i in test:
        if i == '(':
            stack.append(i)

        elif i == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")
