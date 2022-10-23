
from queue import Queue

NM = [int(i) for i in input().split()]
n = NM[0]
m = NM[1]

milks = [0]
for i in input():
    milks.append(i)

dic = {}
for i in range(1, n+1):
    dic[i] = []

for i in range(n-1):
    line = [int(i) for i in input().split()]
    dic[line[0]].append(line[1])
    dic[line[1]].append(line[0])
# print(dic)


def dfs(cur, dest, milk, hasH, hasG):
    global ans
    if visited[cur]:
        return
    visited[cur] = True

    if milks[cur] == 'H':
        hasH = True
    if milks[cur] == 'G':
        hasG = True

    if cur == dest:
        if milk == 'G' and hasG:
            ans = '1'
            return
        if milk == 'H' and hasH:
            ans = '1'

    for nex in dic[cur]:
        if not visited[nex]:
            dfs(nex, dest, milk, hasH, hasG)


walks = []
for i in range(m):
    line = [i for i in input().split()]
    walks.append(line)


for walk in walks:
    ans = '0'
    visited = [False for i in range(n + 1)]
    milk_met = False
    # print(walk)
    dfs(int(walk[0]), int(walk[1]), walk[2], False, False)
    print('ans:', ans)