from queue import Queue
nm = [int(i) for i in input().split()]
n = nm[0]
m = nm[1]


dic = {}
for i in range(1, n+1):
    dic[i] = []

for i in range(m):
    line = ([int(i) for i in input().split()])
    dic[line[0]].append(line[1])
    dic[line[1]].append(line[0])


def bfs(start):
    visited = [False for i in range(n + 1)]
    que = Queue(maxsize=0)
    que.put(start)
    visited[start] = True
    while not que.empty():
        head = que.get()
        for nex in dic[head]:
            if not visited[nex] and nex not in closes:
                visited[nex] = True
                que.put(nex)
    if visited.count(True) == n-len(closes):
        return True
    return False


closes = set([])
for i in range(n):
    if i == 0:
        ans = bfs(1)
    else:
        close = int(input())
        closes.add(close)
        for j in range(1, n+1):
            if j not in closes:
                point = j
                break
        ans = bfs(point)
        print(ans)