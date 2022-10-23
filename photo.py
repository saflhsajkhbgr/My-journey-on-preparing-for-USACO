
n = int(input())
current = [int(i) for i in input().split()]
target = [int(i) for i in input().split()]

if current == target:
    print(0)
    exit()

indices = {}

for i, j in enumerate(target):
    indices[j] = i


ans = 0
for i in range(n):
    ind = target.index(current[-(i+1)])
    for j in range(i, n):
        if ind < indices[current[-(j+1)]]:
            ans += 1
            break

print(ans)