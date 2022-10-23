
n = int(input())
cows = [int(i) for i in input().split()]
cows = sorted(cows, reverse=True)
ans = n
for i in range(n):
    if cows[i] < i:
        ans = i
        break
print(ans)