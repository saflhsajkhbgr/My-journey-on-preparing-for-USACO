
# 定义不可达距离
_ = float('inf')


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


# lst = [[5, 6], [4, 1], [4, 2], [4, 3], [2, 5], [1, 2], [1, 5]]
lst = read('revegetate_bronze_feb19 /3.in')

import sys
ans = [_ for i in range(lst[0][0])]
digit = lst[0][0]


def check(cur):
    res = True
    for l in lst[1:]:
        if cur[l[0]-1] != cur[l[1]-1]:
            pass
        else:
            res = False
    return res


# print(check([1, 1, 2, 3, 1, 2, 2, 2, 2]))

def func(iteration, last):
    for i in range(3):
        if i+1 == 3 and last == 3:
            pass
        else:
            ans[iteration] = i+1
            print(ans)
            if check(ans):
                print('-'*50+'got it'+'-'*50)
                with open('revegetate.out', 'w') as f:
                    for i in ans:
                        f.write(str(i))
                sys.exit()
            elif iteration != digit-1:
                func(iteration+1, i+1)


func(0, 0)