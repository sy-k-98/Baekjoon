s = input()
result = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        tmp = s[i:j+1]
        result.add(tmp)

print(len(result))


