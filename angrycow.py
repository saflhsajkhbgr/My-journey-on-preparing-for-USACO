
nb = [int(i) for i in input().split()]
n = nb[0]
bombs = nb[1]

hales = []
for i in range(n):
    hales.append(int(input()))
hales = sorted(hales)


def check(r):
    global bombs
    b = bombs
    pointer = hales[0]
    while pointer <= hales[-1]:
        pointer += 2*r
        # print(pointer)
        b -= 1
        for i in hales:
            if i >= pointer:
                pointer = i
                break
    if b < 0:
        return False
    return True

# print(check(6))


def binary_search():
    low = 0
    high = hales[-1]
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            high = mid-1
        else:
            low = mid+1
    print(low)


binary_search()