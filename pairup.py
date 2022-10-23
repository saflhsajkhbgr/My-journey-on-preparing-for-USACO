
n = int(input())
cows = []
for i in range(n):
    line = [int(i) for i in input().split()]
    for j in range(line[0]):
        cows.append(line[1])

cows = sorted(cows)

t = 0
for i in range(len(cows)//2):
    s = cows[i] + cows[-(i + 1)]
    if s > t:
        t = s

print(t)