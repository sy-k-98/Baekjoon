import sys
input = sys.stdin.readline

stack_L = list(input().rstrip())
stack_R = []
m = int(input())

for _ in range(m):
    tmp = input()
    if tmp[0] == 'L':
        if len(stack_L) == 0:
            continue
        stack_R.append(stack_L.pop())

    elif tmp[0] == 'D':
        if len(stack_R) == 0:
            continue
        stack_L.append(stack_R.pop())

    elif tmp[0] == 'B':
        if len(stack_L) == 0:
            continue
        stack_L.pop()

    elif tmp[0] == 'P':
        stack_L.append(tmp[2])

stack_L.extend(stack_R[::-1])

print("".join(stack_L))



