
num = int(input())
ans = 0
counter = 0
for i in range(100000):
    for j in range(100000):
        ans = i*4+j*5
        if ans == num:
            # print(i, j)
            counter += 1
        if ans > num:
            break

print(counter)