
_ = float('inf')

with open('taming.in', 'r') as file:
    n = file.readline()
    line = [int(i) for i in file.readline().split()]
    line[0] = 0
    line.reverse()

# line = [1, -1, -1, 0]
# line = [-1, -1, 3, -1, 2, 1, 0, 1, 0]


def minimum():
    lmin = line.copy()
    for record in range(len(lmin)):
        if line[record] == -1 and lmin[record] != 0:
            lmin[record] = _
        elif line[record] != 0:
            lmin[record] = _
            lmin[record+line[record]] = 0
    return lmin.count(0)


def maximum():
    lmax = line.copy()
    for record in range(len(lmax)):
        if line[record] == -1:
            lmax[record] = 0
        elif line[record] != 0:
            lmax[record+line[record]] = 0
    return lmax.count(0)


ans = [minimum(), maximum()]
with open('taming.out', 'w') as file:
    file.write(str(ans[0]) + ' ' + str(ans[1]))