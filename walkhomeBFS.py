cases = input()
_ = float('inf')

Ns = []
Ks = []
grids = []

for i in range(int(cases)):
    NandK = input().split()
    Ks.append(int(NandK[1]))
    Ns.append(int(NandK[0]))
    grid = []
    for j in range(int(NandK[0])):
        line = input()
        l = []
        for pos in line:
            if pos == '.':
                # l.append([])
                l.append(0)
            else:
                l.append(_)
        grid.append(l)
    grids.append(grid)


def down(i, j):
    return i+1, j

def right(i, j):
    return i, j+1


movement = [right, down]
testcounter = 0
for testcases in grids:
    routes = [[[0, 0, []]]]
    i = 0
    e = [len(testcases)-1, len(testcases)-1]
    flag = True
    print('routes[i]:', routes[i])
    while flag:
        route = []
        print('i:', i)
        for r in routes[i]:
            if not flag:
                break
            for m in movement:
                i, j = m(r[0], r[1])
                if testcases[i][j] == _:
                    pass
                else:
                    turns = 0
                    for string in range(len(r[2])):
                        if r[string] != r[string+1]:
                            turns += 1
                            if turns > Ks[testcounter]:
                                break
                    if turns <= Ks[testcounter]:
                        route.append([i, j, [str(m)]])
        for r in route:
            if r[0] == e[0] and r[1] == e[1]:
                flag = False
        i += 1
    print(routes)
    testcounter += 1