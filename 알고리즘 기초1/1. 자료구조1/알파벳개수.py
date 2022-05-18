x = input()
abc = [0] * 26
for i in x:
    abc[ord(i)-ord('a')] += 1

print(*abc)