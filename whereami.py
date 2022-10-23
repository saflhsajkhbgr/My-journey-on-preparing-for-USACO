
with open('whereami.in', 'r') as file:
    N = file.readline()
    boxes = file.readline()

# boxes = 'ABCDABC'


def solve():
    K = 2
    flag = True
    while flag:
        lst = []
        for i in range(len(boxes)):
            if i+K == len(boxes) and [j for j in boxes[i:i+K]] not in lst:
                return K
            combination = [j for j in boxes[i:i+K]]
            # print('combination:', combination)
            if combination not in lst:
                lst.append(combination)
            else:
                break
        K += 1


K = solve()

with open('whereami.out', 'w') as file:
    file.write(str(K))