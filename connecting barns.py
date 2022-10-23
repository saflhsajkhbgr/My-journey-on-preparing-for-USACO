
from queue import Queue

T = int(input())


def bfs(start):
    global ID
    que = Queue(maxsize=0)
    que.put(start)
    visited[start] = True
    while not que.empty():
        head = que.get()
        print('cur:', head)
        groupid[head] = ID
        for nex in dic[head]:
            if not visited[nex]:
                print('nex:', nex)
                visited[nex] = True
                que.put(nex)


for i in range(T):
    nm = [int(i) for i in input().split()]
    n = nm[0]
    m = nm[1]
    dic = {}
    for j in range(n+1):
        dic[j] = []
    for j in range(m):
        line = [int(i) for i in input().split()]
        dic[line[0]].append(line[1])
        dic[line[1]].append(line[0])
    print(dic)

    groupid = [0 for i in range(n+1)]
    visited = [False for i in range(n+1)]

    ID = 1
    for j in range(1, n+1):
        if not visited[j]:
            bfs(j)
            ID += 1

    print(groupid)


    # 单连线
    _ = float('inf')
    single_min_cost = _
    for j in range(len(groupid)):
        for k in range(len(groupid)):
            if groupid[j] == 1 and groupid[k] == max(groupid):
                cost = (k-j)**2
                if cost < single_min_cost:
                    single_min_cost = cost
    print(single_min_cost)

    # 双连线
    double_min_cost1 = _
    double_min_cost2 = _

    # index: groupid, value: min cost from starter group to current station
    staion1 = [0 for i in range(len(groupid)-1)]
    # index: groupid, value: min cost from destination group to current station
    staion2 = [0 for i in range(len(groupid)-1)]

    for j in range(len(groupid)):
        if groupid[j] == 1:
            for k in range(len(groupid)):
                if groupid[k] != 1 and groupid!= max(groupid):
                    double_min_cost1 = min((k-j)**2, double_min_cost1)
                    staion1[groupid[k]] = double_min_cost1

    for j in range(len(groupid)):
        if groupid[j] == max(groupid):
            for k in range(len(groupid)):
                if groupid[k] != 1 and groupid!= max(groupid):
                    double_min_cost2 = min((k-j)**2, double_min_cost2)
                    staion2[groupid[k]] = double_min_cost2

    print(staion1)
    print(staion2)