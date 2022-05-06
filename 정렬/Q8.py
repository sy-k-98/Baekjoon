import sys

n = int(sys.stdin.readline())
word = []

for _ in range(n):
    word.append(sys.stdin.readline().strip())

word_set = list(set(word))

word_set.sort(key = lambda x : (len(x), x))

for w in word_set:
    print(w)