
"""
5 10
4 10
6 15
3 5
4 9
3 6
"""

NM = [int(i) for i in input().split()]
n = NM[0]
m = NM[1]
flavors = []
spiciness = []
for i in range(n):
    line = [int(i) for i in input().split()]
    flavors.append(line[0])
    spiciness.append(line[1])


_ = float('inf')
ans = _
flavor = 0
left = 0
for i in range(n):
    flavor += flavors[i]
    while flavor >= m:
        flavor -= flavors[left]
        left += 1
    spice = max(spiciness[left:i+1])
    if spice < ans:
        ans = spice

print(ans)