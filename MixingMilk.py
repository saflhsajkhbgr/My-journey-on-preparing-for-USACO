
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


def milk_bucket(inp):
    """
    Question: three buckets, pour milk from 1 to 2, 2 to 3, 3 to 4. Stop pouring if one empty or one full,
    print the amount left in each bucket after 100 iterations.
    e.g. [[10, 3], [11, 4], [12, 5]] => 0, 10, 2
    :param inp: such that [[capacity1, milk1], [capacity2, milk2], [capacity3, milk3]]
    :return: milk amount in each bucket
    """
    counter = 0
    i = 0
    while counter != 100:
        if i == 2:
            res = inp[0][1] + inp[2][1]
            if res > inp[0][0]:
                inp[0][1] = inp[0][0]
                inp[2][1] = res - inp[0][0]
            else:
                inp[0][1] = res
                inp[2][1] = 0
            i = 0
        else:
            res = inp[i][1] + inp[i+1][1]
            if not res > inp[i+1][0]:
                inp[i+1][1] = res
                inp[i][1] = 0
            else:
                inp[i+1][1] = inp[i+1][0]
                inp[i][1] = res - inp[i+1][0]
            i += 1
        counter += 1
    ans = []
    for j in inp:
        ans.append(j[1])
    return ans


lst = read('mixmilk.in')
ans = milk_bucket(lst)
with open('mixmilk.out', 'w') as f:
    for a in ans:
        f.write(str(a)+'\n')