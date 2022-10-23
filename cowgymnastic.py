
with open('gymnastics_bronze_dec19/3.in', 'r') as file:
    nk = file.readline().split()
    n = int(nk[0])
    k = int(nk[1])
    classes = []
    for i in range(n):
        classes.append([int(i) for i in file.readline().split()])

# classes = [[4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3]]
# k = 4
pairs = [[i+1, j+1] for i in classes[0] for j in classes[0] if i != j and j > i]
print(pairs)

for p in pairs:
    for c in range(len(classes)):
        if c == 0:
            if classes[c].index(p[1]) > classes[c].index(p[0]):
                order = True
                # True: ascending order
                # print('the order of', [p[0], p[1]], 'is ascending')
            else:
                order = False
                # False: descending order
                # print('the order of', [p[0], p[1]], 'is descending')
        else:
            if order:
                if classes[c].index(p[1]) < classes[c].index(p[0]):
                    pairs.remove([p[0], p[1]])
                    break
                else:
                    pass
            else:
                if classes[c].index(p[1]) > classes[c].index(p[0]):
                    pairs.remove([p[0], p[1]])
                    break
                else:
                    pass

ans = len(pairs)
print(ans)
# with open('gymnastics.out', 'w') as file:
#     file.write(str(ans))