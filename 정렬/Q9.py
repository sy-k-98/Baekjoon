n = int(input())
people = []

for _ in range(n):
    age, name = input().split()
    people.append((int(age), name))

people.sort(key=lambda x: x[0])

for p1, p2 in people:
    print(p1, p2)