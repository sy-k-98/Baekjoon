n = int(input())
answer = ""

while n != 0:

    if n % (-2) != 0:
        n = n // (-2) + 1
        answer += '1'
    else:
        n = n // (-2)
        answer += '0'

if answer == "":
    answer += '0'

print(answer[::-1])