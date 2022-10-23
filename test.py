# 定义不可达距离
_ = float('inf')

num = input()
s = input()
s = [s[i] for i in range(len(s))]


def read(dir):
    lst = []
    with open(dir) as f:
        while True:
            line = f.readline().split()
            if not line:
                break
            l = [i for i in line]
            lst.append(l)
    # lst = lst[1:]
    return lst


def check(s):
    Gnum = s.count('G')
    Hnum = s.count('H')
    if Gnum == 1 or Hnum == 1:
        return True
    else:
        return False

# print(check(['H', 'G',]))


def substring():
    counter = 0
    length = 3
    s = ['G', 'H', 'G', 'H', 'G']
    pos = 0
    while length <= len(s):
        ch = check(s[pos:pos+length])
        if ch:
            counter += 1
        if pos+length == len(s):
            length += 1
            pos = 0
        else:
            pos += 1
    return counter


ans = substring()
print(ans)