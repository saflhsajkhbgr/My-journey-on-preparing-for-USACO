
import time
# 定义不可达距离
_ = float('inf')
# exchange = [[1, 2, 1], [3, 2, 1], [1, 3, 1]]


def read(dir):
    lst = []
    with open(dir) as f:
        while True:
            line = f.readline().split()
            if not line:
                break
            l = [int(i) for i in line]
            lst.append(l)
    # lst = lst[1:]
    return lst


def switch(ex):
    tem = l[ex[1]-1]
    l[ex[1] - 1] = l[ex[0] - 1]
    l[ex[0]-1] = tem

# switch([1, 2, 3], l)
# print(l)
# switch([2, 3, 2], l)
# print(l)
# switch([3, 2, 3], l)
# print(l)
# switch([2, 1, 1], l)
# print(l)

def f(guess, x2, cor):
    if cor == guess:
        return x2+1, cor
    else:
        return x2, cor


exchange = read('shell.in')[1:]
# y = [_ for i in range(len(exchange))]
# for i in range(len(exchange)):
#     switch(exchange[i])
#     # 初始化
#     if i == 0:
#         y[i] = 1
#         cor = l[exchange[i][2]-1]
#     else:
#         y[i], cor = f(guess=l[exchange[i][2]-1], x2=y[i-1], cor=cor)
# ans = y[-1]
# with open('shell.out', 'w') as f:
#     f.write(str(ans))

# print(exchange)

ans = []
for i in range(3):
    cor = 0
    stone = i+1
    l = [1, 2, 3]
    print('ans:', stone)
    for j in range(len(exchange)):
        switch(exchange[j])
        pred = exchange[j][2]
        if stone == l[pred-1]:
            cor += 1
    ans.append(cor)

ans = max(ans)
with open('shell.out', 'w') as f:
    f.write(str(ans))