

def check1(string):
    Hnum = 0
    Gnum = 0
    for s in string:
        if s == 'H':
            Hnum += 1
        if s == 'G':
            Gnum += 1
        if Gnum > 1 and Hnum > 1:
            return False
    return True


def check2(s):
    Gnum = s.count('G')
    Hnum = s.count('H')
    if Gnum == 1 or Hnum == 1:
        return True
    else:
        return False


num = input()
inp = input()


# alpha = ['G', 'H']
# import random
import time

# inp = [alpha[random.randint(0, 1)] for i in range(10000)]

# inp = 'GHGHG'
string = []
for s in inp:
    if s == 'G':
        string.append(0)
    else:
        string.append(1)
# print('string:', string)


def check3(s):
    if sum(s) == 1 or sum(s) == len(s)-1:
        # print(s, '=> True')
        return True
    else:
        # print(s, '=> False')
        return False


pos = 0
counter = 0
c = 0
t1 = time.time()
while pos <= len(string)-3:
    # print('pos:', pos)
    c += 1
    # print(range(pos+2, len(string)-1))
    if pos == len(string)-3:
        if check3(string[-3:]):
            counter += 1
        break
    else:
        flag = False
        for i in range(pos+2, len(string)):
            sub = string[pos:i+1]
            if check3(sub):
                counter += 1
                flag = True
            elif flag:
                pos += 1
                break
            if i+1 == len(string):
                pos += 1
                # print('pos:', pos)
                break
    t2 = time.time()
    if t2 -t1 >= 3.5:
        break
    # if c == 15:
    #     break

print(counter)
# print('cost:', t2-t1)