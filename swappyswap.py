
with open('swap.in', 'r') as file:
    NnK = [int(i) for i in file.readline().split()]
    op1 = [int(i) for i in file.readline().split()]
    op2 = [int(i) for i in file.readline().split()]

# NnK = [7, 2]
# op1 = [2, 5]
# op2 = [3, 7]

lst = [i+1 for i in range(NnK[0])]
for i in range(NnK[1]):
    lstop1 = lst[op1[0]-1:op1[1]].copy()
    lstop1.reverse()
    # print('after op1:', lstop1)
    for l in range(len(lstop1)):
        lst[op1[0]-1+l] = lstop1[l]
    # print(lst)

    lstop2 = lst[op2[0]-1:op2[1]].copy()
    lstop2.reverse()
    # print('after op2:', lstop2)
    for l in range(len(lstop2)):
        lst[op2[0]-1+l] = lstop2[l]


with open('swap.out', 'w') as file:
    for i in lst:
        file.write(str(i)+'\n')