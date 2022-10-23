
NMK = [int(i) for i in input().split()]
N = NMK[0]
M = NMK[1]
K = NMK[2]

# _ = float('inf')
num = [1 for i in range(N)]
k = 0
pos = 1
last = 0
while k<=K:
    num[pos] = pos+1
    if pos == 1:
        k += 5
        last = k
    else:
        k = last + pos+2
        last = k
    pos += 1
    print(k)