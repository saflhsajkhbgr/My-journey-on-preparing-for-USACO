
with open('evolution.in', 'r') as file:
    species = []
    n = int(file.readline())
    for i in range(n):
        line = file.readline().split()[1:]
        species.append(line)

# species = [['spots', 'firebreathing'], [], ['flying'], ['telepathic', 'flying']]


def solve():
    for cow1 in species:
        if cow1:
            # print('cow1:', cow1)
            for cow2 in species:
                if cow2 and cow2 != cow1:
                    # print('cow2:', cow2)
                    for charac in cow2:
                        if charac in cow1:
                            # print(charac, 'matches')
                            flag = True
                            break
                        else:
                            flag = False
                    if flag:
                        if len(cow1) > len(cow2):
                            if len(set(cow1+cow2)) == len(cow1):
                                pass
                            else:
                                return 'no'
                        if len(cow2) > len(cow1):
                            if len(set(cow1+cow2)) == len(cow2):
                                pass
                            else:
                                return 'no'
    return 'yes'


ans = solve()
with open('evolution.out', 'w') as file:
    file.write(str(ans))