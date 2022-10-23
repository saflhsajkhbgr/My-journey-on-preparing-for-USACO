
blocks = []

n = int(input())
for i in range(4):
    blocks.append(set([i for i in input()]))

for i in range(n):
    used = [False, False, False, False]
    word = input()

    dic = {}
    for j in range(4):
        dic[j] = []

    for k in range(4):
        counter = 0
        for letters in word:
            if letters in blocks[k]:
                dic[k].append(letters)
    ans = 0
    for letters in word:
        min = 100000000
        for block in dic:
            if not used[block]:
                if letters in dic[block] and len(dic[block]) < min:
                    min = len(dic[block])
                    take = block
        if min != 100000000:
            used[take] = True
            ans += 1

    if ans == len(word):
        print('YES')
    else:
        print('NO')