
def solve():
    NnL = input().split()
    N = int(NnL[0])
    L = int(NnL[1])
    articles = sorted([int(i) for i in input().split()], reverse=True)
    # L = 2
    # articles = sorted([7, 4, 3, 2, 1], reverse=True)
    # articles = sorted([1, 2, 2, 100], reverse=True)
    # print(articles)

    counter = 0
    maxh = articles[counter]
    while True:
        indices = [i for i in range(len(articles)) if articles[i] >= maxh]
        if len(indices) >= maxh:
            h = maxh
            break
        else:
            counter += 1
            maxh = articles[counter]
    # print(h)

    while L != 0:
        indices = [i for i in range(len(articles)) if articles[i] < h+1]
        # print('indices:', indices)
        gaps = []
        for i in indices:
            gaps.append(h+1-articles[i])
        # print('gaps:', gaps)
        needed = h+1-(len(articles)-len(indices))
        # print('needed:', needed)
        for i in range(needed):
            if gaps[i] <= L:
                L -= gaps[i]
                # print('L:', L)
            else:
                return h
            articles[indices[i]] = h + 1
            # print('articles:', articles)
        h += 1
    return h


print(solve())