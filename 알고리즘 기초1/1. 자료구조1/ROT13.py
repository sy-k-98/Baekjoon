import sys
input = sys.stdin.readline

s = input().rstrip()
answer = ""

for i in s:
    if 'a' <= i <= 'm':
        answer += chr(ord(i) + 13)
    elif 'n' <= i <= 'z':
        answer += chr(ord(i) - 13)
    elif 'A' <= i <= 'M':
        answer += chr(ord(i) + 13)
    elif 'N' <= i <= 'Z':
        answer += chr(ord(i) - 13)
    else:
        answer += i

for i in answer:
    print(i, end="")

