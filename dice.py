import random
_ = float('inf')

# d1 = [4, 5, 6, 7]
# d2 = [2, 4, 5, 10]

# d1 = [2, 2, 2, 2]
# d2 = [1, 1, 1, 1]

d1s = []
d2s = []
n = int(input())
for i in range(n):
    line = [int(i) for i in input().split()]
    d1s.append(sorted(line[0:4]))
    d2s.append(sorted(line[4:8]))


def solve(d1, d2):
    d1greater = [[i, j] for j in range(4) for i in range(4) if d1[i] > d2[j]]
    d2greater = [[i, j] for j in range(4) for i in range(4) if d2[i] > d1[j]]
    if len(d1greater) > len(d2greater):
        A = d1
        B = d2
    else:
        A = d2
        B = d1

    # print('A:', A)
    # print('B:', B)
    # Aaxis = [_ for i in range(10)]
    # Baxis = [_ for i in range(10)]
    # for i in range(len(Aaxis)):
    #     if i in range(0, A[0]):
    #         Aaxis[i] = 0
    #     elif i in range(A[0], A[1]):
    #         Aaxis[i] = 1
    #     elif i in range(A[1], A[2]):
    #         Aaxis[i] = 2
    #     elif i in range(A[2], A[3]):
    #         Aaxis[i] = 3
    #     elif i in range(A[3], 10):
    #         Aaxis[i] = 4
    #
    # for i in range(len(Baxis)):
    #     if i in range(0, B[0]):
    #         Baxis[i] = 0
    #     elif i in range(B[0], B[1]):
    #         Baxis[i] = 1
    #     elif i in range(B[1], B[2]):
    #         Baxis[i] = 2
    #     elif i in range(B[2], B[3]):
    #         Baxis[i] = 3
    #     elif i in range(B[3], 10):
    #         Baxis[i] = 4

    # indices = [i for i in range(len(Aaxis)) if Aaxis[i]>=Baxis[i]]
    # print(Aaxis)
    # print(Baxis)
    # print(indices)

    # for p1 in indices:
    #     for p2 in indices:
    #         for p3 in indices:
    #             for p4 in indices:
    #                 if Aaxis[p1]+Aaxis[p2]+Aaxis[p3]+Aaxis[p4]>=8 and Baxis[p1]+Baxis[p2]+Baxis[p3]+Baxis[p4]<8:
    #                     combination = [p1+1, p2+1, p3+1, p4+1]
    #                     # print('combination:', combination)
    #                     return 'yes'

    # ans2 = 'no'
    for p1 in range(10):
        for p2 in range(10):
            for p3 in range(10):
                for p4 in range(10):
                    C = [p1+1, p2+1, p3+1, p4+1]
                    CbeatA = [[i, j] for j in range(4) for i in range(4) if C[i] > A[j]]
                    AbeatC = [[i, j] for j in range(4) for i in range(4) if A[i] > C[j]]
                    CbeatB = [[i, j] for j in range(4) for i in range(4) if B[i] > B[j]]
                    BbeatC = [[i, j] for j in range(4) for i in range(4) if B[i] > C[j]]
                    if len(CbeatA) > len(AbeatC) and BbeatC > CbeatB:
                        return 'yes'
                    # print(p1, p2, p3, p4)
                    # if Aaxis[p1]+Aaxis[p2]+Aaxis[p3]+Aaxis[p4]>=8 and Baxis[p1]+Baxis[p2]+Baxis[p3]+Baxis[p4]<8:
                    #     combination = [p1+1, p2+1, p3+1, p4+1]
                        # print('combination:', combination)
                        # return 'yes'
    return 'no'
    # print('ans1:', ans1)
    # print('ans2:', ans2)


# d1 = sorted([random.randint(1, 10) for i in range(4)])
# d2 = sorted([random.randint(1, 10) for i in range(4)])
# print('d1:', d1)
# print('d2:', d2)

# d1s = []
# d2s = []
# for i in range(10):
#     d1 = sorted([random.randint(1, 10) for i in range(4)])
#     d1s.append(d1)
#     d2 = sorted([random.randint(1, 10) for i in range(4)])
#     d2s.append(d2)
#
# ans = solve(d1, d2)
# print(ans)


for i in range(len(d1s)):
    # print(d1s[i])
    # print(d2s[i])
    ans = solve(d1s[i], d2s[i])
    print(ans)