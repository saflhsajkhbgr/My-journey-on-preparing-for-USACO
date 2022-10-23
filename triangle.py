
with open('triangles.in', 'r') as file:
    n = file.readline()
    points = []
    for i in range(int(n)):
        points.append([int(i) for i in file.readline().split()])

# points = [[0, 0], [0, 1], [1, 0], [1, 2]]

maxA = 0
# right angle vertex
for p in points:
    maxx = 0
    maxy = 0
    # print('cur vertex:', p)
    corp1 = None
    corp2 = None
    for rest in points:
        if rest != p:
            # print('point', rest)
            # print('maxx:', maxx)
            # print('maxy:', maxy)
            # if x1 = x2
            if rest[0] == p[0] and abs(rest[1]-p[1]) > maxy:
                # print('point', rest, 'satisfies')
                corp1 = rest
                maxy = abs(rest[1]-p[1])
            # if y1 = y2
            elif rest[1] == p[1] and abs(rest[0]-p[0]) > maxx:
                # print('point', rest, 'satisfies')
                corp2 = rest
                maxx = abs(rest[0]-p[0])
            # print('-'*100)
    if corp1 and corp2 and maxx*maxy > maxA:
        maxA = maxx*maxy
    # print(corp1)
    # print(corp2)
    # print('Area:', maxx*maxy)
    # print('-' * 100)


# print('max Area:', maxA)
with open('triangles.out', 'w') as file:
    file.write(str(maxA))