
inp = [int(i) for i in input().split()]
m = inp[0]
n = inp[1]
grid = []
for i in range(m):
    grid.append([j for j in input()])


def check(a, b):
    if str(a[0])+str(a[1])+str(b[0])+str(b[1]) in record or str(b[0])+str(b[1])+str(a[0])+str(a[1]) in record:
        return False
    else:
        record.add(str(a[0])+str(a[1])+str(b[0])+str(b[1]))
        record.add(str(b[0])+str(b[1])+str(a[0])+str(a[1]))
    return True
# print(grid)

ans = 0
record = set([])

for line in range(m):
    for column in range(n):
        # print(line)
        # print(column)
        if grid[line][column] == 'G':
            region = []
            coor = []
            if line-1>=0:
                region.append(grid[line-1][column])
                coor.append([line-1, column])
            else:
                region.append('.')
                coor.append([])
            if line +1 <= m-1:
                region.append(grid[line+1][column])
                coor.append([line+1, column])
            else:
                region.append('.')
                coor.append([])
            if column-1 >=0:
                region.append(grid[line][column-1])
                coor.append([line, column-1])
            else:
                region.append('.')
                coor.append([])
            if column+1 <= n-1:
                region.append(grid[line][column+1])
                coor.append([line, column+1])
            else:
                region.append('.')
                coor.append([])
            # print(region)

            # up, down, left, right
            if region[0] == 'C' and region[1] == 'C':
                # up & down
                ans += 1
            elif region[2] == 'C' and region[3] == 'C':
                # left & right
                ans += 1
            elif region[0] == 'C' and region[2] == 'C':
                # up & left
                if check(coor[0], coor[2]):
                    ans += 1
            elif region[0] == 'C' and region[3] == 'C':
                # up & right
                if check(coor[0], coor[3]):
                    ans += 1
            elif region[1] == 'C' and region[2] == 'C':
                # down & left
                if check(coor[1], coor[2]):
                    ans += 1
            elif region[1] == 'C' and region[3] == 'C':
                # down & right
                if check(coor[1], coor[3]):
                    ans += 1


print(ans)