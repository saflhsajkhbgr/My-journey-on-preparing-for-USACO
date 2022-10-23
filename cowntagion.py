
n = int(input())
mp = [0 for i in range(n+1)]
for i in range(1, n):
    line = [int(i) for i in input().split()]
    mp[line[0]] += 1
    mp[line[1]] += 1


start = 1
ans = n-1
for node in range(len(mp)):
    factor = 0
    res = 1
    while res < mp[node]:
        factor += 1
        res = 2**factor
    ans += factor

print(ans)