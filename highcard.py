

n = int(input())
inp = set([])
for i in range(n):
    inp.add(int(input()))

Elsie = []
Bessie = []
for i in range(2*n):
    if i+1 in inp:
        Elsie.append(i+1)
    else:
        Bessie.append(i+1)
# print(Elsie)
# print(Bessie)
counter = 0
shift = 0
i = 0
while i+shift < n:
    if Bessie[i+shift] > Elsie[i]:
        i += 1
        counter += 1
    else:
        shift += 1

print(counter)