
together = []
x = int(input())
for i in range(x):
    line = input().split()
    together.append(line)

separate = []
y = int(input())
for i in range(y):
    line = input().split()
    separate.append(line)

groups = []
g = int(input())
for i in range(g):
    line = input().split()
    s = set([])
    for j in line:
        s.add(j)
    groups.append(s)
# print(groups)
# print(together)
# print(separate)

vio = 0
for pairs in together:
    for group in groups:
        if pairs[0] in group:
            if not(pairs[1] in group):
                vio += 1
                break

for pairs in separate:
    for group in groups:
        if pairs[0] in group:
            if pairs[1] in group:
                vio += 1
                break

print(vio)