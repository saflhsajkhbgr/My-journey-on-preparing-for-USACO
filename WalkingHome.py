
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

print(grids)
print(Ns)
print(Ks)

# Ns = [3]
# Ks = [3]
# grids = [[[0, 0, 0], [0, _, 0], [0, 0, 0]]]


def DP():
    testcounter = 0
    anss = []
    for testcases in grids:
        print('testcase:', testcases)
        N = Ns[testcounter]
        for i in range(N):
            for j in range(N):
                if testcases[i][j] != _:
                    print('i:', i)
                    print('j:', j)
                    testcases[i][j] = []
                    print('testcases[i][j]:', testcases[i][j])
                    if i == 0 and j == 0:
                        testcases[i][j] = []
                    if i == 0 and j != 0:
                        testcases[i][j] = [['R' for k in range(j)]]
                    if i != 0 and j == 0:
                        testcases[i][j] = [['D' for k in range(i)]]
                    if i != 0 and j != 0:
                        uproute = testcases[i-1][j]
                        leftroute = testcases[i][j-1]
                        print('uproute:', uproute)
                        print('leftroute:', leftroute)
                        for route in uproute:
                            cur = []
                            for r in route:
                                cur.append(r)
                            cur.append('D')
                            print('cur:', cur)
                            turns = 0
                            flag = True
                            for r in range(len(cur)):
                                if r+1 != len(cur):
                                    if cur[r] != cur[r+1]:
                                        turns += 1
                                        if turns > Ks[testcounter]:
                                            print(cur, 'exceeds K:', Ks[testcounter], 'by turning for', turns, 'times')
                                            flag = False
                                            break
                            if flag:
                                print(cur, 'is a valid route')
                                testcases[i][j].append(cur)

                        for route in leftroute:
                            cur = []
                            for r in route:
                                cur.append(r)
                            cur.append('R')
                            print('cur:', cur)
                            turns = 0
                            flag = True
                            for r in range(len(cur)):
                                if r+1 != len(cur):
                                    if cur[r] != cur[r+1]:
                                        turns += 1
                                        if turns > Ks[testcounter]:
                                            print(cur, 'exceeds K:', Ks[testcounter], 'by turning for', turns, 'times')
                                            flag = False
                                            break
                            if flag:
                                print(cur, 'is a valid route')
                                testcases[i][j].append(cur)
                else:
                    print('infinity on:', i, j)
                    testcases[i][j] = []
                    pass

                print('testcase:', testcases)
                print('-'*100)
        testcounter += 1
        print(testcases)
        anss.append(len(testcases[-1][-1]))
    return anss


anss = DP()
print(anss)