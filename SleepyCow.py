import time
# 定义不可达距离
_ = float('inf')

"""
USACO 2019 January Contest, Bronze
Problem 2. Sleepy Cow Sorting
http://usaco.org/index.php?page=viewproblem2&cpid=892
"""


def read(dir):
    lst = []
    with open(dir) as f:
        while True:
            line = f.readline().split()
            if not line:
                break
            l = [int(i) for i
                 in line]
            lst.append(l)
    return lst


# lst = [[4], [1, 2, 4, 3]]
# print(cor)
lst = read('sleepy_bronze_jan19/5.in')
num = lst[0][0]
l = lst[1]
cor = [i+1 for i in range(num)]
tobfix = []
for cow in range(len(l)):
    if l[cow] != cor[cow]:
        tobfix.append(l[cow])


def shift(b):
    c = l[0]
    for i in range(len(l)):
        if l[i] != b:
            l[i] = l[i+1]
        else:
            l[i] = c
            break


def overtime():
    ans = 0
    while l != cor:
        if l[0] not in tobfix:
            for i in range(l.index(tobfix[0])+1, num+1):
                if i == num:
                    shift(l[-1])
                    break
                if l[0] < l[i]:
                    shift(l[i-1])
                    break
        else:
            for i in range(num+1):
                if i == num:
                    shift(l[-1])
                    break
                elif l[0] < l[i]:
                    tobfix.remove(l[0])
                    shift(l[i-1])
                    break
        print(l)
        ans += 1

# print(ans)
with open('sleepy.out', 'w') as f:
    f.write()