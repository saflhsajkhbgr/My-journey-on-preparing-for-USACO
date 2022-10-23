
permutation = sorted([int(i) for i in input().split()])
pset = set(permutation)
read = []
pos = 0


def solve():
    A = permutation[0]
    for i in range(1, 7):
        for j in range(i, 7):
            B = permutation[i]
            C = permutation[j]
            if A+B+C != permutation[-1]:
                continue
            else:
                AplusB = A+B
                AplusC = A+C
                BplusC = B+C
                if AplusC in pset and AplusB in pset and BplusC in pset:
                    return A, B, C


A, B, C = solve()
print(str(A)+' '+str(B)+' '+str(C))