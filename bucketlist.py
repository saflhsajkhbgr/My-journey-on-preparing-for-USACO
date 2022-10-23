

_ = float('inf')

with open('blist.in', 'r') as file:
    n = file.readline()
    cows = []
    Max = 0
    for i in range(int(n)):
        line = file.readline().split()
        cows.append([int(i) for i in line])
        if int(line[1]) > Max:
            Max = int(line[1])

# Max = 13
# cows = [[4, 10, 1], [8, 13, 3], [2, 6, 2]]

timestamp = [[] for i in range(Max)]

for i in range(len(cows)):
    for j in range(cows[i][0], cows[i][1]):
        timestamp[j].append(cows[i][2])

ans = max([sum(i) for i in timestamp])
with open('blist.out', 'w') as file:
    file.write(str(ans))

# print(ans)