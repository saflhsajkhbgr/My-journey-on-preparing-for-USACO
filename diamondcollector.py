
NK = [int(i) for i in input().split()]
n = NK[0]
K = NK[1]

diamonds = []
for i in range(n):
    diamonds.append(int(input()))

diamonds = sorted(diamonds)

left = 0
right = -1
ans = 0
for i in range(n):
    if i == 0:
        window_fromleft = [diamonds[i]]
        window_fromright = [diamonds[-1]]
    else:
        window_fromleft.append(diamonds[i])
        window_fromright.append(diamonds[-(i+1)])

    while max(window_fromleft)-min(window_fromleft) > K:
        left += 1
        window_fromleft = window_fromleft[1:]

    while max(window_fromright) - min(window_fromright) > K:
        right -= 1
        window_fromright = window_fromright[:-1]

    total_diamond = len(window_fromright) + len(window_fromleft)
    if total_diamond > ans:
        ans = total_diamond

print(ans)