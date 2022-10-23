

# 定义不可达距离
_ = float('inf')
# s = [s[i] for i in range(len(s))]


def f1(string):
    Gnum = 0
    Hnum = 0
    for s in string:
        if s == 'H':
            Hnum += 1
        if s == 'G':
            Gnum += 1
        if Gnum > 1 and Hnum > 1:
            return False
    return True


def f2(l):
    string = l
    Gnum = string.count('G')
    Hnum = string.count('H')
    if Gnum > 1 and Hnum > 1:
        return False
    else:
        return True


# print(f2(['H', 'G', 'H', 'H', 'H', 'H']))


def substring():
    counter = 0
    length = 3
    pos = 0
    while length <= len(s):
        ch = f2(s[pos:pos+length])
        # print(ch)
        if ch:
            # print(s[pos:pos+length])
            counter += 1
        if pos+length == len(s):
            length += 1
            pos = 0
        else:
            pos += 1
    return counter


num = input()
s = input()

ans = substring()
print(ans)


import time

# string = 'GHGHGGHGHGGGGGHGHGHGGGGHHHGHGHGHHHGGHGHGHHGHHHHHHGHHHGHHHGGGGHGHGGHGHGGHGHGGGGGHGHGHGGGGHHHGHGHGHHHGGHGHGHHG' \
#     'HHHHHHGHHHGHHHGGGGHGHGGHGHGGHGHGGGGGHGHGHGGGGHHHGHGHGHHHGGHGHGHHGHHHHHHGHHHGHHHGGGGHGHGHHHGHGHGHHHGGHGHGHHGHHHHHHG' \
#     'HHHGHGHGHHHGGHGHGHHGHHHHHHGHHHGHGHGHHHGGHGHGHHGHHHHHHGGHGHGHHGHHHHHHGHHHGHGHGHHHGGHGHGHGHGHGHHGHHHHHHGHHHGHGHGHHHGG' \
#     'HHGHHHHHHGHHHGHGHGHHHGGHGHGHHGHHHHHHGGHGHGHHGHHHHHHGHHHGHGHGHHHGGHGHGHGHGHGHHGHGHHHGGHGHGHGHGHGHHGHGGHGH' \
#     'GGGGGHGHGHGGGGHHHGHGHGHHHGGHGHG'
#
# l = [string[i] for i in range(len(string))]


# t1 = time.time()
# ans = f1()
# t2 = time.time()
# print('cost1:', t2-t1)

# t3 = time.time()
# ans = f2()
# t4 = time.time()
# print('cost2:', t4-t3)