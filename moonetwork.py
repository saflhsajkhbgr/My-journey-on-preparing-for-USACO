

mn = [int(i) for i in input().split()]
m = mn[1]
n = mn[0]
coordinates = [[0, 0]]
for i in range(n):
    coor = [int(i) for i in input().split()]
    coordinates.append(coor)

# cons = [[0 for i in range(n+1)] for j in range(n+1)]
dic = {}
for i in range(1, n+1):
    dic[i] = []

for i in range(m):
    connection = [int(i) for i in input().split()]
    dic[connection[0]].append(connection[1])
    dic[connection[1]].append(connection[0])


def dfs(start):
    if visited[start]:
        return
    visited[start] = True
    global xmax, ymax, xmin, ymin
    xmax = max(coordinates[start][0], xmax)
    xmin = min(coordinates[start][0], xmin)
    ymax = max(coordinates[start][1], ymax)
    ymin = min(coordinates[start][1], ymin)
    for nex in dic[start]:
        if not visited[nex]:
            dfs(nex)


parameters = []
for i in range(1, n+1):
    visited = [False for i in range(n + 1)]
    _ = float('inf')
    groups = []
    xmin = _
    ymin = _
    ymax = 0
    xmax = 0
    if not visited[i]:
        dfs(i)
    # print(xmax, xmin, ymax, ymin)
    parameter = (xmax-xmin+ymax-ymin)*2
    parameters.append(parameter)

ans = min(parameters)
print(ans)