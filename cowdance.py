
NM = [int(i) for i in input().split()]
N = NM[0]
M = NM[1]
durations = []
for i in range(N):
    durations.append(int(input()))


def check(size):
    onstage = sorted(durations[0:size])
    offstage = durations[size:]
    for cow in range(len(offstage)):
        kicked = min(onstage)
        ind = onstage.index(kicked)
        onstage[ind] = onstage[ind]+offstage[cow]
        if onstage[ind] > M:
            return False
    return True


def binary_search():
    low = 1
    high = N
    mid = (low + high)//2
    while low <= high:
        mid = (low + high)//2
        if check(mid):
            high = mid - 1
        else:
            low = mid + 1
    print(mid)


binary_search()