
_ = float('inf')

with open('hoofball.in', 'r') as file:
    n = file.readline()
    cows = sorted([int(i) for i in file.readline().split()])

# cows = [1, 2, 4, 7, 10]

subgroups = []

while cows:
    currentcow = cows[0]
    read = [currentcow]
    while True:
        dis = _
        for cow in cows:
            # print('cow:', cow)
            if cow != currentcow and abs(currentcow-cow) <= dis:
                dis = abs(currentcow-cow)
                nextcow = cow
        if nextcow in read:
            # print(read)
            cows = [i for i in cows if i not in read]
            subgroups.append(read)
            # print(cows)
            read = []
            break
        else:
            read.append(nextcow)
            currentcow = nextcow

# print(read)
ans = len(subgroups)
with open('hoofball.out', 'w') as file:
    file.write(str(ans))