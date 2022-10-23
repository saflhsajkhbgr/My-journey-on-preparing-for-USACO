
"""
6 3 2
1 1 3 4 10 14
1 1 4 10 14
"""

nmc = [int(i) for i in input().split()]
n = nmc[0]
m = nmc[1]
c = nmc[2]

times = sorted([int(i) for i in input().split()])
timestamp = [times[0]]
timestamp.extend(times)


def check(t):
    pos = 1
    bus = 1
    first = 1
    while pos != n+1:
        wait = timestamp[pos]-timestamp[first]
        if wait > t or pos-first+1 > c:
            bus += 1
            first = pos
        pos += 1
        if bus > m:
            return False
    return True


def binary_search():
    low = timestamp[0]
    high = timestamp[-1]
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            high = mid-1
        else:
            low = mid+1
    print(mid)


binary_search()