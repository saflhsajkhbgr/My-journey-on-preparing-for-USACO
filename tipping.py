
n = int(input())
grid = []
for i in range(n):
    grid.append([int(i) for i in input()])
# print(grid)
import pprint
# with open('cowtip.in') as file:
#     n = int(file.readline())
#     grid = []
#     for i in range(n):
#         line = file.readline()[0:-1]
#         temp = []
#         for pos in line:
#             temp.append(int(pos))
#         grid.append(temp)

correct = [[0 for i in range(n)] for j in range(n)]
ans = 0
line = 0
while grid != correct:
    while 1 not in grid[line]:
        line += 1
    one = grid[line].index(1)
    for nextline in range(line, n):
        for pos in range(one, n):
            if grid[nextline][pos] == 1:
                grid[nextline][pos] = 0
            else:
                grid[nextline][pos] = 1

    pprint.pprint(grid)
    ans += 1

print(ans)
# with open('cowtip.out', 'w') as file:
#     file.write(str(ans))