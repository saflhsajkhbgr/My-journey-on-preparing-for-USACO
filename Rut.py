
# 定义不可达距离
_ = float('inf')
import time

lst = []
with open('prob3_bronze_dec20/6.in') as f:
    while True:
        line = f.readline().split()
        if not line:
            break
        l = [i for i in line]
        lst.append(l)
lst = lst[1:]
print(lst)


# lst = [['E', 3, 5], ['N', 5, 3], ['E', 4, 6], ['E', 10, 4], ['N', 11, 2], ['N', 8, 1]]


# num = int(input())
# lst = []
# for i in range(num):
#     s = input().split()
#     lst.append(s)


def Emove(s, a, b):
    return s, int(a)+1, int(b)
def Wmove(s, a, b):
    return s, int(a)-1, int(b)
def Nmove(s, a, b):
    return s, int(a), int(b)+1
def Smove(s, a, b):
    return s, int(a), int(b)-1


def simulation(L):
    lst = []
    for l in L:
        if l == []:
            lst.append([])
        elif l[0] == 'E':
            [s, a, b] = Emove(l[0], l[1], l[2])
            lst.append([s, a, b])
        elif l[0] == 'W':
            [s, a, b] = Wmove(l[0], l[1], l[2])
            lst.append([s, a, b])
        elif l[0] == 'N':
            [s, a, b] = Nmove(l[0], l[1], l[2])
            lst.append([s, a, b])
        elif l[0] == 'S':
            [s, a, b] = Smove(l[0], l[1], l[2])
            lst.append([s, a, b])
    return lst

t1 = time.time()
# dct = {i: [] for i in range(len(lst))}
L = []
ans = [_ for i in lst]
step = 0
t1 = time.time()
while True:
    step += 1
    for i in lst:
        if i:
            L.append([i[1], i[2]])
    lst = simulation(lst)
    t01 = time.time()
    for l in lst:
        # print('lst:', lst)
        if l:
            t11 = time.time()
            if [l[1], l[2]] in L:
                # print('found:', [l[1], l[2]], 'in', L)
                ans[lst.index(l)] = step
                lst[lst.index(l)] = []
            t12 = time.time()
            print('cost:', t12-t11)
    t02 = time.time()
    print('total cost:', t02-t01)
    t2 = time.time()
    if t2-t1 >= 3.5:
        # print('cost:', t2-t1)
        break
for a in ans:
    if a != _:
        print(a)
    else:
        print('Infinity')