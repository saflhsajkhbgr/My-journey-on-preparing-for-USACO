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


def dfs(cur, HorG):
    if visited[cur]:
        return
    groups[cur] = id
    visited[cur] = True
    for nex in dic[cur]:
        if milks[nex] == HorG:
            dfs(nex, HorG)


walks = []
for i in range(m):
    line = [i for i in input().split()]
    walks.append(line)


ans = '0'
groups = [0 for i in range(n+1)]
milkgroup = [0]
visited = [False for i in range(n + 1)]
id = 1

while True:
    cur = visited[1:].index(False)+1
    if milks[cur] == 'H':
        milkgroup.append('H')
        dfs(cur, 'H')
    else:
        milkgroup.append('G')
        dfs(cur, 'G')
    id += 1
    if visited.count(False) == 1:
        break

# print(groups)
# print(milkgroup)

finalans = ''
for walk in walks:
    # print(walk)
    ans = '0'
    if groups[int(walk[0])] != groups[int(walk[1])]:
        ans = '1'
    elif walk[2] == milkgroup[groups[int(walk[0])]]:
        ans = '1'
    finalans += ans

"""
连通分量，将节点分组
"""

print(finalans)