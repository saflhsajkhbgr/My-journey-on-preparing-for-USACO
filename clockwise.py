
n = int(input())

for inp in range(n):
    countleft = 0
    countright = 0
    route = input()
    current = route[0]
    for dir in route[1:]:
        if dir == 'N' and current == 'E':
            countleft += 1
        if dir == 'N' and current == 'W':
            countright += 1
        if dir == 'S' and current == 'W':
            countleft += 1
        if dir == 'S' and current == 'E':
            countright += 1
        if dir == 'E' and current == 'N':
            countright += 1
        if dir == 'E' and current == 'S':
            countleft += 1
        if dir == 'W' and current == 'N':
            countleft += 1
        if dir == 'W' and current == 'S':
            countright += 1
        current = dir
    # print(countright)
    # print(countleft)
    if countright > countleft:
        print('CW')
    else:
        print('CCW')