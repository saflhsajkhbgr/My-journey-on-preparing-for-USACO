from queue import Queue


class Mirror:
    def __init__(self, ind, x, y, dir, steps):
        self.ind = ind
        self.x = x
        self.y = y
        self.dir = dir
        self.steps = steps


line = [int(i) for i in input().split()]

start = [line[1], line[2]]
dest = [line[3], line[4]]

dic = {}
mirrors = []
mirrors.append(start)
dic[0] = []
for i in range(1, line[0]+1):
    mirror = [int(i) for i in input().split()]
    mirrors.append(mirror)
    dic[i] = []

for i in dic:
    for j in range(len(mirrors)):
        if (mirrors[j][0] == mirrors[i][0] or mirrors[j][1] == mirrors[i][1]) and mirrors[j] != mirrors[i]:
            # [x, y, coming direction, steps]
            dic[i].append(j)

# print(mirrors)
# print(dic)


def bfs(s):
    visited = [False for i in range(line[0]+1)]
    que = Queue(maxsize=0)
    mir1 = Mirror(0, s[0], s[1], 'H', steps=0)
    mir2 = Mirror(0, s[0], s[1], 'V', steps=0)
    que.put(mir1)
    que.put(mir2)
    visited[0] = True
    while not que.empty():
        head = que.get()
        # print(head.x, head.y, head.steps)
        if head.x == dest[0] or head.y == dest[1]:
            return head.steps
        for nex in dic[head.ind]:
            dir = head.dir
            if not visited[nex]:
                if dir == 'H' and mirrors[nex][1] == head.y:
                    mir = Mirror(nex, mirrors[nex][0], mirrors[nex][1], 'V', steps=head.steps+1)
                    que.put(mir)
                elif dir == 'V' and mirrors[nex][0] == head.x:
                    mir = Mirror(nex, mirrors[nex][0], mirrors[nex][1], 'H', steps=head.steps+1)
                    que.put(mir)


ans = bfs(start)
print(ans)