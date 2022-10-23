
n = int(input())
line = []
for i in range(n):
    inp = int(input())
    line.append(inp)
right = sorted(line)
print(line)
print(right)
count = 0
for i in range(n):
    if right[i]!=line[i]:
        count+=1

ans = max(0, count-1)
print(ans)