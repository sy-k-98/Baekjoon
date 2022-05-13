import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    words = list(input().rstrip().split())
    reverse_words = []

    for word in words:
        reverse_words.append(word[::-1])

    result = " ".join(reverse_words)

    print(result)


