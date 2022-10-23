
# P = [1, 1, 3, 3, 1, 2, 3]
# T = [1, 2, 5, 2, 4, 1, 4]

P = [1, 5, 3, 3, 4]
T = [1, 2, 2, 2, 1]
import random
import time

# P = [random.randint(0, 10) for i in range(15)]
# T = [random.randint(0, 10) for i in range(15)]

# gap = [0, 3, 1, 1, 3]
target = [0 for i in P]
counter = 0
while T != P:
    allinterval = []
    gap = []
    for p in range(len(P)):
        gap.append(P[p] - T[p])
    print('gap:', gap)
    longestinterval = [0]
    for g in range(len(gap)):
        # print('g:', gap[g])
        if gap[longestinterval[-1]] > 0:
            if gap[g] > 0:
                longestinterval.append(g)
            if gap[g] <= 0:
                allinterval.append(longestinterval)
                longestinterval = [g]
        elif gap[longestinterval[-1]] < 0:
            if gap[g] < 0:
                longestinterval.append(g)
            if gap[g] >= 0:
                allinterval.append(longestinterval)
                longestinterval = [g]
        if gap[longestinterval[-1]] == 0:
            longestinterval = [g]
    if longestinterval and allinterval == []:
        allinterval.append(longestinterval)
        # print('-'*100)
    print(allinterval)
    if allinterval[0] == [0, 0]:
        allinterval[0] = [0]
    longestinterval = allinterval[0]
    for i in allinterval:
        if len(i) > len(longestinterval):
            longestinterval = i
    print('longestinterval:', longestinterval)
    for l in longestinterval:
        if gap[l] < 0:
            T[l] -= 1
        if gap[l] > 0:
            T[l] += 1
    counter += 1
    print('new temp:', T)
    print('-'*100)
    if counter >= 10000:
        break


print(counter)
print(P)