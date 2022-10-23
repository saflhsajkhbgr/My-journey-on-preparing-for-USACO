
T = int(input())
cases = []
for i in range(T):
    n = int(input())
    hunger = [int(i) for i in input().split()]
    cases.append(hunger)

# cases = [[8, 10, 5], [4, 6, 4, 4, 6, 4], [0, 1, 0], [1, 2], [10, 9, 9]]
# cases = [[3, 7, 6, 6, 5]]
"""
4 6 4 4 6 4
4 4 2 4 6 4
4 4 2 2 4 4
4 4 2 2 2 2
2 2 2 2 2 2
"""
# cases = [[8, 10, 5], [4, 6, 4, 4, 6, 4], [0, 1, 0], [1, 2], [10, 9, 9]]
# cases = []
# with open('prob3_bronze_jan22/2.in', 'r') as file:
#     n = file.readline()
#     for i in range(int(n)):
#         t = file.readline()
#         cases.append([int(i) for i in file.readline().split()])

for cows in cases:
    # print(cows)
    counter = 0
    if len(cows) == 2 and cows[0] != cows[1]:
        counter = -1
        print(counter)
        continue
    if len(cows) == 1 or (len(cows) == 2 and cows[0] == cows[1]):
        print(0)
        continue
    flag = True
    while flag:
        mini = min(cows)
        # print(cows)
        for j in range(len(cows)-1):
            if cows[j] > mini:
                gap = cows[j] - mini
                cows[j+1] -= gap
                cows[j] = mini
                counter += gap
                mini = min(cows)
                # print(cows)
                if len(set(cows)) == 1:
                    print(counter*2)
                    flag = False
                    break
        if mini < 0:
            counter = -1
            print(counter)
            break