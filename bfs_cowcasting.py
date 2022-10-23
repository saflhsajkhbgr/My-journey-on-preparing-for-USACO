
from queue import Queue

que = Queue(maxsize=0)

n = int(input())
cows = [[0 for i in range(3)] for j in range(n+1)]
for i in range(1, n+1):
    line = [int(i) for i in input().split()]
    cows[i] = line


mat = [[0 for i in range(n+1)] for j in range(n+1)]
for cow1 in range(1, n+1):
    for cow2 in range(cow1+1, n+1):
        if (cows[cow1][0]-cows[cow2][0])**2 + (cows[cow1][1]-cows[cow2][1])**2 <= cows[cow1][2]**2:
            mat[cow1][cow2] = 1
            mat[cow2][cow1] = 1

visited = [False for i in range(n+1)]
ans = 0


def bfs(start):
    que.put(start)
    visited[start] = True
    while not que.empty():
        head = que.get()
        global ans
        ans += 1
        for i in range(len(mat[head])):
            if mat[head][i] == 1 and not visited[i]:
                visited[i] = True
                que.put(i)


anss = []
for i in range(1, n+1):
    if not visited[i]:
        ans = 0
        bfs(i)
        anss.append(ans)

print(max(anss))
