
# P = [1, 1, 3, 3, 1, 2, 3]
# T = [1, 2, 5, 2, 4, 1, 4]

# P = [1, 5, 3, 3, 4]
# T = [1, 2, 2, 2, 1]
import random

# P = [random.randint(0, 100) for i in range(1000)]
# T = [random.randint(0, 100) for i in range(1000)]

# gap = [0, 3, 1, 1, 3]
num = input()
P = [int(i) for i in input().split()]
T = [int(i) for i in input().split()]

target = [0 for i in P]
counter = 0

# import time
# t1 = time.time()
while T != P:
    allinterval = []
    gap = []
    for p in range(len(P)):
        gap.append(P[p] - T[p])
    # print('gap:', gap)
    longestinterval = [0]
    for g in range(len(gap)):
        # print('g:', gap[g])
        # print('longestinterval:', longestinterval)
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
    allinterval.append(longestinterval)
    if longestinterval and allinterval == []:
        allinterval.append(longestinterval)
        # print('-'*100)
    # print('allinterval:', allinterval)
    if allinterval[0] == [0, 0]:
        allinterval[0] = [0]
    longestinterval = allinterval[0]
    for i in allinterval:
        if len(i) > len(longestinterval):
            longestinterval = i
    # print('longestinterval:', longestinterval)

    if len(longestinterval) == 1:
        for interval in allinterval:
            counter += abs(gap[interval[0]])
        break

    for l in longestinterval:
        if gap[l] < 0:
            T[l] -= 1
        if gap[l] > 0:
            T[l] += 1
    counter += 1
    # print('counter:', counter)
    # print('new temp:', T)
    # print('-'*100)
    if counter >= 10000:
        break

print(counter)
# t2 = time.time()
# print('cost:', t2-t1)
# print(P)