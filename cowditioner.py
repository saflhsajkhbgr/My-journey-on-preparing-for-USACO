
n = int(input())
target = [int(i) for i in input().split()]
current = [int(i) for i in input().split()]
gap = [target[i]-current[i] for i in range(n)]

"""
02002
"""


ans = 0
pos = 0
# 第一个非零的位置
while True:
    start = 0
    end = 0
    pos_or_neg = None
    for i in range(pos, n):
        if gap[i] == 0 and pos_or_neg == None:
            pass
        else:
            # 正区间
            if gap[i] > 0:
                if pos_or_neg == None:
                    start = i
                    pos_or_neg = True
                    # print(start)
                elif pos_or_neg == False:
                    end = i-1
                    break
            # 负区间
            if gap[i] < 0:
                if pos_or_neg == None:
                    start = i
                    pos_or_neg = False
                elif pos_or_neg == True:
                    end = i-1
                    break

            if gap[i] == 0 and pos_or_neg != None:
                end = i-1
                break

            if i == len(gap)-1 and gap[i] != 0:
                end = i
                break
    # print(start)
    # print(end)
    if pos_or_neg == True:
        m = min(gap[start:end+1])
        ans += m
        for i in range(start, end+1):
            gap[i] -= m

    elif not pos_or_neg:
        m = max(gap[start:end+1])
        ans += abs(m)
        for i in range(start, end+1):
            gap[i] -= m

    flag = True
    for i in range(pos, n):
        if gap[i] != 0:
            pos = i
            # print(pos)
            flag = False
            break
    # print(gap)
    if flag:
        break

print(ans)