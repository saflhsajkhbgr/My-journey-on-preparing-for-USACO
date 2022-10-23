
n = int(input())

cows = [[0 for i in range(3)] for j in range(n+1)]

for i in range(1, n+1):
    line = [int(i) for i in input().split()]
    cows[i] = line

dic = {}
for i in range(1, n+1):
    dic[i] = []
print(cows)
for cow1 in range(1, n+1):
    for cow2 in range(cow1+1, n+1):
        # print(cows[cow1])
        # print(cows[cow2])
        if (cows[cow1][0]-cows[cow2][0])**2 + (cows[cow1][1]-cows[cow2][1])**2 <= cows[cow1][2]**2:
            dic[cow1].append(cow2)
            dic[cow2].append(cow1)
# print(dic)


def dfs(a):
    # a/b: code
    if visited[a]:
        return
    global ans
    ans += 1
    visited[a] = True
    for nex in dic[a]:
        if not visited[nex]:
            dfs(nex)


visited = [False for j in range(n+1)]
anss = []
for i in range(1, n+1):
    if not visited[i]:
        ans = 0
        dfs(i)
        anss.append(ans)

print(max(anss))