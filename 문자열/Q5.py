word = input().upper()
unique_word = list(set(word))
cnt = []

for w in unique_word:
    cnt.append(word.count(w))

if cnt.count(max(cnt)) > 1:
    print("?")

else:
    print(unique_word[cnt.index(max(cnt))])
