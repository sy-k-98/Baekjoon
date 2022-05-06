k = input()
alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=','z=']
cnt = 0

for i in alphabet:
    k = k.replace(i, '*')

print(len(k))
