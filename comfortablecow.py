
n = input()
coordinates = []
cows = {}

for i in range(int(n)):
    coor = [int(i) for i in input().split()]
    coordinates.append(coor)
    counter = 4
    surroudning = [[coor[0] - 1, coor[1]], [coor[0] + 1, coor[1]], [coor[0], coor[1] - 1], [coor[0], coor[1] + 1]]
    for pos in surroudning:
        if pos in coordinates:
            cows[str(pos[0])+str(pos[1])] -= 1
            counter -= 1
    cows[str(coor[0]) + str(coor[1])] = counter
    ans = list(cows.values()).count(1)
    print(ans)