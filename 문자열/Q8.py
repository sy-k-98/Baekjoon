word = list(input())
alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

time = 0

for i in word:
    for alpha in alphabet:
        if i in alpha:
            time += alphabet.index(alpha) + 3

print(time)