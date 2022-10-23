
# lst = [[4], ['bird', 2, 'flies eatsworms'],
#            ['cow', 4, 'eatsgrass', 'isawesome', 'makesmilk', 'goesmoo'],
#            ['sheep', 1, 'eatsgrass'],
#            ['goat', 2, 'makesmilk eatsgrass']]


def read(dir):
    dct = {}
    with open(dir) as f:
        while True:
            line = f.readline().split()
            if not line:
                break
            dct[line[0]] = line[3:]
    return dct


dct = {'bird': ['flies', 'eatsworms'],
       'cow': ['eatsgrass', 'isawesome', 'makesmilk', 'goesmoo'],
       'sheep': ['eatsgrass'],
       'goat': ['makesmilk', 'eatsgrass']}


# 保证每次问问题都能够最小化aniset的损失
# ask the questions with a characteristic that is shared the most
aniset = [i for i in dct.keys()]
character = [j for i in dct.values() for j in i]
ans = 0
c = 0
setcharacter = list(set(character))
characcount = [character.count(i) for i in setcharacter]
while len(aniset) != 1:
    setcharacter = list(set([j for i in aniset for j in dct[i]]))
    print('setcharacter:', setcharacter)
    print('characcount:', characcount)
    N_question = setcharacter[characcount.index(min(characcount))]
    Y_question = setcharacter[characcount.index(max(characcount))]
    print('N_question:', N_question)
    print('Y_question:', Y_question)
    N = aniset.copy()
    Y = aniset.copy()
    for n in N:
        if N_question in dct[n]:
            N.remove(n)
    for y in Y:
        if Y_question not in dct[y]:
            Y.remove(y)
    if len(N) >= len(Y):
        aniset = N
        characcount.remove(min(characcount))
        setcharacter.remove(N_question)
    else:
        aniset = Y
        characcount.remove(max(characcount))
        setcharacter.remove(Y_question)
    ans += 1
    print('N:', N)
    print('Y:', Y)
    print('aniset:', aniset)
    print('-'*50+'iter end'+'-'*50)
    c += 1
    if c == 6:
        break

print(ans)