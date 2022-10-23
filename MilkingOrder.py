
# 定义不可达距离
_ = float('inf')


def read(dir):
    lst = []
    with open(dir) as f:
        while True:
            line = f.readline().split()
            if not line:
                break
            l = [int(i) for i in line]
            lst.append(l)
    # lst = lst[1:]
    return lst


lst = [[6, 3, 2], [4, 5, 6], [5, 3], [3, 1]]
ans = [_ for i in range(lst[0][0])]

for fix in lst[2:]:
    ans[fix[1]-1] = fix[0]

ranked = lst[1].copy()
while ranked:
    rank = 0
    if len(ranked) == 1:
        for i in range(len(ans)):
            if ans[-(i+1)] == _:
                ans[-(i+1)] = ranked[rank]
                ranked.remove(ranked[rank])
                break
        break
    if ranked[rank] not in ans:
        for pos in range(len(ans)):
            if pos+len(ranked) == len(ans)+1:
                # [0, 1, 2, 3, _, _], [5, 6]
                ans[pos] = ranked[rank]
                ranked.remove(ranked[rank])
                rank = 0
                break
            if ans[pos] == _ and ans[pos+1] == ranked[rank+1]:
                print('ans[pos+1]:', ans[pos+1])
                print('ranked[rank+1]:', ranked[rank+1])
                print('len(ans)-(pos+1):', len(ans)-(pos+1))
                # for i in range(len(ans)-(pos+1)):
                #     if ans[-i] == _:
                #         ans[-(i+1)] = ranked[rank]
                #         ranked.remove(ranked[rank])
                #         rank = 0
                #         break
                break
    else:
        ranked.remove(ranked[rank])


print(ans)